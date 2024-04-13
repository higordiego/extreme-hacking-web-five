package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"os/exec"
)

func handler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Método não permitido", http.StatusMethodNotAllowed)
		return
	}

	code, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Erro ao ler o corpo da solicitação", http.StatusInternalServerError)
		return
	}

	
	output, err := executeCode(string(code))
	if err != nil {
		log.Println(err.Error())
		http.Error(w, "Erro ao executar o código", http.StatusInternalServerError)
		return
	}

	log.Println("estou aqui")
	fmt.Fprintf(w, "\n%s", output)
}

func executeCode(code string) (string, error) {
	tempFile, err := ioutil.TempFile("", "remote-go-code-*.go")
	if err != nil {
		return "", err
	}
	defer os.Remove(tempFile.Name())

	_, err = tempFile.WriteString(code)
	if err != nil {
		return "", err
	}
	tempFile.Close()

	cmd := exec.Command("go", "run", tempFile.Name())
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return "", err
	}

	if err := cmd.Start(); err != nil {
		return "", err
	}

	outputBytes, err := ioutil.ReadAll(stdout)
	if err != nil {
		return "", err
	}

	return string(outputBytes), nil
}

func handlerFile(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Método não permitido", http.StatusMethodNotAllowed)
		return
	}

	tmpl, err := template.ParseFiles("index.html")
	if err != nil {
		http.Error(w, "Erro ao carregar o modelo", http.StatusInternalServerError)
		return
	}

	err = tmpl.Execute(w, nil)
	if err != nil {
		http.Error(w, "Erro ao renderizar o modelo", http.StatusInternalServerError)
		return
	}
}

func handlerHealth(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Método não permitido", http.StatusMethodNotAllowed)
		return
	}

	fmt.Fprintf(w, "ok")
}

func handleDeploy(w http.ResponseWriter, r *http.Request) {
	filename := r.URL.Query().Get("filename")
	if filename == "" {
		http.Error(w, "Por favor, forneça o parâmetro 'filename' na URL", http.StatusBadRequest)
		return
	}

	fileContent, err := readFile(filename)
	if err != nil {
		http.Error(w, fmt.Sprintf("Erro ao ler o arquivo '%s': %v", filename, err), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprintf(w, "Conteúdo do arquivo '%s':\n%s\n", filename, fileContent)
}

func readFile(filename string) (string, error) {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func main() {
	http.HandleFunc("/health", handlerHealth)
	http.HandleFunc("/", handlerFile)
	http.HandleFunc("/public", handleDeploy)
	http.HandleFunc("/deploy", handler)

	port := os.Getenv("PORT")

	if port == "" {
		port = "8080"
	}

	fmt.Printf("Servidor rodando em http://localhost:%s\n", port)
	http.ListenAndServe(":"+port, nil)
}
