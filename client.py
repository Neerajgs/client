
import socket
import select
import errno

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    chat = input("Enter Message : ")
    client.send(bytes(chat,"utf-8"))
    
    msg = client.recv(1024).decode()
    print(msg)
    if chat == "file" : 
        """ Opening and reading the file data. """
        filename = input(" Enter the required filename : ")
        file = open(filename, "r")
        data = file.read()

        """ Sending the filename to the server. """
        client.send(filename.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Closing the file. """
        file.close()

        """ Closing the connection from the server. """
        client.close()
    else:
        chat = input("Enter Message : ")
        client.send(bytes(chat,"utf-8"))
        
        msg = client.recv(1024).decode()



if __name__ == "__main__":
    main()
