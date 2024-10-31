
from pythonosc.udp_client import SimpleUDPClient

# OSC setup
ip = "127.0.0.1"
port = 9000
osc = SimpleUDPClient(ip, port)

def send_terrors(terror_ids):
    # print("Sending TO OSC...")
    osc.send_message( "/avatar/parameters/VF126_r1_slot_0" , int(terror_ids[0]) )
    osc.send_message( "/avatar/parameters/VF126_r1_slot_1" , int(terror_ids[1]) )
    osc.send_message( "/avatar/parameters/VF126_r1_slot_2" , int(terror_ids[2]) )



