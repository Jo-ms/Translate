import os 
import sys
import urllib.request
import requests
from gtts import gTTS
from tkinter import*
from tkinter import filedialog
import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract 
  
root = Tk()
root.title("번역기")
root.geometry("800x600+150+150")
root.resizable(False, False)

client_id = "MOCJE8H1THkxUzp4_Ice"
client_secret = "QESJXRcGNX"
url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {"X-Naver-Client-Id" :client_id, "X-Naver-Client-Secret":client_secret}

pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
file = filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("png files","*.png"),("all files","*.*")))

encText = pytesseract.image_to_string(Image.open(file))
test = encText.replace('\n', ' ')

def ko_translate():

    params = (("source", "en"),("target", "ko"),("text", test))
    response = requests.post(url, data=params, headers=headers)
    tts = gTTS(text=test, lang='ko')
    tts.save("Korea.wav")
    if response.status_code == 200:
        response_body = response.json()
        text = response_body[u'message'][u'result'][u'translatedText']
        scrt=tkst.ScrolledText(root, width = 100, height = 3)
        scrt.place(x = 50, y = 350)
        
        scrt.insert(INSERT, text)
        scrt.insert(END, "\n")
        
        print(scrt.get(INSERT, END))
        


def ja_translate():
    params = (("source", "en"),("target", "ja"),("text", test))
    response = requests.post(url, data=params, headers=headers)
    tts = gTTS(text=test, lang='ja')
    tts.save("Japan.mp3")
    if response.status_code == 200:
        response_body = response.json()
        text = response_body[u'message'][u'result'][u'translatedText']
        scrt=tkst.ScrolledText(root, width = 100, height = 3)
        scrt.place(x = 50, y = 350)
        
        scrt.insert(INSERT, text)
        scrt.insert(END, "\n")
        
        print(scrt.get(INSERT, END))

def fr_translate():
    params = (("source", "en"),("target", "fr"),("text", test)) 
    response = requests.post(url, data=params, headers=headers)
    tts = gTTS(text=test, lang='fr')
    tts.save("France.mp3")
    if response.status_code == 200:
        response_body = response.json()
        text = response_body[u'message'][u'result'][u'translatedText']
        scrt=tkst.ScrolledText(root, width = 100, height = 3)
        scrt.place(x = 50, y = 350)
        
        scrt.insert(INSERT, text)
        scrt.insert(END, "\n")
        
        print(scrt.get(INSERT, END))

def ch_translate():
    params = (("source", "en"),("target", "zh-CN"), ("text", test))
    response = requests.post(url, data=params, headers=headers)
    tts = gTTS(text=test, lang='zh-CN')
    tts.save("China.mp3")
    if response.status_code == 200:
        response_body = response.json()
        text = response_body[u'message'][u'result'][u'translatedText']
        scrt=tkst.ScrolledText(root, width = 100, height = 3)
        scrt.place(x = 50, y = 350)
        
        scrt.insert(INSERT, text)
        scrt.insert(END, "\n")
        
        print(scrt.get(INSERT, END))

translator = Label(root, text="번역기")
newImg = ImageTk.PhotoImage(Image.open(file))
translator.configure(image=newImg)
translator.place(x = 200, y = 50)

button_ko = Button(root, text="한국어로 번역하기", command=ko_translate)
button_ko.place(x = 50, y = 50, width=130, height=40)

button_ja = Button(root, text="일본어로 번역하기", command=ja_translate)
button_ja.place(x = 50, y = 100, width=130, height=40)

button_fr = Button(root, text="불어로 번역하기", command=fr_translate)
button_fr.place(x = 50, y = 150, width=130, height=40)

button_ch = Button(root, text="중국어로 번역하기", command=ch_translate)
button_ch.place(x = 50, y = 200, width=130, height=40)

root.mainloop()