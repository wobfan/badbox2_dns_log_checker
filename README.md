# BadBox2 DNS Log Checker

A simple Python script to search NextDNS logs for BadBox2 malware C2 domains.

## Getting Your DNS Log

1. Go to [my.nextdns.io](https://my.nextdns.io)
2. Navigate to **Settings**
3. Click on **Export Logs**
4. Download your log file (CSV format)

## Usage

1. Place your NextDNS log file (`XXXXXX.csv`) in the project directory
2. Run the script:
   ```bash
   python badbox2_dns_checker.py
   ```

The script will search for known BadBox2 C2 domains and report any matches found in your DNS logs.

## About BadBox2

BadBox2 is a malware that targets Android devices. This tool helps identify potential infections by checking DNS logs for communication with known command and control servers.

C2 domain list source: [Human Security BadBox 2.0 Report](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/)