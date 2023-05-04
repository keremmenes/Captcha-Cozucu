from cgitb import text
import time
import cv2
import pytesseract
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

driverurl= "C:/Users/kerem/Documents/VSCodeProjects/Sifreleme/CaptchaCozucu/chromedriver.exe"
driver=webdriver.Chrome(executable_path=driverurl)
driver.get("http://ebelediye.antalya.bel.tr/webportal/index.php")
time.sleep(5)
kullaniciAdi= driver.find_element(By.XPATH,'//*[@id="exampleInputPassword1"]')
sifre= driver.find_element(By.XPATH,'/html/body/form/div[5]/div/div/div[1]/div/div[2]/div/input')
kullaniciAdi.send_keys("123456")
sifre.send_keys("tyuıı")

time.sleep(5)

resim =driver.find_element(By.XPATH,'/html/body/form/div[5]/div/div/div[1]/div/div[3]/div/input')

pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"

url="http://ebelediye.antalya.bel.tr/webportal/lib/button.php?guvenlik=1"

urllib.request.urlretrieve(url,"img1.jpg")

#text=pytesseract.image_to_string("img1.jpg")

imge=cv2.imread("img1.jpg")

imge= cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
imge=cv2.medianBlur(imge,5)
text=pytesseract.image_to_string(imge)
print(text)
resim.send_keys(text)

