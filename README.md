
# ICMP Packet Detection with SMS Notification

This project utilizes Scapy to detect ICMP packets and sends SMS notifications using the Twilio API when certain types of ICMP packets are detected. This can be useful for monitoring network activity and potential scanning attempts.

## Features

- Detects various ICMP packet types:
  - Echo Request (Ping)
  - Echo Reply
  - Time Exceeded
  - Destination Unreachable
- Sends SMS notifications through Twilio for detected packets.

## Prerequisites

- Python 3.x
- Twilio account (to send SMS)
- Scapy library
- python-dotenv library (for loading environment variables)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/icmp-sms-notification.git
   cd icmp-sms-notification
   ```

2. **Install required packages:**

   You can install the required Python packages using pip. It's recommended to use a virtual environment.

   ```bash
   pip install scapy twilio python-dotenv
   ```

3. **Set up Twilio account:**

   - Sign up for a Twilio account if you don't have one.
   - Obtain your Account SID, Auth Token, and Messaging Service SID from the Twilio console.

4. **Create a `.env` file:**

   In the project directory, create a file named `.env` and add your Twilio credentials:

   ```plaintext
   TWILIO_ACCOUNT_SID='your_account_sid'
   TWILIO_AUTH_TOKEN='your_auth_token'
   TWILIO_MESSAGING_SERVICE_SID='your_messaging_service_sid'
   ```

## Usage

1. **Run the script:**

   Execute the Python script to start sniffing for ICMP packets:

   ```bash
   python icmp_sms_notification.py
   ```

2. **Monitoring:**

   The script will listen for ICMP packets and will send SMS notifications based on the detected packet types.

## Important Notes

- Ensure you have the necessary permissions to sniff packets on your network.
- The script is designed to send notifications for a limited number of packets. You can adjust this by changing the `max_packets` variable in the code.
