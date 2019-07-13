import requests
from bs4 import BeautifulSoup
def main_spider(url):
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text, "html.parser")
    fw=open('link.txt','w')
    for link in soup.find_all('a'):
        hre=link.get("href")
        fw.write(hre+"\n")
        print(hre)

     #   ip=str(hre)
    #lines = ip.split("\\n")
    
    fw.close()
    
main_spider(url='http://'+str(input('enter url: \n')))
