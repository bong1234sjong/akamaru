

https://realpython.com/python-logging/
https://dev.to/yo-shi/exploring-the-world-of-packets-with-scapy-a-beginners-hands-on-journey-to-understanding-1d0g
https://pwnable.kr/play.php
https://gitlab.cylab.be/cylab/python-network-analysis
https://realpython.com/python-testing/
https://realpython.com/command-line-interfaces-python-argparse/#reader-comments

Core:
- [x] Argparse to handle flags for either loading pcap or capturing
- [x] Live sniffer using scapy
- [x] Packet storage
- [x] Pcap loader using scapy

Analysis:
- [ ] Cleartext detector, logic to check for common cleartext ports and scanning payload for keyword "USER", "PASS", or "GET".
- [ ] Port Scan Detector, tracks unique destination ports per source IP, trigger alert if a threshold of e.g. 20 ports is surpassed within a given timeframe.
- [ ] ARP Spoofing, maintain a dictionary of IP addresss mapped to their MAC address, trigger alert if an IP Address changes MAC address.

Database:
- [ ] Enters every new threat into a Database PostgreSQL(IP, Date, Port, Threat Activity)

Ollama:
- [ ] Let Ollama make a summary of threats detected in the loaded pcap file, as well as looking in the Database to see if the IP-Address has been detected as a threat actor before, create a recommendation if the IP has been detected before.
