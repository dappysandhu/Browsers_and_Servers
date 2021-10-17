# Browsers_and_Servers

mySocket.py

How Browsers and Servers internally works


Line1 = import socket module from python.


Line3 = We created a socket both client socket and server socket which endpoint of connection.

Line4 = s.connect will connect to given domain and port number using the socket we created.

Line5 = We created a string "l" which has the request for server from browser and has the info about the data we want server to search and response back to browser and important it is encoded with UTF-8.

Line7 = s.send is send the UTF-8 string which is sent to server by browser why we used .send() because it protocol that who speak first and who will listen first just like phone call, and heer browser is requesting.

Line9 = W created a little while loop here.

Line10= Wile receiving data from server we put a limit and .recv() will wait until the giveb=n limit or if the data is below that limit it will wait till receiving completes(which is very fast basically and usually we dont wait).

Line11= and we put a condition here that if the data is less tha 1 (character) it will break beacause we dont do that the server will be waiting forever.

Line12= we break the loop.

Line13= If we eveything is fine it will print the data we requested for and before that the data will be decoded into unicode from UTF-8.

Line15= Now connection is closed.

Done!!!
