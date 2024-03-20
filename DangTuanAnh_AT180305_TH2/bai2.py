# Module dns cho phép truy vấn DNS và nhận thông tin về tên miền
import dns.resolver
# Tạo biến hosts và gán là mảng chuỗi các giá trị miền mà muốn truy vấn
hosts = ["oreilly.com","yahoo.com","google.com","microsoft.com","cnn.com"]
# Sử dụng vòng lặp để truy vấn tới từng giá trị miền ở hosts
for host in hosts:
    # In ra giá trị tên miền truy vấn
    print(host)
    # Sử dụng hàm resole để lấy bản ghi A (Địa chỉ IPv4) cho tên miền đó
    ipv4 = dns.resolver.resolve(host,"A")
    ipv6 = dns.resolver.resolve(host,"AAAA")
    # Sử dụng vòng lặp để in ra giá trị ip đã tìm được
    for i in ipv4:
        print(i)