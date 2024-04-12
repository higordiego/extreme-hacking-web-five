# Guia de Construção Go Remote Code Execution

## Introdução

**OS**: Debian 12
**Hostname**: extreme-go-remote-code
**Vulnerability 1**: Directory public
**Vulnerability 2**: Code Remote Execution in Golang
**Vulnerability 2**: Privilege Scalation


## Required Settings

**CPU**: 2 CPU  
**Memory**: 2GB  
**Disk**: 20GB

### Install
**Docker**: Docker version 25.0.3 ou superior
**Docker compose** Docker Compose version v2.24.6 ou superior

## Build Guide
1. Copiar o conteudo da pasta src para /root
2. Mover o build.sh para o diretório do linux do usuário que está manuseando.
3. Dar permissões de execução no build.sh
4. Executar como root o build.sh