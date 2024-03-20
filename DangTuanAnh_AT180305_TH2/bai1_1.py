# Module request để gủi các yêu cầu HTTP sử dụng để get đến API của shodan.io
import requests
# Module os để tương tác với hệ điều hành. Trong trường hợp này thì truy cập tới biến môi trường là  SHODAN_API_KEY
import os
# Truy cập tới biến môi trường SHODAN_API_KEY để lấy giá trị và gán giá trị cho biến SHODAN_API_KEY
SHODAN_API_KEY  = os.environ['SHODAN_API_KEY']
# Gán cho biến ip
ip = '8.8.8.8'
# Hàm shodanInfo nhận mội đối số là ip để gọi api tới shodan và trả về kết quả
def shodanInfo(ip):
    try:
        # GET API tới Shodan sử dụng URL với địa chị ip và SHODAN_API_KEY
        # Phương thức .json() để chuyển nội dung response thành dạng json
        result  = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key=${SHODAN_API_KEY}&minify=True").json()
        # Nếu có lỗi xảy ra trong quá trình request thì in ra màn hình báo lỗi
    except Exception as exception:
        result = {'error': "Information not avaliable"}
    return result
#In ra kết quả trả về của hàm shodanInfo
print(shodanInfo(ip))