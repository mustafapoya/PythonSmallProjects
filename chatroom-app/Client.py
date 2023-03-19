import tkinter
import socket
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("UTF8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("There is an Error Receiving the Message")


def send():
    msg = my_msg.get()
    my_msg.set("")

    sock.send(bytes(msg, "UTF8"))
    if msg == "#quite":
        sock.close()
        window.close()


def on_closing():
    my_msg.set("#quite")
    send()


window = Tk()
window.title("Chat Room Application")
window.configure(bg="green")

message_frame = Frame(window, height=100, width=100, bg="red")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="red", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg="blue", font="arial", bg="red")
label.pack()

entry_field = Entry(window, textvariable=my_msg, fg="red", width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Arial", fg="white", command=send)
send_button.pack()

quite_button = Button(window, text="Quite", font="arial", fg="white", command=on_closing)
quite_button.pack()


Host = "127.0.0.1"
Port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((Host, Port))

receive_thread = Thread(target=receive)
receive_thread.start()


mainloop()

