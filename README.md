# Browsers in python

"mySocket.py"

How Browsers and Servers internally works


import socket module from python.

First of all we created a socket both client socket and server socket which is endpoint of connection, Then we used s.connect which connects the socket to given domain and port number (by the socket we created). Ween it's done we made a string "l" which has the request for the server from the browser and has the info about the data, we want the server to search and response back to browser and important it is encoded with UTF-8. So now we have to send this string to the server and that is done by s.send it sends the UTF-8 string to the server, why we used .send() because it is protocol that who speak first and who will listen first (just like a phone call), and here browser is requesting(speaking first). After this done we gave some condition to the response from server and for that we created a little while loop here. so what it doing is while receiving data from the server we put a limit and .recv() will wait until the given limit or if the data is below that limit will completes, it will wait till data receiving completes(which is very fast basically and usually we dont wait). And we put a condition here that if the data is less than 1 (character) it will break beacause we don't want the server to be waiting forever, and we break the loop. If eveything is fine it will print the data we requested for and before that the data will be decoded into unicode from UTF-8.
It will have date time content-type(xml, json, html, etc), content-lenght, server details, connection details and then the documnet or data we requested for.
At last the connection is closed.

Done!!!
