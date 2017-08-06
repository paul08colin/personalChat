import singleton
import socket
import threading
import netInterface
@singleton.csingleton    
class CNetWork:
    def __init__(self):
        self._index = 0
        self._packIndexMap = {}
    def Run(self):
        self._mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._mySocket.connect(("192.168.0.109", 9999))
        t2 = threading.Thread(target = (self.ReadFromNetwork), args = (self._mySocket, 1))
        t2.start()
    def ReadFromNetwork(self,  mySocket, abc):
        while(True):
            str2 = self._mySocket.recv(1024)
            endStr = "\n"
            str2 = "others: " + str(str2) + endStr 
           # self._chatShow.insert("1.0", str2)
           # self._chatShow.insert(END, str2)
            print ("I receive from server: ", str2)
            if (1 in self._packIndexMap):
                self._packIndexMap[1].OnReply()
    def Send(self, curNetInterface, packet):
        self._mySocket.send(input.encode())
        self._index = self._index + 1
        self._packIndexMap[self._index] = curNetInterface
        

        

