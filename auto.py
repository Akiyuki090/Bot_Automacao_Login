import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)

navegador.get('https://webmail.umbler.com')
time.sleep(3)
navegador.find_element('xpath', '//*[@id="Email"]').send_keys('email')
time.sleep(3)
navegador.find_element('xpath', '//*[@id="Password"]').send_keys('senha')
time.sleep(3)
navegador.find_element('xpath', '//*[@id="btnLogin"]').click()
time.sleep(3)
