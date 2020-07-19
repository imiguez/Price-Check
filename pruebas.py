from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup

import smtplib

def checkeoDePrecio():
    try:

        html = urlopen("https://compragamer.com/producto/procesador_intel_core_i3_9100f_4_2ghz_turbo_1151_9th_gen_8492?redir=1&nro_max=50")
 
    except HTTPError as e:
 
        print(e)
 
    except URLError:
 
        print("Server down or incorrect domain")
 
    else:
 
        res = BeautifulSoup(html.read(),"html.parser")

        tags = res.findAll("div", {"style": "font-size: 38px"})
 
        precio = res.find("div", {"class": "precioEspecial col-sm-3 col-xs-5"})

        a = precio.getText().strip()[1:6]
    #CAMBIO DE STR A INT
        b = a.replace("," , "")
        b = int(b)
        if b<6300:
            sendMail()

        print(b)
        for tag in tags:
            print(tag.getText())



def sendMail():
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nano2001miguez@gmail.com', '1234567890a49831799')
    subject = 'El precio bajo!'
    body = 'Checkea este link https://compragamer.com/producto/procesador_intel_core_i3_9100f_4_2ghz_turbo_1151_9th_gen_8492?redir=1&nro_max=50'
    msg = f'{subject}\n\n{body}'

    server.sendmail(
        'nano2001miguez@gmail.com',
        'zaseznano@gmail.com',
        msg
    )
    print('Se ha enviado el MAIL!')



checkeoDePrecio()