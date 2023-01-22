from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.laborum.cl/en-region-metropolitana/empleos-publicacion-hoy-busqueda-psicologo.html"

path = (r"C:\Users\Elias\Desktop\Programs\chromedriver.exe")

#Headless mode
options=Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
driver.implicitly_wait(10)

containers = driver.find_elements(by="xpath", value='//div[@class="sc-gyFTku NNeLf sc-cKZAiZ jNQKlq"]')

titulos = []
empresas = []
ubicacions = []
links = []

for container in containers:
    titulo=container.find_element(by="xpath", value='.//h2').text
    empresa=container.find_element(by="xpath", value='.//h3').text
    ubicacion=container.find_element(by="xpath", value='.//h3[@class="sc-gneEKw cQDfVc"]').text
    link=container.find_element(by="xpath", value='.//a').get_attribute("href")

    titulos.append(titulo)
    empresas.append(empresa)
    ubicacions.append(ubicacion)
    links.append(link)

driver.quit()

mi_diccionario = {'titulo': titulos, '\nempresa': empresas, '\nubicacion': ubicacions, '\nlink': links}
mi_df = pd.DataFrame(mi_diccionario)
mi_df.to_csv('Laborum.csv')