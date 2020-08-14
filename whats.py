from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que voce quer enviar, aqui usamos um Quick Reply chamado /m2
        self.mensagem = "/m2"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        # O arquivo deve conter um nome (a ser buscado) por linha
        self.grupos_ou_pessoas = open("contatos").read().splitlines()
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
        executable_path=r'./chromedriver', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            # Buscar contato 
            search = self.driver.find_element_by_xpath("(//div[@contenteditable='true'])")
            search.click()
            #Limpa campo de busca
            search.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
            # Escrever na busca 
            search.send_keys(grupo_ou_pessoa)
            time.sleep(1)
            try:
	        # Seleciona o Nome e clica
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
                time.sleep(1)
                campo_grupo.click()

                #Busca a caixa de msg, escreve msg e envia #_3FRCZ copyable-text selectable-text
                chat_box = self.driver.find_element_by_xpath("(//div[@contenteditable='true'])[2]")
                time.sleep(1)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                chat_box.send_keys(Keys.ENTER)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(1)
                botao_enviar.click()
                time.sleep(2)
            except:
                print(f"Falha:{grupo_ou_pessoa}")
                time.sleep(2)
              

bot = WhatsappBot()
bot.EnviarMensagens()
