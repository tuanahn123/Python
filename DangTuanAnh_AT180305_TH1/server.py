import socket
    # Khai báo tên hàm start_server với host là localhost (127.0.0.1) và port là 3000
def start_server(host='127.0.0.1', port=3000):
    # Dùng để tạo một đối tượng socket của server, serverSocket
    # - Tham số đầu tiên cho biết đại chị IP, cụ thể AF_INET chỉ ra mạng đang sử dụng IPV4
    # - Tham số thứ 2 cho biêt loại socket là TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Gắn socket với địa chỉ IP và cổng để server có thể lắng nghe các kết nổi đến trên cổng này
        s.bind((host, port))
        # Bắt đầu lắng nghe kết nối từ client
        s.listen()
        # In ra để biết server đang lắng nghe trên cổng nào
        print(f"Server đang lắng nghe trên {host}:{port}")
        # Chấp nhận một kết nối từ client
        # một socket mới conn được sử dụng để giao tiếp với client và địa chỉ address của client đó.
        conn, address = s.accept()
        # Sử dụng with để xử lý nếu có error thì socket được đóng lại đúng cách
        with conn:
            # In ra để biết server đã lắng nghe được kết nối từ client
            print(f"Kết nối từ {address}")
            # Tạo một vòng lặp vô hạn để liên tục xử lý dữ liệu từ client
            while True:
                # Nhận dữ liệu từ client lấy kích thước bộ đệm tối đa chỗ mỗi lần gọi là 1024
                data = conn.recv(1024)
                if not data:
                    # Nếu không có dữ liệu, ngừng lắng nghe
                    break 
                # Gửi lại dữ liệu đã chuyển thành chữ hoa
                conn.sendall(data.upper())

if __name__ == "__main__":
    # Chạy hàm start_server
    start_server()
