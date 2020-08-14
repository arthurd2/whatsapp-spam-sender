# Enviador de Mensagens via Whatsapp
Este script serve para mandar a mesma mensagem (Quick Reply) para varios contatos.
Ele:
* le os nomes de um arquivo
* abre o whatsapp web
* para cada nome:
    * limpa o campo de busca
    * busca o nome
    * escreve mensagem e envia
## Instalação
* Clonar este repositorio
* Instalar pacotes necessarios
```sh
apt install python3 pip3
pip3 install -r requirements.txt
```
* Baixar o [Driver do Chrome](https://chromedriver.chromium.org/downloads) da mesma versão do instalado em sua maquina.
## Configurando
* Por padrão ele:
    * manda a Quick Message `/m2` , basta configurar ela no seu WhatsApp.
    * lê o arquivo `./contatos` e busca o nome dos destinatarios la.

## Executando
* Abra seu whatsapp e deixe pronto para ler o QRCode de uma novo whatsapp web
* Execute: ```pyhthon3 whats.py```
* Ele abrira uma janela do Chrome com web.whatsapp.com e apresentará o QRCode
* Voce tem 15 segundos para validar
* Sem e observe a magica acontecer...
