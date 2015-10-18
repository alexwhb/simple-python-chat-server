# simple-python-chat-server
A very simple Python chat server. 

At this point there is no client code, but the server is still usable without one. Assuming you're on a mac, all you have to do is run `python path to server.py` that will start the server. Then, once the server is running, enter: `telnet loclhost 5000` in the commandline. that will connect you up to the server. or if you are doing it from multiple computers, as long as you are on the same network you just have to replace localhost with the computer's IP address that you are running the server from. 


I wrote this, server to get a better undersanding of socket programming. Most of the code is from [here](http://www.binarytides.com/code-chat-application-server-client-sockets-python/). I made it a bit more functinal and a bit more structured. 
