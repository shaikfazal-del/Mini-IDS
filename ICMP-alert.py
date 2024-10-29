from scapy.all import *
from twilio.rest import Client

# Initialize Twilio client
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Global counter for ICMP packets
icmp_packet_count = 0
max_packets = 2

def send_sms(message_body):
    message = client.messages.create(
        messaging_service_sid='message-id',
        body=message_body,
        to='+9193XXXXXXXX'
    )
    print(f"Message sent with SID: {message.sid}")

def detect_icmp_scans(packet):
    global icmp_packet_count
    if packet.haslayer(ICMP):
        icmp_type = packet[ICMP].type
        source_ip = packet[IP].src
        message_body = ""

        if icmp_type == 8:  # Echo Request (Ping)
            message_body = f"ICMP Echo Request (Ping) detected from {source_ip}. This may be part of an Nmap ping scan."
        elif icmp_type == 0:  # Echo Reply
            message_body = f"ICMP Echo Reply detected from {source_ip}."
        elif icmp_type == 11:  # Time Exceeded
            message_body = f"ICMP Time Exceeded detected from {source_ip}. Could be from a traceroute."
        elif icmp_type == 3:  # Destination Unreachable
            message_body = f"ICMP Destination Unreachable detected from {source_ip}. This might occur during a port scan."

        if message_body:
            print(message_body)
            send_sms(message_body)
            icmp_packet_count += 1

        if icmp_packet_count >= max_packets:
            return True

# Start sniffing ICMP packets, stop after the maximum number of packets
sniff(filter="icmp", prn=detect_icmp_scans, stop_filter=lambda x: icmp_packet_count >= max_packets)
