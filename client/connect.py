import threading
import tkinter as tk
import pdb
import singleton
import netInterface
from singleton import csingleton
from netInterface import CNetInterface
@csingleton
class CUI(CNetInterface):
    def __init__(self):
        self._win = tk.Tk()
        self._win.title("personalChat")
        self._chatShow =  tk.Text(self._win, height = 50, width = 90)
        
    def ShowUi(self):
       # self._chatShow =  tk.Text(self._win, height = 2, width = 90)
        self._chatShow.grid(column= 0, row = 0)
        self._chatSend =  tk.Text(self._win, height = 2, width = 90)
        self._chatSend.grid(column= 0, row = 1)
        buttonSend =  tk.Button(self._win, height = 2, width = 30, command=self.clickSend)
        buttonSend.grid(column= 0, row = 2)
        self._win.mainloop()
    def clickSend(self):
        input = self._chatSend.get("1.0", "end-1c")
        print ("you input: ", input)
        self._chatShow.insert("1.0", "you: " + input + "\n")
#        mySocket.send(input.encode())
        print ("send success")
        input = self._chatSend.delete("1.0", "end-1c")
    def run(self):
        self.ShowUi()
    def ReadFromNetwork(self,  mySocket, abc):
        while(True):
            str2 = mySocket.recv(1024)
            endStr = "\n"
            str2 = "others: " + str(str2) + endStr 
            self._chatShow.insert("1.0", str2)
           # self._chatShow.insert(END, str2)
            print ("I receive from server: ", str2)
    def OnReply(self, packet):
            str2 = packet 
            endStr = "\n"
            str2 = "others: " + str(str2) + endStr 
            self._chatShow.insert("1.0", str2)
            print ("I receive from server: ", str2)
       # CNetInterface.OnReply(packet)

            
        
