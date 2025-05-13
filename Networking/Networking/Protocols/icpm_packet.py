import scapy.all as scapy  # Imports the Scapy library

def create_icmp_packet(source_ip, destination_ip):
    """
    Creates an ICMP echo request packet encapsulated within an IP packet.

    Args:
        source_ip (str): The IP address of the machine sending the packet.
        destination_ip (str): The IP address of the destination host.

    Returns:
        scapy.Packet: A Scapy packet object containing the IP and ICMP layers.
    """
    ip_packet = scapy.IP(dst=destination_ip, src=source_ip)
    icmp_packet = scapy.ICMP()
    complete_packet = ip_packet / icmp_packet
    return complete_packet

def send_packet(packet, interface):
    """
    Sends a Scapy packet and attempts to receive a single response on a specific interface.

    Args:
        packet (scapy.Packet): The Scapy packet object to send.
        interface (str): The name of the network interface to use for sending.
    """
    response = scapy.sr1(packet, timeout=2, verbose=False, iface=interface)
    if response is not None:
        response.show()
    else:
        print("No response received.")

if __name__ == "__main__":
    target_ip = "192.168.0.1"  # Replace with the IP address you want to ping. This IP address is typically the  network router.
    source_ip = "192.168.0.2" # Replace with your machine's IP address
    network_interface = "your_network_interface"  # Replace with your actual network interface name (e.g., "en0", "wlan0")

    icmp_packet = create_icmp_packet(source_ip, target_ip)
    send_packet(icmp_packet, network_interface)