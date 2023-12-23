import requests
import time
import threading
from itertools import cycle
from colorama import init, Fore, Back, Style
from faker import Faker

init()
print(Fore.BLUE, Style.BRIGHT, Back.BLACK + """

    __        _       ___  __   _  __  ___ ___      
   (_ ` )\/) / ) )_/  )_  (_ ` / ` )_) )_  )_  )\ ) 
- .__) (  ( (_/ /  ) (__ .__) (_. / \ (__ (__ (  (  - 
                                                  
  """)
print(Fore.WHITE)

targ = input("URL: ")
time.sleep(1)
print("\n[NOTE]: It may take some time to set up proxy connections ... ")


def make_request(proxy_url):
    fake = Faker()
    headers = {'User-Agent': fake.user_agent()}

    proxy_url = "http://" + proxy_url
    list_proxy = [proxy_url]
    proxy_cycle = cycle(list_proxy)

    for i in range(1):
        proxy = next(proxy_cycle)
        proxies = {"http": proxy, "https": proxy}
        try:
            r = requests.get(url=targ, proxies=proxies, headers=headers).text
            print(" ", proxy, " ===> [REQUESTED]")
        except Exception as E:
            pass


def smoke():
    time.sleep(25)
    print("\n[NOTE] Now smokescreening: ", targ)


smoke_thread = threading.Thread(target=smoke)
smoke_thread.start()

proxy_urls = [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
    'https://raw.githubusercontent.com/rx443/proxy-list/main/online/all.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt'
]

threads = []

for proxy_url in proxy_urls:
    try:
        thread = threading.Thread(target=make_request, args=(proxy_url,))
        threads.append(thread)
        thread.start()
    except Exception as E:
        pass

for thread in threads:
    thread.join()




