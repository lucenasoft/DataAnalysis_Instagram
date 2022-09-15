import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

argument = {'argumentos':['--incognito','--disable-blink-features=AutomationControlled','headless','window-size=1920x1080','disable-gpu']}
usernames = list()  #Aqui sera armazenado todos os usúarios para verificar.
local = os.getcwd()
open_txt = open(f'{local}/config/usernames.txt')
read_usernames = open_txt.readlines()
for l in read_usernames:
    usernames.append(l.strip('\n'))

#Aqui é definido as configurações do navegador.
def navegador(a):
    path = 'config/driver'
    chrome_options = Options()
    for x in range(0,len(argument['argumentos'])):
        chrome_options.add_argument(f'{argument["argumentos"][x]}')
    manager = ChromeDriverManager(path=path)
    driver = webdriver.Chrome(service=Service(manager.install()),chrome_options=chrome_options)
    verific(driver)
    gerar_dados(driver)

#Nesta função ocorre a verificação das contas. 
def verific(driver):
    global narnia1
    for x in range(len(usernames)):
        driver.get(f'https://www.instagram.com/{usernames[x]}')
        sleep(3)
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[1]/button/div")
            print('Perfil OK!')
        except:
            print('Perfil inválido')
            

def gerar_dados(driver):
    try:
        inf_dados = driver.find_element(By.CLASS_NAME, '_aa_7').text
        print(inf_dados)
    except:
        print('Sem dados para ler')

navegador(a=1)

""" 
    OBS (NAVEGADOR INVISIVEL, PARA SABER SOMENTE OS STATUS E NÃO O QUE ESTÁ OCORRENDO).

    1º PRECISO IMPLEMENTAR A MODELAGEM DOS DADOS, COMO ARMAZENAR OS USERNAMES COM O STATUS.
    2º CRIAR INTERFACE COM TKINTER PARA RECEBER OS USERNAMES INVES DE SALVAR NO BLOCO DE NOTAS.
    3º CRIAR UM DB PARA RECEBER OS DADOS GERADOS, COMO CONTAS E OS STATUS.

"""
