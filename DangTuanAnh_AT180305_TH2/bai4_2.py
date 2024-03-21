# Module nmap sử dụng để tương tác với Nmap, một công cụ để quét mạng
import nmap
# Khở tạo lớp NmapScanner
class NmapScanner:
    # Phương thức khởi tạo đối tượng scanner để thực hiện quét
    def __init__(self):
        self.portScanner = nmap.PortScanner()
    
    # Định nghĩa phương thức nmap nhận vào hai tham số là self, địa chỉ ip, port
    def nmapScan(self,ip_address,port):
        # Thực hiện quét cổng trên địa chỉ ip và cổng
        self.portScanner.scan(ip_address,port)
        # iIn ra câu lệnh nmap thực sự được sử dụng trong quá trình quét
        print(" [+] Executing commanf: ", self.portScanner.command_line())

# Khởi tạo hàm main
def main():
    # Yêu cầu người dùng nhập vào địa chỉ ip
    ip_address = input("IP scan: ")
    # Khởi tạo một mảng gồm các cổng cần quét
    ports = ["21","22","23","25","80","443"]
    # Thực hiện quét các cổng được khai báo ở trên
    for port in ports:
        # Sử fungfj phương thức nmapScan đã được định nghĩa ở trên
        NmapScanner().nmapScan(ip_address,port)
# Hàm main để chạy chương trình
if __name__ == "__main__":
    main()