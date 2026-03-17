@echo off
echo ============================================
echo  RESET MOI TRUONG TRUOC KHI CHAY TEST
echo ============================================

echo [1/6] Kill Appium server...
taskkill /F /IM node.exe /T 2>nul
timeout /t 2 /nobreak >nul

echo [2/6] Reset ADB server...
adb kill-server
timeout /t 2 /nobreak >nul
adb start-server
timeout /t 2 /nobreak >nul

echo [3/6] Kill UiAutomator2 tren dien thoai...
adb shell am force-stop io.appium.uiautomator2.server
adb shell am force-stop io.appium.uiautomator2.server.test
timeout /t 1 /nobreak >nul

echo [4/6] Kill Zing MP3...
adb shell am force-stop com.zing.mp3
timeout /t 1 /nobreak >nul

echo [5/6] Mo lai Zing MP3...
adb shell monkey -p com.zing.mp3 -c android.intent.category.LAUNCHER 1
timeout /t 5 /nobreak >nul

echo [6/6] Khoi dong Appium server moi...
start "Appium Server" cmd /k appium
timeout /t 5 /nobreak >nul

echo ============================================
echo  XONG! Gio chay test trong PyCharm
echo ============================================
pause
```

---

## Quy Trình Chuẩn Từ Giờ
```
Mỗi buổi sáng hoặc sau khi máy restart:
  1. Double click reset_and_run.bat
  2. Chờ thấy "Appium REST http interface listener started"
  3. Mở PyCharm → chạy test

Sau khi test xong:
  1. Nhấn Stop (■) — chờ "[STOP] Dong driver"
  2. KHÔNG terminate giữa chừng

Nếu bị chậm bất thường:
  1. Stop test
  2. Double click reset_and_run.bat
  3. Chạy lại