# Module os để tương tác với hệ điều hành. Trong trường hợp này thì truy cập tới biến môi trường là  SHODAN_API_KEY
import shodan
# Truy cập tới biến môi trường SHODAN_API_KEY để lấy giá trị và gán giá trị cho biến SHODAN_API_KEY
import os
# Gán biến là một mảng rỗng
servers = []
SHODAN_API_KEY = os.environ['SHODAN_API_KEY']

# Khởi tạo Shodan với SHODAN_API_KEY
shodanApi = shodan.Shodan(SHODAN_API_KEY)
   
# Thực hiện tìm kiếm sử dụng API của Shodan để tìm danh sách địa chỉ IP cho các máy chủ FTp đăng nhập ở chế độ Anonymous
results = shodanApi.search("port: 21 Anonymous user logged in")
# In số lượng hosts
print("hosts number: " + str(len(results["matches"])))

# Sử dùng vòng lặp để lấy ra ip để append vào mảng servers
for result in results["matches"]:
    if result["ip_str"] is not None:
        servers.append(result["ip_str"])
# Sử dùng vòng lặp để in ra tất cả các ip
for ip in servers:
    print(ip)
