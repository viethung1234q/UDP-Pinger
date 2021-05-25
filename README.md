# UDP-Pinger

# Đoàn Việt Hưng - hungdoan2712@gmail.com

# PACKET LOSS

UDP provides applications with an unreliable transport service. Messages may get lost in the network
due to router queue overflows, faulty hardware or some other reasons. Because packet loss is rare or
even non-existent in typical campus networks, the server in this lab injects artificial loss to simulate
the effects of network packet loss. The server creates a variable randomized integer which determines
whether a particular incoming packet is lost or not.

# CLIENT CODE

You need to implement the following client program.
The client should send 10 pings to the server. Because UDP is an unreliable protocol, a packet sent
from the client to the server may be lost in the network, or vice versa. For this reason, the client
cannot wait indefinitely for a reply to a ping message. You should get the client wait up to one second
for a reply; if no reply is received within one second, your client program should assume that the
packet was lost during transmission across the network. You will need to look up the Python
documentation to find out how to set the timeout value on a datagram socket.

Specifically, your client program should:

(1) send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection
first, since UDP is a connectionless protocol.)

(2) print the response message from server, if any

(3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responses

(4) otherwise, print “Request timed out”

During development, you should run the UDPPingerServer.py on your machine, and test your
client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged your code, you
should see how your application communicates across the network with the ping server and ping
client running on different machines.

# MESSAGE FORMAT

The ping messages in this lab are formatted in a simple way. The client message is one line,
consisting of ASCII characters in the following format:

              Ping sequence_number time

where sequence_number starts at 1 and progresses to 10 for each successive ping message sent by the
client, and time is the time when the client sends the message.
