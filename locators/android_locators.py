# locators/android_locators.py
from appium.webdriver.common.appiumby import AppiumBy


class AndroidHomeLocators:
    # Bottom navigation tabs
    BOTTOM_NAV_LIBRARY = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.zing.mp3:id/bnv']/android.widget.FrameLayout[1]")
    BOTTOM_NAV_HOME    = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.zing.mp3:id/bnv']/android.widget.FrameLayout[2]")
    BOTTOM_NAV_CHART   = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.zing.mp3:id/bnv']/android.widget.FrameLayout[3]")
    BOTTOM_NAV_RADIO   = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.zing.mp3:id/bnv']/android.widget.FrameLayout[4]")
    BOTTOM_NAV_PROFILE = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.zing.mp3:id/bnv']/android.widget.FrameLayout[5]")

    # Nút tìm kiếm trên header màn hình Khám phá
    SEARCH_BUTTON      = (AppiumBy.ID, "com.zing.mp3:id/search")

    # Bài hát đầu tiên trong section "Phát nhanh" ở màn hình Khám phá
    QUICK_PLAY_FIRST_ITEM = (AppiumBy.XPATH,
        "(//android.widget.TextView[@text='Phát nhanh']"
        "/parent::*/parent::*/following-sibling::*"
        "//android.widget.ImageView)[1]")

    # Mini player hiện phía dưới màn hình khi có bài đang phát
    MINI_PLAYER        = (AppiumBy.ID, "com.zing.mp3:id/playbarContainer")

    # Popup quảng cáo / khuyến mãi (xuất hiện khi mở app)
    POPUP_SKIP_BTN     = (AppiumBy.ID, "com.zing.mp3:id/btnNegative")

    # Bottom sheet (Đặc quyền Premium, v.v.) — nhấn vùng ngoài để đóng
    BOTTOM_SHEET_OUTSIDE = (AppiumBy.ID, "com.zing.mp3:id/touch_outside")


class AndroidSearchLocators:
    SEARCH_BAR         = (AppiumBy.ID, "com.zing.mp3:id/search")
    SEARCH_INPUT       = (AppiumBy.ID, "com.zing.mp3:id/edtSearch")
    FIRST_SONG_RESULT  = (AppiumBy.XPATH,
        "(//androidx.recyclerview.widget.RecyclerView//android.widget.TextView"
        "[@resource-id='com.zing.mp3:id/tvTitle'])[1]")
    SONG_LIST          = (AppiumBy.ID, "com.zing.mp3:id/recyclerView")
    NO_RESULT_TEXT     = (AppiumBy.ID, "com.zing.mp3:id/tvEmpty")


class AndroidLoginLocators:
    LOGIN_BTN      = (AppiumBy.ID, "com.zing.mp3:id/btnLogin")
    EMAIL_INPUT    = (AppiumBy.ID, "com.zing.mp3:id/edtEmail")
    PASSWORD_INPUT = (AppiumBy.ID, "com.zing.mp3:id/edtPassword")
    SUBMIT_BTN     = (AppiumBy.ID, "com.zing.mp3:id/btnSubmit")
    ERROR_MSG      = (AppiumBy.ID, "com.zing.mp3:id/tvError")
    AVATAR         = (AppiumBy.ID, "com.zing.mp3:id/imgAvatar")


class AndroidPlayerLocators:
    # Thông tin bài hát
    SONG_TITLE         = (AppiumBy.ID, "com.zing.mp3:id/tvTitleSong")
    ARTIST_NAME        = (AppiumBy.ID, "com.zing.mp3:id/tvSubTitle")

    # Các nút điều khiển chính
    PLAY_PAUSE_BTN     = (AppiumBy.ID, "com.zing.mp3:id/btnPlay")
    NEXT_BTN           = (AppiumBy.ID, "com.zing.mp3:id/btnNext")
    PREV_BTN           = (AppiumBy.ID, "com.zing.mp3:id/btnPrev")

    # Các nút tính năng
    SHUFFLE_BTN        = (AppiumBy.ID, "com.zing.mp3:id/imgHotActionLeft")
    REPEAT_BTN         = (AppiumBy.ID, "com.zing.mp3:id/imgHotActionRight")
    HEART_BTN          = (AppiumBy.ID, "com.zing.mp3:id/btnFav")

    # Thanh tiến trình
    PROGRESS_BAR       = (AppiumBy.ID, "com.zing.mp3:id/seekBar")

    # Nút gập player xuống mini player (mũi tên xuống ở góc trên)
    MINIMIZE_BTN       = (AppiumBy.ID, "com.zing.mp3:id/btnBack")


class AndroidChartLocators:
    # Row đầu tiên (bài hát #1) trong danh sách ZingChart
    CHART_TOP1_ITEM    = (AppiumBy.XPATH,
        "(//androidx.recyclerview.widget.RecyclerView"
        "//android.widget.RelativeLayout[@clickable='true'])[1]")

    # Thumbnail bài hát top 1 (fallback)
    CHART_TOP1_THUMB   = (AppiumBy.XPATH,
        "(//android.widget.ImageView[@resource-id='com.zing.mp3:id/imgThumb'])[1]")

    # Tiêu đề bài hát top 1 — dùng để verify
    CHART_TOP1_TITLE   = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle'])[1]")
