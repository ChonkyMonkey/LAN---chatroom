Title: LAN - chatroom

Project Description: 

As the title suggests, this project is a chatroom designed to make communication 
with other members on your network possible. I made this as trivial alternative to 
shouting/ third-party applications when communicating with my siblings. The program 
requires python to be installed on the machine as the whole program is written in 
python. It works by having one computer runs the Server.py file to host the chatroom 
whilst users run the Client.py file. The person hosting the server can also run the 
client file on a seperate python interpreter.

I used the sockets library and threading library to construct this programme.
The socket libary was a necessary libary as it was what allowed me to enable 
communication across my network to begin with. The threading libary allowed me to run 
each client on a seperate thread in order to enable multitasking. I had intially learnt 
about asynchronous functions but upon further reading here
(https://stackoverflow.com/questions/57948910/what-is-the-difference-between-using-pythons-threading-versus-async-await#:~:text=With%20asyncio%2C%20a%20piece%20of,able%20to%20use%20several%20cores.)

and here
(https://stackoverflow.com/questions/34680985/what-is-the-difference-between-asynchronous-programming-and-multithreading)

among other resources, I learnt that threading was more suitable for my task.

In further iterations of this project I may decide to add a gui as currently the 
programme is not visually appealing just sitting in a console. I may also add more 
advanced chatroom features such as admin rights and hard code the user/pass into a env 
file to keep it secret.