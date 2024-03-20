import socket
    # Khai báo tên hàm start_client với mặc định host là localhost (127.0.0.1) và port 3000
def start_client(server_host='127.0.0.1', server_port=3000):
    #   Dùng để tạo một đối tượng socket của client, clientSocket
    # - Tham số đầu tiên cho biết đại chị IP, cụ thể AF_INET chỉ ra mạng đang sử dụng IPV4
    # - Tham số thứ 2 cho biêt loại socket là TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Kết nối tới server với cổng ở trên
        s.connect((server_host, server_port))
        # Tạo một vòng lặp vô hạn để client có thể gửi nhiều tin nhắn cho đến khi người dùng quyết định thoát
        while True:
            # In ra màn hình
            message = input("Nhập dữ liệu để gửi ('exit' để thoát): ")
            if message.lower() == 'exit':
            # Nếu nhập là chuỗi 'exit' thì thoát chương trình
                break
            # Mã hóa chuỗi nhập vào thành dạng bytes và gửi đến server. sendall để đảm bảo tất cả bytes được gửi đi
            s.sendall(message.encode())
            # Nhận dữ liệu từ server. 
            # Chỉ định số bytes tối đa nhận được là 1024
            data = s.recv(1024)
            # Giải mã dữ liệu nhận được từ server dưới dạng bytes thành chuỗi và in ra màn hình.
            print(f"Dữ liệu từ server: {data.decode()}")

if __name__ == "__main__":
    # Chạy hàm start_client
    start_client()
