#!/usr/bin/python3                                                                                                        
import urllib.request

def encurta_url(url):
    urlapi = "http://tinyurl.com/api-create.php?url="
    encurta_url = urllib.request.urlopen(urlapi + url).read()
    return encurta_url.decode("utf-8")
print("------------Encurta URL----------")
url = input("Informa  uma url: ")
print("Original: ",url)
print("Encurtado: ",encurta_url(url))
print("------------Obrigado!------------")
