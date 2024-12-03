# Điều Khiển Chuột Ảo Bằng Nhận Diện Cử Chỉ Tay

## Mô Tả Dự Án

Ứng dụng điều khiển chuột máy tính không cần tiếp xúc sử dụng công nghệ nhận diện cử chỉ tay MediaPipe. Người dùng có thể điều khiển con trỏ và thực hiện các thao tác chuột như nhấp, kéo, chụp màn hình chỉ bằng cử động tay.

## Tính Năng

- Di chuyển con trỏ theo ngón trỏ
- Nhấp chuột trái 
- Nhấp chuột phải
- Nhấp đúp
- Chụp màn hình

## Yêu Cầu Hệ Thống

- Python 3.7+
- Webcam
- Các thư viện: 
  * OpenCV
  * MediaPipe
  * PyAutoGUI
  * Pynput

## Cài Đặt

1. Clone dự án
```bash
git clone https://github.com/duonghiepit/virtual-mouse-gesture.git
cd virtual-mouse-gesture
```

2. Tạo môi trường ảo
```bash
python -m venv venv
source venv/bin/activate  # Trên Linux/macOS
venv\Scripts\activate    # Trên Windows
```

3. Cài đặt các phụ thuộc
```bash
pip install -r requirements.txt
```

## Sử Dụng

```bash
python main.py
```

Nhấn 'q' để thoát ứng dụng.

## Hướng Dẫn Cử Chỉ

- Di chuyển: Giữ ngón trỏ duỗi thẳng
- Nhấp chuột trái: Gập ngón trỏ
- Nhấp chuột phải: Gập ngón giữa
- Nhấp đúp: Gập cả ngón trỏ và ngón giữa
- Chụp màn hình: Gập ngón trỏ và ngón giữa, thu ngón cái lại

## Giấy Phép

MIT License

## Tác Giả

Hiep Duong Trong# virtual-mouse-gesture
