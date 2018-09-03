import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import *


root = Tk()
root.geometry("600x800+400+0")
global i0


def getDetails(first,last):
    global i0
    first = first.lower()
    last = last.lower()
    url = 'http://www.nba.com/players/' + first + '/' + last
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    hnw = soup.select('#player-tabs-Info section section section section')
    det = soup.select('#player-tabs-Info section section section ul li')
    for i in range(5):
        det[i] = det[i].getText().split("\n")
    det[5] = det[5].getText().split("PREVIOUSLY")
    for i in range(5):
        det[i].pop()
    for i in range(5):
        det[i][1] = det[i][1].lstrip()
    for i in range(2):
        hnw[i] = hnw[i].getText().split("\n")
        hnw[i].pop(0)
    hnwf = []
    hnwf.append(hnw[0])
    hnwf.append(hnw[1])
    for i in range(2):
        hnwf[i][0] = hnwf[i][0].lstrip()
        hnwf[i][1] = hnwf[i][1].lstrip()
        hnwf[i][2] = hnwf[i][2].lstrip()
    details = {}
    name = first.capitalize() + ' ' + last.capitalize()
    details[name] = {hnwf[0][0]:hnwf[0][1]+hnwf[0][2],hnwf[1][0]:hnwf[1][1]+hnwf[1][2],det[0][0]:det[0][1],det[1][0]:det[1][1],det[2][0]:det[2][1],det[3][0]:det[3][1],det[4][0]:det[4][1],'PREVIOUSLY':det[5][1]}
    print(details[name])
    lisk = []
    lisv = []
    for key in details[name].keys():
        lisk.append(key)
    for value in details[name].values():
        lisv.append(value)
    sp = ''
    for i in range(8):
        sp = sp + lisk[i] + '====>>'
        sp = sp + lisv[i] + '\n'

    try:
        c0.delete(i0)
        i0 = c0.create_text(280,230,text=sp,font=("Arial",20))
    except:
        i0 = c0.create_text(280,230,text=sp,font=("Arial",20))


def clearall():
    entry1.delete(0,END)
    entry2.delete(0,END)



def details():
    first = entry1.get()
    last = entry2.get()
    getDetails(first,last)

c3=Canvas(root,width=500,height=100,bg="yellow")
c3.pack()
textw = "Please give correct names\n    of basket ball players"
c3.create_text(250,50,text=textw,font=("Arial",20))
label1 = Label(root,text = 'Enter First Name')
label1.pack()
#label1.place(x=100,y=250)
entry1 = Entry(root,width = 20)
#entry1.place(x=100,y=300)
entry1.pack()
label2 = Label(root,text = 'Enter Last Name')
#label2.place(x=300,y=250)
label2.pack()
entry2 = Entry(root,width = 20)
#entry2.place(x=300,y=300)
entry2.pack()
submit = Button(root,text = 'DETAILS', command = details)
#submit.place(x=290,y=350)
submit.pack()
c0=Canvas(root,width=550,height=450,bg="yellow")
c0.pack()
textw = ""
i0 = c0.create_text(250,50,text=textw,font=("Arial",20))

clear = Button(root,text = 'CLEAR', command = clearall)
clear.pack()
