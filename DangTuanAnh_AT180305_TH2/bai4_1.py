# Module nmap sử dụng để tương tác với Nmap, một công cụ để quét mạng
import nmap
# Khởi tạo đối tượng PortScanner để sử dụng quét các cổng
portScanner = nmap.PortScanner()
# Yếu câu người dùng nhập vào host muốn quét và gán vào biến host_scan
host_scan = input('Host scan: ')
# Khai báo một chuỗi các cổng mạng cần được quét, cách nhau bằng dấu phẩy
portList = "21,22,23,25,80"
# Thực hiện quét cổng:
# Sử dụng phương thức scan của đối tượng PortScanner để quết trên máy chủ được chỉ định hosts = host_scan
# Tham số -n : Để không giải quyết tên miền
# Tham số -p: Để chỉ định danh sách cổng là danh sách các cổng đã khai báo ở trên
portScanner.scan(hosts=host_scan,arguments='-n -p' + portList)
# In ra man hình dòng lệnh nmap thực thế sử dụng để thực hiện quét
print(portScanner.command_line())
# Tạo một dánh sách các máy chủ và trạng thái từ kết quả quét
host_list = [(x,portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
# In ra màn hình máy chủ và trạng thái đã quét được
for host,status in host_list:
    print(host,status)
# In ra màn hìn thông tin chi tiết của cổng
for protocol in portScanner[host].all_protocols():
    # In ra màn hình tất cả các giao thức
    print('Protocol : %s' % protocol)
    # Khởi tạo danh sách cổng với giao thức TCP
    listPort = portScanner[host]['tcp'].keys()
    for port in listPort:
        # In ra màn hình cổng và trạng thái kết quả đã quét
        print('Port : %s State : %s' % (port, portScanner[host][protocol][port]['state']))