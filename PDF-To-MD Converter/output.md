UFW (Uncomplicated
Firewall)
The ufw (Uncomplicated Firewall) is a user-friendly command-line tool for managing firewall rules on Linux systems.
Syntax:
ufw [command] [options] 
Basic Commands:
Command
Description
ufw status
Check firewall status.
ufw enable
Enable the firewall.
ufw disable
Disable the firewall.
ufw allow 22
Allow incoming connections on port 22 (SSH).
ufw deny 80
Block access to port 80 (HTTP).
ufw delete allow 22
Remove the rule allowing port 22.
ufw allow from 192.168.1.100 Allow traffic from a specific IP.
ufw deny from 192.168.1.100 Block traffic from a specific IP.
ufw reset
Reset all firewall rules.
Example Usage:
ufw enable
ufw allow 80/tcp 
ufw status
Example Output:
Status: active 
To                         Action      From 
--                         ------      ---- 
80/tcp                     ALLOW       Anywhere 
22/tcp                     ALLOW       Anywhere 
Note:
ufw is a frontend for iptables and is commonly used in Ubuntu and Debian-based systems.
Use sudo before ufw commands for administrative access.
Conclusion:
ifconfig → Used for managing network interfaces (deprecated in favor of ip).
ufw → Simple firewall tool to allow or block network traffic.
Both are essential for managing Linux networking and security.
