from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator
from time import sleep
from selenium import webdriver
import os
from pathlib import Path
translator = Translator()

def person1(fn, ln):
    invite1 = fn
    invite2 = ln

    printInvite1 = translator.translate(invite1, dest='hi')
    printInvite2 = translator.translate(invite2, dest='hi')
    name1 = printInvite1.text + ' ' + printInvite2.text+' ,'
    draw.text(xy=(350, 617), text=name1, fill=(218, 37, 28), font=font_type)

def person2(fn, ln):
    invite3 = fn
    invite4 = ln
    printInvite3 = translator.translate(invite3, dest='hi')
    printInvite4 = translator.translate(invite4, dest='hi')
    name2 = printInvite3.text + ' ' + printInvite4.text
    draw.text(xy=(540, 617), text=name2, fill=(218, 37, 28), font=font_type)

def person3(fn,ln):
    invite5 = fn
    invite6 = ln
    printInvite5 = translator.translate(invite5, dest='hi')
    printInvite6 = translator.translate(invite6, dest='hi')
    name3 = printInvite5.text + ' ' + printInvite6.text
    draw.text(xy=(350, 670), text=name3, fill=(218, 37, 28), font=font_type)

image = Image.open('i1.jpeg')
font_type = ImageFont.truetype('Sanskr.ttf', 38, encoding="unic")
#whatsApp name
name = 'bro'

draw = ImageDraw.Draw(image)
#print(name1)
person1('jayesh', 'chaudhary')
person2('mayur', 'chaudhary')
person3('champak', 'chaudhary')


draw.text(xy=(600, 670), text='सह परिवार', fill=(218, 37, 28), font=font_type)
image.show()

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
