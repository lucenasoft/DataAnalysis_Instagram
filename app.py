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
def navegador():
    path = 'config/driver'
    chrome_options = Options()
    for x in range(0,len(argument['argumentos'])):
        chrome_options.add_argument(f'{argument["argumentos"][x]}')
    manager = ChromeDriverManager(path=path)
    driver = webdriver.Chrome(service=Service(manager.install()),chrome_options=chrome_options)
    verific(driver)

#Nesta função ocorre a verificação das contas. 
def verific(driver):
    for x in range(len(usernames)):
        driver.get(f'https://www.instagram.com/{usernames[x]}')
        sleep(3)
        print('=-'*15+'=')
        print(f'Profile: {usernames[x]}')
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[1]/button/div")
            print('Status: OK - 200')
        except:
            print('Status: Error - 404')
        gerar_dados(driver)
            
#Aqui é gerado os dados a serem retornados.
def gerar_dados(driver):
    try:
        print('=-'*15+'=')
        ana_li = driver.find_element(By.CLASS_NAME,'x78zum5.x1q0g3np.xieb3on').text
        print(ana_li)
        print('=-'*15+'=')
        inf_dados = driver.find_element(By.CLASS_NAME,'_aa_c').text
        datas_inf_list = inf_dados.split('\n')
        for x in range(len(datas_inf_list)):
            if x == 0:
                datas_result = f'{datas_inf_list[0]}'
            elif x == 1:
                print(f'Bio: {datas_inf_list[x]}')
            else:
                print(datas_inf_list[x])
        print('=-'*15+'=')
    except:
        print('Sem dados para ler')

navegador()