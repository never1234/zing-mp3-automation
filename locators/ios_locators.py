# ============================================================
# iOS Locators — Element của Zing MP3 trên iOS
# Dùng Appium Inspector trên Mac để lấy accessibility id thật
# ============================================================


class IOSHomeLocators:
    # Bottom navigation tabs
    BOTTOM_NAV_HOME    = ("accessibility id", "tab_home")
    BOTTOM_NAV_CHART   = ("accessibility id", "tab_chart")
    BOTTOM_NAV_RADIO   = ("accessibility id", "tab_radio")
    BOTTOM_NAV_LIBRARY = ("accessibility id", "tab_library")
    BOTTOM_NAV_PROFILE = ("accessibility id", "tab_profile")

    # Nút tìm kiếm trên header màn hình Khám phá
    SEARCH_BUTTON      = ("accessibility id", "search_button")

    # Bài hát đầu tiên trong section "Phát nhanh" ở màn hình Khám phá
    QUICK_PLAY_FIRST_ITEM = ("xpath",
        "(//XCUIElementTypeOther"
        "[.//XCUIElementTypeStaticText[@name='Phát nhanh']]"
        "//XCUIElementTypeImage)[1]")

    # Mini player hiện phía dưới khi có bài đang phát
    MINI_PLAYER        = ("accessibility id", "mini_player")


class IOSSearchLocators:
    SEARCH_BAR         = ("accessibility id", "search_bar")
    SEARCH_INPUT       = ("accessibility id", "search_input")
    FIRST_SONG_RESULT  = ("xpath",
        "//XCUIElementTypeCell[1]"
        "//XCUIElementTypeStaticText[@name='song_title']")
    SONG_LIST          = ("accessibility id", "search_result_list")
    NO_RESULT_TEXT     = ("accessibility id", "no_result_label")


class IOSPlayerLocators:
    # Thông tin bài hát
    SONG_TITLE         = ("accessibility id", "song_title_label")
    ARTIST_NAME        = ("accessibility id", "artist_name_label")

    # Các nút điều khiển chính
    PLAY_PAUSE_BTN     = ("accessibility id", "btn_play_pause")
    NEXT_BTN           = ("accessibility id", "btn_next")
    PREV_BTN           = ("accessibility id", "btn_prev")

    # Các nút tính năng
    SHUFFLE_BTN        = ("accessibility id", "btn_shuffle")
    REPEAT_BTN         = ("accessibility id", "btn_repeat")
    HEART_BTN          = ("accessibility id", "btn_like")

    # Thanh tiến trình
    PROGRESS_BAR       = ("accessibility id", "progress_slider")

    # Nút gập player xuống mini player (mũi tên xuống ở góc trên)
    MINIMIZE_BTN       = ("accessibility id", "btn_minimize")


class IOSLoginLocators:
    LOGIN_BTN          = ("accessibility id", "btn_login")
    EMAIL_INPUT        = ("accessibility id", "input_email")
    PASSWORD_INPUT     = ("accessibility id", "input_password")
    SUBMIT_BTN         = ("accessibility id", "btn_submit")
    ERROR_MSG          = ("accessibility id", "label_error")
    AVATAR             = ("accessibility id", "img_avatar")
