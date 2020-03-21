from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator
from time import sleep
from selenium import webdriver
import os
from pathlib import Path


translator = Translator()
image = Image.open('i1.jpg')
font_type = ImageFont.truetype('Sanskr.ttf', 38, encoding="unic")
#whatsApp name
name = 'bro'
invite1 = 'Mayur'
invite2 = 'chaudhary'

printInvite1 = translator.translate(invite1, dest='hi')
printInvite2 = translator.translate(invite2, dest='hi')
name1 = printInvite1.text+' '+printInvite2.text
#print(name1)

draw = ImageDraw.Draw(image)
draw.text(xy=(250, 420), text=name1, fill=(214, 75, 56), font=font_type)

image2 = Image.open('i2.jpg')
image3 = Image.open('i3.jpg')

im2 = image2.convert('RGB')
im3 = image3.convert('RGB')


imagelist = [im2, im3]

os.chdir('C:\\Users\\mayur Choudhary\\Desktop\\mayur')
os.mkdir(name1)
os.chdir(name1)
path1=Path().absolute()
image.save('file.pdf', save_all=True, append_images=imagelist)
#---------------------------------------------------------------------


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


filepath = 'file.pdf'

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
#user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath('//input[@accept="*"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()
