# Browsers in python

"mySocket.py"

How Browsers and Servers internally works


import socket module from python.

First of all we created a socket both client socket and server socket which endpoint of connection, Then we used s.connect connect to given domain and port number using the socket we created. WHen it's done we created a string "l" which has the request for server from browser and has the info about the data we want server to search and response back to browser and important it is encoded with UTF-8. So now we have to send this string to server and that is done by s.send sends the UTF-8 string to server by browser, why we used .send() because it protocol that who speak first and who will listen first just like phone call, and here browser is requesting. After this done we gave some condition to the response from server and for that we created a little while loop here. so what it did is Wile receiving data from server we put a limit and .recv() will wait until the giveb=n limit or if the data is below that limit it will wait till receiving completes(which is very fast basically and usually we dont wait). And we put a condition here that if the data is less tha 1 (character) it will break beacause we don't want the server to be waiting forever. and we break the loop. If eveything is fine it will print the data we requested for and before that the data will be decoded into unicode from UTF-8.
At last the connection is closed.

Done!!!
