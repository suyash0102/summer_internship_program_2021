# Creating a socket
import socket as s
import cv2
import struct
import pickle

server_s = s.socket(s.AF_INET,s.SOCK_STREAM)
host_name  = s.gethostname()
host_ip = s.gethostbyname(host_name)
print('HOST IP:',host_ip)

port = 1
s_address = (host_ip,port)
print("Socket Created Successfully")

server_s.bind(s_address)
print("Socket Bind Successfully")

server_s.listen(5)
print("LISTENING AT:",s_address)

print("Socket Accepted")

# Streaming the captured video
while True:
    client_s, addr = server_s.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_s:
        vid = cv2.VideoCapture(0)

        while (vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_s.sendall(message)
            print(a)

            cv2.imshow('Server', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_s.close()

print("Created By TEAM Summer_04_16")