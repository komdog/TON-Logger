
from pythonosc.udp_client import SimpleUDPClient

# OSC setup
ip = "127.0.0.1"
port = 9000
osc = SimpleUDPClient(ip, port)

def send_terrors(terror_ids):
    for i in range(3):
        terror_value = float(terror_ids[i]) / 291.0 # Get Float value from terror id
        if i > 0 and terror_value == 0: terror_value = 155.0 / 291.0 # 155 is an empty terror slot
        
        # Send data to OSC
        osc.send_message( f"/avatar/parameters/VF123_r1_slot_{i}" , terror_value )



