import socket
from IPy import IP


# 147.91.19.26

# 192.168.184.128

# Scan ports
def scan(target, portNumber):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target]  ' + str(target))
    for port in range(1, portNumber):
        scanPort(converted_ip, port)


# Convert domain name to ip address
def check_ip(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except:
        return socket.gethostbyname(ipaddress)


# Grabbing service's details
def getBanner(sock):
    return sock.recv(1024)


# this function will scan the port is open or not
def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = getBanner(sock)
            print("[+] Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


if __name__ == '__main__':
    targets = input("[+] Enter Target/s To Scan:(split multiple targets by ,): ")
    portNumber = input("[+] Enter Port Number To Scan: ")
    if ',' in targets:
        for ipAddress in targets.split(','):
            scan(ipAddress.strip(' '), portNumber)
    else:
        scan(targets, portNumber)
