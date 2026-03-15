import time
import os


def wait(seconds: float = 1.0):
    """Chờ một khoảng thời gian (giây)"""
    time.sleep(seconds)


def make_dir(path: str):
    """Tạo thư mục nếu chưa tồn tại"""
    os.makedirs(path, exist_ok=True)


def get_platform() -> str:
    """Lấy platform hiện tại từ biến môi trường"""
    return os.getenv("PLATFORM", "android").lower()


def is_android() -> bool:
    return get_platform() == "android"


def is_ios() -> bool:
    return get_platform() == "ios"
