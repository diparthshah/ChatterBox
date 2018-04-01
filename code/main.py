from Tkinter import *
import socket

addr=""
who=0

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nickname window
nickwindow = Tk()
nickwindow.title("ChatterBox")
nickwindow.maxsize(height=80, width=350)
nickwindow.minsize(height=80, width=350)

nicklabel = Label(nickwindow, text="Enter Your Nickname ")
nicklabel.place(x=10, y=10)
nickentry = Entry(nickwindow)
nickentry.place(x=150, y=10)

def closenick():
    getnick = nickentry.get()
    global nickname
    nickname=getnick
    nickwindow.destroy()

nickbtn = Button(nickwindow, text="OK", command=closenick)
nickbtn.place(x=150,y=40)
nickwindow.mainloop()

# Main chat window
window = Tk()
window.title("ChatterBox")
window.maxsize(height=440, width=450)
window.minsize(height=440, width=450)

iplabel = Label(window, text="Enter Your Friends IP")
iplabel.place(x=10, y=60)

ipentry = Entry(window)
ipentry.place(x=150, y=60)

chatarea = Text(window, height=17, width=60)
chatarea.place(x=10, y=100)
wlcmsg = "Welocme to ChatterBox"+" "+nickname
chatarea.insert(END,wlcmsg)

msglabel = Label(window, text="Enter Message ")
msglabel.place(x=10,y=350)

msgentry = Entry(window, width=53)
msgentry.place(x=10, y=370)

def clientmsg():
    clientmsg = msgentry.get()
    sendmsg = "\n"+nickname+":"+clientmsg
    clientsocket.send(sendmsg)
    chatarea.insert(END,sendmsg)

msgbtn = Button(window, text="Send Message", height=1, width=15, command=clientmsg)
msgbtn.place(x=10,y=400)

def endconn():
    clientsocket.close()
    serversocket.close()

endbtn = Button(window, text="End Chat", height=1, width=15,command=endconn)
endbtn.place(x=290,y=400)

def clientside():
    addr = ipentry.get()
    clientsocket.connect((addr, 5000))
    chatstring = "\nConnecting to address"+addr+"at port 5000"
    chatarea.insert(END,chatstring)

okbtn=Button(window, command=clientside, text="OK", width=11)
okbtn.place(x=320, y=60)

def serverside():
    clientsocket.close()
    who=1
    name = socket.gethostname()
    server_address = socket.gethostbyname(name)
    serversocket.bind((server_address,5000))
    while True:
        # accept connection
        conn, addr = serversocket.accept()
        print "Connected with " + addr[0] + " " + str(addr[1])

    serversocket.close()


serverbtn = Button(window, text="Wait for someone to connect...", width=50, command=serverside)
serverbtn.place(x=10,y=10)

orlabel = Label(window, text="OR")
orlabel.place(x=220,y=40)

window.mainloop()
