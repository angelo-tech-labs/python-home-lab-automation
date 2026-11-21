# My first Python network monitoring project
print("Starting Home Lab Network Monitor")   
import socket

server_ip = "10.10.10.10"

print("Checking DNS connectivity to DC01...")

connection = socket.socket()
connection.settimeout(3)

result = connection.connect_ex((server_ip, 53))

if result == 0:
    print("SUCCESS: DC01 DNS TCP port 53 is reachable!")
else:
    print("FAILED: DC01 DNS TCP port 53 is not reachable.")

connection.close()