import requests
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
DRIVER_PATH = 'C:\path\chromedriver'
url = "https://www.instagram.com/alceil/"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}
respone=requests.get(url,headers=header)
soup = BeautifulSoup(respone.text,'html.parser')
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
soup = BeautifulSoup(driver.page_source,'html.parser')
links = []
for i in soup.find_all('a',href = True):
    if i['href'].startswith('/p'):
        print("Link found https://www.instagram.com/{0}".format(i['href']))
        links.append("https://www.instagram.com/" +i['href'])


for i,j in enumerate(links):
    driver_i = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver_i.get(j)
    soup_i= BeautifulSoup(driver_i.page_source,'html.parser')
    image_link = soup_i.find_all('div',{'class':'eLAPa kPFhm'})
    print(image_link)
    # download_image(image_link)
    driver_i.quit()        



def download_image(url,destination = 'C:/Users/ashis/Desktop/pythonprojects/instsave'):
    resource = urllib.request.urlopen(url)
    filename = destination + "kindi" + ".jpg"
    output = open(filename,"wb")
    output.write(resource.read())
    output.close



