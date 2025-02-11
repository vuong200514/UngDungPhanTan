from pupdb.core import PupDB
db = PupDB('phonebook.json')
ten = [
    "Đào Mạnh Vương", "Lê Thị Hồng", "Nguyễn Thị Mai", "Phạm Văn Hùng", "Hoàng Thị Lan",
    "Đặng Văn Sơn", "Bùi Thị Thu", "Vũ Văn Nam", "Phan Thị Hạnh", "Ngô Văn Dũng",
    "Đỗ Thị Hương", "Lý Văn Tùng", "Trịnh Thị Ngọc", "Nguyễn Văn Minh", "Lê Thị Thanh",
    "Phạm Thị Hòa", "Hoàng Văn Phúc", "Đặng Thị Kim", "Bùi Văn Khánh", "Vũ Thị Liên"
]
diaChi = [
    "197 Trần Phú, Hà Nội", "456 đường Trần Duy Hưng, Hà Nội", "789 đường Trần Hưng Đạo, Hà Nội", "101 đường Phan Bội Châu, Hà Nội",
    "112 đường Hai Bà Trưng, Hà Nội", "131 đường Trần Duy Hưng, Hà Nội", "415 đường Trần Hưng Đạo, Hà Nội", "161 đường Phan Bội Châu, Hà Nội",
    "718 đường Hai Bà Trưng, Hà Nội", "192 đường Trần Duy Hưng, Hà Nội", "202 đường Trần Hưng Đạo, Hà Nội", "213 đường Phan Bội Châu, Hà Nội",
    "224 đường Hai Bà Trưng, Hà Nội", "235 đường Trần Duy Hưng, Hà Nội", "246 đường Trần Hưng Đạo, Hà Nội", "257 đường Phan Bội Châu, Hà Nội",
    "268 đường Hai Bà Trưng, Hà Nội", "279 đường Trần Duy Hưng, Hà Nội", "280 đường Trần Hưng Đạo, Hà Nội", "291 đường Phan Bội Châu, Hà Nội"
]
emails = [
    "aoaao25@gmail.com", "hong@gmail.com", "mai@gmail.com", "hung@gmail.com", "lan@gmail.com",
    "son@gmail.com", "thu@gmail.com", "nam@gmail.com", "hanh@gmail.com", "dung@gmail.com",
    "huong@gmail.com", "tung@gmail.com", "ngoc@gmail.com", "minh@gmail.com", "thanh@gmail.com",
    "hoa@gmail.com", "phuc@gmail.com", "kim@gmail.com", "khanh@gmail.com", "lien@gmail.com"
]
sdt = [
    "0974807212", "0974807213", "0974807214", "0974807215", "0974807216",
    "0974807217", "0974807218", "0974807219", "0974807220", "0974807221",
    "0974807222", "0974807223", "0974807224", "0974807225", "0974807226",
    "0974807227", "0974807228", "0974807229", "0974807230", "0974807231"
]
for i in range(20):
    thongTin = {
        "ten": ten[i],
        "diachi": diaChi[i],
        "email": emails[i]
    }
    db.set(sdt[i], thongTin)

# Hàm tìm kiếm thông tin
def timKiem(sdt):
    contact = db.get(sdt)
    if contact:
        print(f"Thông tin liên hệ cho số điện thoại {sdt}:")
        print(f"Tên: {contact['ten']}")
        print(f"Địa chỉ: {contact['diachi']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"Không tìm thấy thông tin liên hệ cho số điện thoại {sdt}")

timKiem("0974807212")