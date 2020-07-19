import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://compragamer.com/producto/procesador_intel_core_i3_9100f_4_2ghz_turbo_1151_9th_gen_bundle_f_juegos_y_soft_8492?redir=1&nro_max=50'
headers = {"User-Agente": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    precio = soup.find("div", {"class": "precioEspecial col-sm-3 col-xs-5"})
    tags = soup.find("div", {"style": "font-size: 38px"}).getText().strip()

    a = precio.getText().strip()[1:6]
    #CAMBIO DE STR A INT
    b = a.replace("," , "")
    b = int(b)
    if b < 6400:
        send_mail()

    print(b)
    print(tags)

def send_mail():
    server = smtplib.SMTP('smpt.')
