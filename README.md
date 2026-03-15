# 🎵 Zing MP3 Automation Test

Automation test cho ứng dụng **Zing MP3** trên Android, iOS và Web.

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.11+ |
| Mobile Framework | Appium v2 |
| Test Runner | Pytest |
| Báo cáo | Allure Report |
| Platform | Android ✅ · iOS ✅ (cần Mac) |

---

## 📁 Cấu Trúc Project

```
zing-mp3-automation/
├── configs/
│   ├── android_config.py     # Cấu hình Android
│   └── ios_config.py         # Cấu hình iOS
├── locators/
│   ├── android_locators.py   # Element ID Android
│   └── ios_locators.py       # Element ID iOS
├── pages/
│   ├── base_page.py          # Hàm dùng chung 2 platform
│   ├── home_page.py
│   ├── search_page.py
│   ├── player_page.py
│   └── login_page.py
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_playback.py
├── utils/
│   └── helpers.py
├── conftest.py               # Setup driver, chụp ảnh khi fail
├── pytest.ini
├── requirements.txt
└── .env.example
```

---

## ⚙️ Cài Đặt

### 1. Yêu cầu phần mềm
```
- Python 3.11+
- Node.js 18+
- JDK 11+
- Android Studio (có AVD emulator)
- Appium v2
```

### 2. Cài Appium
```bash
npm install -g appium
appium driver install uiautomator2   # Android
appium driver install xcuitest       # iOS — cần Mac
```

### 3. Cài Python packages
```bash
pip install -r requirements.txt
```

### 4. Tạo file .env
```bash
cp .env.example .env
# Mở .env và điền thông tin thật vào
```

---

## 🚀 Chạy Test

### Khởi động Appium server (Terminal 1)
```bash
appium
```

### Chạy test (Terminal 2)

```bash
# Android
pytest tests/ --platform=android -v

# iOS
pytest tests/ --platform=ios -v

# Chạy 1 file cụ thể
pytest tests/test_search.py --platform=android -v

# Chạy 1 test cụ thể
pytest tests/test_playback.py::TestPlayback::test_next_song --platform=android -v
```

---

## 📊 Xem Báo Cáo Allure

```bash
# Sau khi chạy test xong
allure serve reports/allure-results
```

Báo cáo tự động mở trên browser với:
- ✅ Số test pass / fail
- 📸 Screenshot khi test fail
- ⏱️ Thời gian chạy từng test
- 📋 Chi tiết từng bước

---

## 📱 Lấy Element ID Thật

Dùng **Appium Inspector** để lấy element ID của từng màn hình:

```bash
# Cài Appium Inspector
npm install -g appium-inspector

# Mở và kết nối vào thiết bị đang chạy app
# Click vào element → copy ID → paste vào locators/
```

---

## 🔄 Git Workflow

```bash
# Lần đầu
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main

# Hàng ngày
git add .
git commit -m "Add/Fix: mô tả ngắn"
git push
```

---

## ⚠️ Lưu Ý Quan Trọng

- File `.env` **KHÔNG** được push lên Git (đã có trong .gitignore)
- Locator trong `locators/` là **placeholder** — cần dùng Appium Inspector để lấy ID thật
- iOS cần chạy trên **macOS** — không thể chạy trên Windows
