# Module request để gủi các yêu cầu HTTP sử dụng để gửi yêu cầu tới http://testphp.vulnweb.com
import requests
# Khởi tạo một mảng rỗng logins
logins = []
# Mở file login.txt
with open('DangTuanAnh_AT180305_TH2/login.txt','r') as fileHandle:
    # Đọc từng dòng trong file và đẩy vào trong mảng logins
    for line in fileHandle:
       login = line[:-1]
       logins.append(login)
# Khai báo url và gán giá trị là trang web để thực hiện 
url = "http://testphp.vulnweb.com"
#Sử dụng vòng lặp để thực hiện từng trường hợp trong mảng logins
for login in logins:
    # In ra màn hình url đang thực hiện
    print("Checking..." + url + login)
    # Gửi yêu câu tới url đang thực hiện và gán giá trị trả về là response
    response = requests.get(url + login)
    # Nếu giá trị trả về là 200 thì là thành công
    if response.status_code == 200:
        print("Login resource detected: " + login)