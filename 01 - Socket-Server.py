#this is a socket server program using TCP protocol
# why TCP and not UDP
#--Packets dropped in the network are detected and retransmitted by the sender.
#--Data is read by your application in the order it was written by the sender.


# run this program at different terminal

from datetime import datetime
import socket
import time     
#using socket library to create P2P network program

HostAddr = "127.0.0.1"
Port = 50000

sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#object is created based on AFI and protocol is TCP using Sock_Stream

sockObj.bind((HostAddr,Port))   #socket is fixed to "127.0.0.1:50000"
sockObj.listen()                #Waiting for client to be connected to server

with open('ServerSide.txt','a') as openedFile:

    print("Waiting for client to be connected...")
    openedFile.write("Waiting for client to be connected...")
    openedFile.write("\n") 
    conn, addr = sockObj.accept()   # saving connection and address of client 

    with conn:                                  #exception handling
        print(f"Client Connected by {addr}")
        openedFile.write(f"Client Connected by {addr}")
        openedFile.write("\n") 

        for i in range(5):
            
            time.sleep(2)                       #pausing system for getting response from the client   
            
            response = conn.recv(4096)          
            if not response:                    #run till conn drop
                break
            print("Client Says: " + response.decode())

            openedFile.write("Client Says: " + response.decode() + "-- ")
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
            openedFile.write(timestampStr)
            openedFile.write("\n")                    

            conn.sendall(b'this is sent by server')     #Sending message  

            openedFile.write("Server Says: this message is sent by Server -- ")
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
            openedFile.write(timestampStr)
            openedFile.write("\n")        
        
        conn.close()
        print("Connection closed")
        openedFile.write("Connection closed")

        openedFile.write("\n")
        openedFile.write("\n")
   