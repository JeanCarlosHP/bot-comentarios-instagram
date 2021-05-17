from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice


class InstagramBot:

    def __init__(self, nome_usuario, senha):

        self.nome_usuario = nome_usuario
        self.senha = senha

        firefoxPerfil = webdriver.FirefoxProfile()
        firefoxPerfil.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxPerfil.set_preference("dom.webnotifications.enabled", False)

        self.driver = webdriver.Firefox(
            firefox_profile=firefoxPerfil, executable_path='geckodriver.exe'
        )

    def login(self):

        driver = self.driver
        driver.get("https://www.instagram.com")

        sleep(3)

        elemento_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        elemento_usuario.clear()

        for letra in self.nome_usuario:
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

        print("Digitando comentário...")

        for letra in comentario:
            elemento_comentario.send_keys(letra)
            sleep(randint(1, 3))

    def comenta_nas_fotos(self):

        vezes_comentadas = 0
        driver = self.driver

        link_sorteio = "https://www.instagram.com/p/COy5nT_FJyh/"

        while True:

            driver.get(link_sorteio)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            try:

                with open("lista_perfis.txt", "r", encoding='utf-8') as arquivo:
                    perfis = arquivo.read().split()

                driver.find_element_by_class_name("Ypffh").click()
                elemento_entrada_comentario = driver.find_element_by_class_name(
                    "Ypffh")

                sleep(randint(5, 10))

                pessoa_1 = choice(perfis)
                pessoa_2 = choice(perfis)

                marcar_2_pessoas = pessoa_1 + " " + pessoa_2

                print("\nComentando:", marcar_2_pessoas)

                self.escreve_comentario(
                    marcar_2_pessoas, elemento_entrada_comentario)

                sleep(randint(5, 10))

                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()

                vezes_comentadas += 1

                print('Vezes comentadas: ', vezes_comentadas)

                for i in range(1, 3):
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")

                sleep(randint(60, 120))

            except Exception as e:
                print(e)
                sleep(5)


Bot = InstagramBot("perfil/email", "senha")
Bot.login()
