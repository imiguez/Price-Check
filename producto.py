from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
def demo(): 
    try:
    
        html = urlopen("https://compragamer.com/producto/procesador_intel_core_i3_9100f_4_2ghz_turbo_1151_9th_gen_8492?redir=1&nro_max=50")
    
    except HTTPError as e:
    
        print(e)
    
    except URLError:
    
        print("Server down or incorrect domain")
    
    else:
    
        res = BeautifulSoup(html.read(),"html.parser")
    
        tags = res.findAll("div", {"style": "font-size: 38px"})

        
    
        for tag in tags:
    
            print(tag.getText())

demo()