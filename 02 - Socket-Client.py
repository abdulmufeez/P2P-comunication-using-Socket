#this is a socket server program using TCP protocol

#run this at different terminal

from datetime import datetime
import socket
import time

HostAddr = "127.0.0.1"      # The server's hostname or IP address
Port = 50000                # The port used by the server

sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open('ClientSide.txt','a') as openedFile:

        #connect to server
        sockObj.connect((HostAddr, Port))

        for i in range(5):
                #sending message
                sockObj.sendall(b'this message is sent by client')
                
                openedFile.write("Client Says: this message is sent by client -- ")
                dateTimeObj = datetime.now()
                timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                openedFile.write(timestampStr)
                openedFile.write("\n")


                #waiting to get response from server
                time.sleep(2)    

                #recieving response
                response = sockObj.recv(4096)
                if not response:                   
                        break
                print("Server Says: " + response.decode())  

                openedFile.write("Server Says: " + response.decode() + "-- ")
                dateTimeObj = datetime.now()
                timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                openedFile.write(timestampStr)
                openedFile.write("\n")     

        sockObj.close()
        print("Connection closed")
        openedFile.write("Connection closed")

        openedFile.write("\n")
        openedFile.write("\n")