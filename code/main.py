from Tkinter import *
import socket

addr = ""
nickname = ""
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

window = Tk()
window.title("ChatterBox")
window.maxsize(height=400, width=400)
window.minsize(height=400, width=400)

nicklabel = Label( window, text="Enter Your Nickname ")
nicklabel.place(x=10, y=10)

nickentry = Entry(window)
nickentry.place(x=150, y=10)

iplabel = Label(window, text="Enter Your Friends IP")
iplabel.place(x=10, y=40)

ipentry = Entry(window)
ipentry.place(x=150, y=40)

chatarea = Text(window, height=15, width=50)
chatarea.place(x=20, y=105)
chatarea.insert(END,"Welcome to ChatterBox")

msgentry = Entry(window, width=44)
msgentry.place(x=20, y=330)

def clientmsg():
    clientmsg = msgentry.get()
    sendmsg = "\n"+nickname+":"+clientmsg
    clientsocket.send(sendmsg)
    chatarea.insert(END,sendmsg)

msgbtn = Button(window, text="Send Message", height=1, width=15, command=clientmsg)
msgbtn.place(x=20,y=360)

def endconn():
    clientsocket.close()

endbtn = Button(window, text="End Chat", height=1, width=15,command=endconn)
endbtn.place(x=230,y=360)

def clientside():
    addr = ipentry.get()
    nickname = nickentry.get()
    clientsocket.connect((addr, 5000))
    chatstring = "\nConnecting to address"+addr+"at port 5000"
    chatarea.insert(END,chatstring)

okbtn=Button(window, command=clientside, text="OK", width=10)
okbtn.place(x=180, y=70)

window.mainloop()