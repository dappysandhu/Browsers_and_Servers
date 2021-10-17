import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org', 80))
l='GET http://data.pr4e.org/page1/htm HTTP/1.0 \n'.encode()
s.send(l)

While True:
    data=s.recv(500)
    if len(data)<1:
        break
    print(data.decode())
s.close()
