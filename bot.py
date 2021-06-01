from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice


class InstagramBot:

    def __init__(self):
        self._link = ''
        self._nome_usuario = ''
        self._senha = ''
        self._quantidade_perfis = 0
        self._comentar_cada_minuto = 0
        self._comentario = ''
        self._vezes_comentadas = 0

    def abrir_navegador(self):
        firefoxPerfil = webdriver.FirefoxProfile()
        firefoxPerfil.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxPerfil.set_preference("dom.webnotifications.enabled", False)

        self.driver = webdriver.Firefox(
            firefox_profile=firefoxPerfil, executable_path='geckodriver.exe'
        )

    def login(self):
        self.abrir_navegador()
        driver = self.driver
        driver.get("https://www.instagram.com")

        sleep(5)

        elemento_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        elemento_usuario.clear()

        for letra in self.usuario:
            elemento_usuario.send_keys(letra)
            sleep(randint(1, 2))

        elemento_senha = driver.find_element_by_xpath(
            "//input[@name='password']")
        elemento_senha.clear()

        for letra in self.senha:
            elemento_senha.send_keys(letra)
            sleep(randint(1, 2))

        elemento_senha.send_keys(Keys.RETURN)

        sleep(5)

        self.comenta_nas_fotos()

    @staticmethod
    def escreve_comentario(comentario, elemento_comentario):

        for letra in comentario:
            elemento_comentario.send_keys(letra)
            sleep(randint(1, 3))

    def comenta_nas_fotos(self):

        vezes_comentadas = 0
        driver = self.driver

        link_sorteio = self.link

        while True:

            driver.get(link_sorteio)
            # driver.execute_script(
            #     "window.scrollTo(0, document.body.scrollHeight);")

            try:

                with open("lista_perfis.txt", "r", encoding='utf-8') as arquivo:
                    perfis = arquivo.read().split()

                driver.find_element_by_class_name("Ypffh").click()
                elemento_entrada_comentario = driver.find_element_by_class_name(
                    "Ypffh")

                sleep(randint(5, 10))
                
                for i in range(self.quantidade_perfis):
                    if i == 0:
                        comentario = choice(perfis) + ' '
                    else:
                        comentario += choice(perfis) + ' '

                self.comentario = comentario

                self.escreve_comentario(
                    comentario, elemento_entrada_comentario)

                sleep(randint(5, 10))

                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()

                vezes_comentadas += 1
                self.vezes_comentadas = vezes_comentadas

                for i in range(1, 3):
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")

                sleep(self.comentar_cada_minuto0)

            except Exception as e:
                print(e)
                sleep(5)

    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, usuario):
        self._nome_usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def quantidade_perfis(self):
        return self._quantidade_perfis

    @quantidade_perfis.setter
    def quantidade_perfis(self, quantidade):
        self._quantidade_perfis = quantidade

    @property
    def comentar_cada_minuto(self):
        return self._comentar_cada_minuto

    @comentar_cada_minuto.setter
    def comentar_cada_minuto(self, minutos):
        self._comentar_cada_minuto = minutos * 60

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario

    @property
    def vezes_comentadas(self):
        return self._vezes_comentadas

    @vezes_comentadas.setter
    def vezes_comentadas(self, vezes):
        self._vezes_comentadas = vezes


if __name__ == '__main__':
    bot = InstagramBot('jeann.carlosh', 'jctel47@',
                       'https://www.instagram.com/p/CPdxVNtha3h/')
    bot.login()
