# Importar a biblioteca correspondente
import pyautogui as pa


import time


pa.PAUSE = 0.5


# Abrir a janela window
pa.press("win")
# Digitar chrome para localizar navegador
pa.write("chrome")
pa.press("enter")
time.sleep(5)
# Clicar na guia de e-mail correspondente 
pa.click(x=1652, y=149)
pa.press("enter")

time.sleep(5)

for i in range(50):
    # clicar para excluir e-mails
    pa.click(x=437, y=336)
    pa.click(x=640, y=234)

    


























