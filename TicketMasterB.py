
#   Ig : https://www.instagram.com/franciscovmag/
#   Github: https://github.com/YNK0
#   LinkedIn: https://www.linkedin.com/in/francisco-maga%C3%B1a-a67a02227/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pywhatkit

#Link del evento en TicketMaster
url = "https://www.ticketmaster.com.mx/bad-bunny-world-s-hottest-tour-mexico-11-12-2022/event/14005C3BF9D292C7"

#Whatsapp API
def sen_alert_wsp(num):
    msg = "Tickets disponibles"     #Mensaje deseado
    pywhatkit.sendwhatmsg_instantly(num, msg , 15)

while 1:
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(2)
        #Linea para aceptar cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        #Texto para comparar
        text_confirm = "Precio más bajo"
        text_ldg = "Cargando..."

        text_ldg_nc = "Ola"
        print("Cargando...")

        while 1:
                #Espera mientras carga la pagina comprobando el texto en pantalla
                while text_ldg == text_ldg_nc:
                    text_ldg_nc = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div/div/div[1]/div/div[1]/h2").text
                    time.sleep(1)
                #Con la pagina cargada, compara el texto para checar si existen boletos disponibles
                try:
                    time.sleep(1)
                    text = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div/div/div[2]/div[1]/button[1]").text
                    if text == text_confirm:
                        #Si el texto es el mismo se empiezan a enviar alertas
                        print("Boletos disponibles")
                        print("Iniciando Alerta.....")
                        sen_alert_wsp("+111111111")   #Incluir el numero con la extension del pais
                        print("Alertas enviadas")
                        time.sleep(2)
                        try:
                            #Se trata de seleccionar el boleto disponible
                            print("Tratando de seleccionar boleto")
                            driver.find_element(By.ID, "quickpicks-list").click()
                            time.sleep(1)
                            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div/div[2]/section/div[3]/div/div[2]/div/div[2]/button[2]").click()
                            print("Boleto seleccionado")
                        except:
                            #No se pudo seleccionar el boleto
                            print("Error")
                            print("Boleto no seleccionado")
                            break
                            break
                except:
                    #Actualiza los textos de la pagina
                    driver.refresh()
                    text_ldg_nc = text_ldg
                    time.sleep(2)
    except:
        #Si ocurre un error inesperado, hace reiniciar el ciclo
        print("Ha ocurrido un error")
        print("Reiniciando ")