# Browsers in python

"mySocket.py"

How Browsers and Servers internally works

import socket module from python.

First of all, we created a socket both client socket and server socket which is the endpoint of the connection. Then we used s.connect which connects the socket to a given domain and port number (by the socket we created). When it's done we made a string "l" which has the request for the server from the browser and has the info about the data, we want the server to search and respond to the browser and important it is encoded with UTF-8. So now we have to send this string to the server and that is done by (s.send), it sends the UTF-8 string to the server, why we used .send() because it is a protocol that who speak first and who will listen first (just like a phone call), and here browser is requesting(speaking first). After this was done we gave some conditions to the response from the server and for that, we created a little while loop here. so what it doing is while receiving data from the server we put a limit and .recv() will wait until the given limit or if the data is below that limit will complete, it will wait till data receiving completes(which is very fast basically and usually we don't wait). And we put a condition here that if the data is less than 1 (character) it will break because we don't want the server to be waiting forever, and we break the loop. If everything is fine it will print the data we requested and before that the data will get decoded into Unicode from UTF-8. It will have the date-time content type (XML, JSON, HTML Etc), content length, server details, connection details and, the document or data we requested. At last, the connection is closed.

Done!!!  
