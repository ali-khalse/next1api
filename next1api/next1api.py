# pip install beautifulsoup4
from bs4 import BeautifulSoup
from requests import get,post
class Music:
    def __init__(self,*arg):  
        pass
    def download(self,url):
        content = get(url).text
        soup = BeautifulSoup(content, "html.parser")
        data = {}
        music = []
        for a in soup.findAll('div',href=False, attrs={'class':'details'}):
            music.append({"k":(a.find('div',href=False, attrs={'class':'name'}).text).replace("پخش آنلاین آهنگ با کیفیت ",""),
             "u":a.find('i',href=False, attrs={'class':'play'}).get('audiourl')
             })
        data["music"]= music
        for a in soup.findAll('div',href=False, attrs={'class':'pstop f12'}):
            data["date"] = a.text.split("|")[0].replace(a.find('a').text,"")
            data["name"] = a.find('a').text           
        for a in soup.findAll('div',href=False, attrs={'class':'center'}):
            data["M_name"] = (a.find('h2').text)
            
        for a in soup.findAll('img',src=True,attrs={'width':'480','height':'480'}):
            data["tumbnial"] = a.get('src')

        return data     

    def search(self,sear):
        content = get("https://nex1music.ir/?s="+str(sear),verify = True).text
        soup = BeautifulSoup(content, "html.parser")
        data = []
        for a in soup.findAll('div', attrs={'class':'ps anm'}):
            nim_d = {}
            f = a.find('a',href=True)
            nim_d["name"] = f.text
            nim_d["url"] = f.get('href')
            data.append(nim_d)
            
        return data     
#C = Music()
#url = C.search("راه")[0]['url']
#print(C.download(url))
