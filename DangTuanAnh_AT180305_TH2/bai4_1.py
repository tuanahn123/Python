import nmap

portScanner = nmap.PortScanner()
host_scan = input('Host scan: ')
portList = "21,22,23,25,80"
portScanner.scan(hosts=host_scan,arguments='-n -p' + portList)
print(portScanner.command_line())
host_list = [(x,portScanner[x]['status']['state']) for x in portScanner.all_hosts()]

for host,status in host_list:
    print(host,status)
for protocol in portScanner[host].all_protocols():
    print('Protocol : %s' % protocol)
    listPort = portScanner[host]['tcp'].keys()
    for port in listPort:
        print('Port : %s State : %s' % (port, portScanner[host][protocol][port]['state']))