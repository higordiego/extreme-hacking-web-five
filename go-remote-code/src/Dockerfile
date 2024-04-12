# Usa uma imagem base do Ubuntu
FROM ubuntu:18.04

# Atualiza os pacotes e instala as dependências necessárias
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    git \
    nano \
    vim \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cria o diretório de trabalho
WORKDIR /home/extremehacking/app

# Baixa o arquivo do Go com permissões adequadas
RUN wget -O go.tar.gz https://golang.org/dl/go1.21.1.linux-amd64.tar.gz

# Extrai o arquivo do Go
RUN tar -C /home/extremehacking -xzf go.tar.gz && \
    rm go.tar.gz

# Define as variáveis de ambiente para Go
ENV PATH $PATH:/home/extremehacking/go/bin
ENV GOPATH /home/extremehacking/go

# Adiciona o usuário extremehacking
RUN useradd -ms /bin/bash extremehacking

# Copia o código fonte para o contêiner
COPY . .

# Compila o código Go
RUN go build -o app

# Remove o Dockerfile após a compilação
RUN rm -f Dockerfile
RUN rm -f go.mod
RUN rm -f README.md
RUN rm -f main.go

# Define as permissões do arquivo app para o usuário extremehacking
RUN chown extremehacking:extremehacking /home/extremehacking/app/app

# Adiciona um arquivo somente leitura como root
USER root
RUN touch /root/flag_pwn.txt && chmod 400 /root/flag_pwn.txt
RUN echo "Extreme{6630db853468e9c768a584981349e924}" > /root/flag_pwn.txt

USER extremehacking
# Comando para iniciar o servidor SSH e o servidor Go quando o contêiner for executado
CMD ./app
