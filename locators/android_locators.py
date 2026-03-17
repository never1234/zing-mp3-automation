# locators/android_locators.py
from appium.webdriver.common.appiumby import AppiumBy


class AndroidHomeLocators:
    # ── Bottom navigation tabs ────────────────────────────────────────────────
    # Dùng tvLabel text — nhanh hơn FrameLayout instance(), tránh lỗi is_enabled() trên container
    BOTTOM_NAV_LIBRARY = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Thư viện")')
    BOTTOM_NAV_HOME    = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Khám phá")')
    BOTTOM_NAV_CHART   = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("#zingchart")')
    BOTTOM_NAV_RADIO   = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Phòng nhạc")')
    BOTTOM_NAV_PROFILE = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Cá nhân")')

    # ── Bottom Navigation — nhãn tab (alias) ─────────────────────────────────
    BOTTOM_NAV_LABEL_THU_VIEN   = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Thư viện")')
    BOTTOM_NAV_LABEL_KHAM_PHA   = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Khám phá")')
    BOTTOM_NAV_LABEL_ZINGCHART  = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("#zingchart")')
    BOTTOM_NAV_LABEL_PHONG_NHAC = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Phòng nhạc")')
    BOTTOM_NAV_LABEL_CA_NHAN    = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/tvLabel").text("Cá nhân")')

    # ── Nút tìm kiếm trên header màn hình Khám phá ───────────────────────────
    SEARCH_BUTTON      = (AppiumBy.ID, "com.zing.mp3:id/search")

    # ── Bài hát đầu tiên trong section "Phát nhanh" ──────────────────────────
    # Dùng viewPager resource-id thay vì parent/following-sibling XPath — nhanh hơn ~10x trên real device
    QUICK_PLAY_FIRST_ITEM = (AppiumBy.XPATH,
        "(//androidx.viewpager.widget.ViewPager[@resource-id='com.zing.mp3:id/viewPager']"
        "//android.widget.RelativeLayout[@clickable='true'])[1]")

    # ── Mini player ───────────────────────────────────────────────────────────
    MINI_PLAYER         = (AppiumBy.ID, "com.zing.mp3:id/playbarContainer")
    MINI_PLAYER_PLAY_PAUSE = (AppiumBy.ID, "com.zing.mp3:id/btnPlayPause")
    MINI_PLAYER_FAV     = (AppiumBy.ID, "com.zing.mp3:id/btnFav")
    MINI_PLAYER_THUMB   = (AppiumBy.ID, "com.zing.mp3:id/imgThumb")
    MINI_PLAYER_DISC    = (AppiumBy.ID, "com.zing.mp3:id/imgDisc")
    MINI_PLAYER_PROGRESS = (AppiumBy.ID, "com.zing.mp3:id/progress")

    # ── Popup quảng cáo / khuyến mãi ────────────────────────────────────────
    POPUP_SKIP_BTN      = (AppiumBy.ID, "com.zing.mp3:id/btnNegative")

    # ── Bottom sheet — nhấn vùng ngoài để đóng ──────────────────────────────
    BOTTOM_SHEET_OUTSIDE = (AppiumBy.ID, "com.zing.mp3:id/touch_outside")

    # ── Màn hình Khám phá — Header ───────────────────────────────────────────
    PAGE_TITLE          = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/text' and @text='Khám phá']")

    # ── Màn hình Khám phá — Section "Phát nhanh" ────────────────────────────
    SECTION_PHAT_NHANH  = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/text' and @text='Phát nhanh']")
    TOP100_PLAYLIST_FIRST = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle'])[1]")

    # ── Màn hình Khám phá — Section "Gợi ý bài hát" ─────────────────────────
    SECTION_GOI_Y_BAI_HAT = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle' and @text='Gợi ý bài hát']")
    BTN_PHAT_TAT_CA     = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/tvPlay' and @text='Phát tất cả']")
    SONG_TITLE_IN_LIST  = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle'])[2]")
    SONG_ARTIST_IN_LIST = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvArtist'])[1]")

    # ── Màn hình Khám phá — Section "Top 100" ───────────────────────────────
    SECTION_TOP_100     = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/text' and @text='Top 100']")
    TOP100_ITEM_TITLE   = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle' and contains(@text,'Top 100')])[1]")

    # ── Màn hình Khám phá — Category Tabs ───────────────────────────────────
    CATEGORY_TABS       = (AppiumBy.ID,   "com.zing.mp3:id/rvCategory")
    # childSelector scoped vào rvCategory — tránh crash UiAutomator2 do tvTitle match quá nhiều element
    TAB_CHO_BAN         = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/rvCategory")'
        '.childSelector(new UiSelector().resourceId("com.zing.mp3:id/tvTitle").text("Cho bạn"))')
    TAB_THU_GIAN        = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/rvCategory")'
        '.childSelector(new UiSelector().resourceId("com.zing.mp3:id/tvTitle").text("Thư giãn"))')
    TAB_WORKOUT         = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/rvCategory")'
        '.childSelector(new UiSelector().resourceId("com.zing.mp3:id/tvTitle").text("Workout"))')
    TAB_TAP_TRUNG       = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.zing.mp3:id/rvCategory")'
        '.childSelector(new UiSelector().resourceId("com.zing.mp3:id/tvTitle").text("Tập trung"))')
    NOTIFICATION_ICON   = (AppiumBy.ID,   "com.zing.mp3:id/ivIcon")

    # ── Màn hình Khám phá — Section "Dành riêng cho bạn" ────────────────────
    SECTION_DANH_RIENG  = (AppiumBy.XPATH,
        "//android.widget.TextView[@text='Dành riêng cho bạn']")
    BTN_REFRESH         = (AppiumBy.ID,   "com.zing.mp3:id/btnRefresh")
    BTN_REFRESH_VIEW    = (AppiumBy.ID,   "com.zing.mp3:id/btnRefreshView")

    # ── Promotion Banner ──────────────────────────────────────────────────────
    PROMOTION_ZONE_BG    = (AppiumBy.ID,  "com.zing.mp3:id/promotionZoneBg")
    PROMOTION_ZONE_TITLE = (AppiumBy.ID,  "com.zing.mp3:id/promotionZoneTitle")
    PROMOTION_ZONE_CLOSE = (AppiumBy.ID,  "com.zing.mp3:id/promotionZoneClose")
    PROMOTION_ZONE_THUMB = (AppiumBy.ID,  "com.zing.mp3:id/promotionZoneThumb")

    # ── ViewPager / Content area ──────────────────────────────────────────────
    VIEW_PAGER          = (AppiumBy.ID,   "com.zing.mp3:id/viewPager")
    PAGED_TAB           = (AppiumBy.ID,   "com.zing.mp3:id/pagedTab")
    RECYCLER_VIEW       = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")

    # ── App bar / toolbar ────────────────────────────────────────────────────
    APP_BAR             = (AppiumBy.ID,   "com.zing.mp3:id/appBar")
    TOOLBAR             = (AppiumBy.ID,   "com.zing.mp3:id/toolbar")


class AndroidSearchLocators:
    # ── Thanh tìm kiếm ───────────────────────────────────────────────────────
    SEARCH_BAR          = (AppiumBy.ID,   "com.zing.mp3:id/search")
    SEARCH_INPUT        = (AppiumBy.ID,   "com.zing.mp3:id/etSearchBar")       # ô nhập trong màn search
    SEARCH_CLEAR_BTN    = (AppiumBy.ID,   "com.zing.mp3:id/btnClear")          # nút xóa text tìm kiếm
    SEARCH_LAYOUT       = (AppiumBy.ID,   "com.zing.mp3:id/searchLayout")

    # ── Kết quả tìm kiếm ─────────────────────────────────────────────────────
    FIRST_SONG_RESULT   = (AppiumBy.XPATH,
        "(//androidx.recyclerview.widget.RecyclerView//android.widget.TextView"
        "[@resource-id='com.zing.mp3:id/tvTitle'])[1]")
    SONG_LIST           = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    NO_RESULT_TEXT      = (AppiumBy.ID,   "com.zing.mp3:id/tvEmpty")

    # ── Tabs kết quả (Nổi bật, Bài hát, MV, Nghệ sĩ, Playlist) ─────────────
    RESULT_TABS         = (AppiumBy.ID,   "com.zing.mp3:id/wrapViewPager")
    TAB_NOI_BAT         = (AppiumBy.ACCESSIBILITY_ID, "Nổi bật")
    TAB_BAI_HAT         = (AppiumBy.ACCESSIBILITY_ID, "Bài hát")
    TAB_MV              = (AppiumBy.ACCESSIBILITY_ID, "MV")
    TAB_NGHE_SI         = (AppiumBy.ACCESSIBILITY_ID, "Nghệ sĩ")
    TAB_PLAYLIST        = (AppiumBy.ACCESSIBILITY_ID, "Playlist")

    # ── Từ khóa gần đây ──────────────────────────────────────────────────────
    KEYWORD_CHIP        = (AppiumBy.ID,   "com.zing.mp3:id/tvKeyword")         # chip từ khóa gần đây
    KEYWORD_CONTAINER   = (AppiumBy.ID,   "com.zing.mp3:id/flKeywords")
    RECENT_SUBTITLE     = (AppiumBy.ID,   "com.zing.mp3:id/tvSubtitle")

    # ── Item trong danh sách kết quả ─────────────────────────────────────────
    ITEM_TITLE          = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    ITEM_ARTIST         = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    ITEM_THUMB          = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    ITEM_MORE_BTN       = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")
    SONG_INDICATOR      = (AppiumBy.ID,   "com.zing.mp3:id/songIndicator")     # bài đang phát


class AndroidLoginLocators:
    LOGIN_BTN      = (AppiumBy.ID, "com.zing.mp3:id/btnLogin")
    EMAIL_INPUT    = (AppiumBy.ID, "com.zing.mp3:id/edtEmail")
    PASSWORD_INPUT = (AppiumBy.ID, "com.zing.mp3:id/edtPassword")
    SUBMIT_BTN     = (AppiumBy.ID, "com.zing.mp3:id/btnSubmit")
    ERROR_MSG      = (AppiumBy.ID, "com.zing.mp3:id/tvError")
    AVATAR         = (AppiumBy.ID, "com.zing.mp3:id/imgAvatar")


class AndroidPlayerLocators:
    # ── Toolbar ──────────────────────────────────────────────────────────────
    TOOLBAR_PLAY_FROM    = (AppiumBy.ID, "com.zing.mp3:id/tvTitleToolbar")     # "PHÁT TỪ"
    TOOLBAR_SOURCE_NAME  = (AppiumBy.ID, "com.zing.mp3:id/tvSubTitleToolbar")  # tên playlist/nguồn
    MENU_MORE_BTN        = (AppiumBy.ID, "com.zing.mp3:id/menu_overflow")      # nút "Thêm"
    DISC_VIEW            = (AppiumBy.ID, "com.zing.mp3:id/discView")           # ảnh đĩa xoay

    # ── Thông tin bài hát ─────────────────────────────────────────────────────
    SONG_TITLE           = (AppiumBy.ID, "com.zing.mp3:id/tvTitleSong")
    ARTIST_NAME          = (AppiumBy.ID, "com.zing.mp3:id/tvSubTitle")
    HEART_BTN            = (AppiumBy.ID, "com.zing.mp3:id/btnFav")

    # ── Thanh tiến trình ─────────────────────────────────────────────────────
    PROGRESS_BAR         = (AppiumBy.ID, "com.zing.mp3:id/seekBar")
    PROGRESS_CURRENT     = (AppiumBy.ID, "com.zing.mp3:id/seekBarProgressCurrent")
    PROGRESS_MAX         = (AppiumBy.ID, "com.zing.mp3:id/seekBarProgressMax")

    # ── Điều khiển chính ─────────────────────────────────────────────────────
    SHUFFLE_BTN          = (AppiumBy.ID, "com.zing.mp3:id/imgHotActionLeft")
    PREV_BTN             = (AppiumBy.ID, "com.zing.mp3:id/btnPrev")
    PLAY_PAUSE_BTN       = (AppiumBy.ID, "com.zing.mp3:id/btnPlay")
    NEXT_BTN             = (AppiumBy.ID, "com.zing.mp3:id/btnNext")
    REPEAT_BTN           = (AppiumBy.ID, "com.zing.mp3:id/imgHotActionRight")

    # ── Action buttons (hàng 2) ───────────────────────────────────────────────
    ACTION_BTN_1         = (AppiumBy.ID, "com.zing.mp3:id/imgActionOne")
    ACTION_BTN_2         = (AppiumBy.ID, "com.zing.mp3:id/imgActionTwo")
    ACTION_BTN_3         = (AppiumBy.ID, "com.zing.mp3:id/imgActionThree")
    ACTION_BTN_4         = (AppiumBy.ID, "com.zing.mp3:id/imgActionFour")
    QUEUE_BTN            = (AppiumBy.ID, "com.zing.mp3:id/imgActionQueue")

    # ── Banner upgrade (Free/Non-login) ──────────────────────────────────────
    BOTTOM_BANNER        = (AppiumBy.ID, "com.zing.mp3:id/bottomBanner")
    BOTTOM_BANNER_TITLE  = (AppiumBy.ID, "com.zing.mp3:id/bottomBannerTitle")
    BOTTOM_BANNER_THUMB  = (AppiumBy.ID, "com.zing.mp3:id/bottomBannerThumb")

    # ── Nút gập player xuống mini player ─────────────────────────────────────
    MINIMIZE_BTN         = (AppiumBy.ACCESSIBILITY_ID, "Di chuyển lên")
    MINIMIZE_BTN_MORE    = (AppiumBy.ACCESSIBILITY_ID, "Thêm")

    # ── Lyrics view ──────────────────────────────────────────────────────────
    LYRIC_TEXT           = (AppiumBy.ID, "com.zing.mp3:id/tvLyric")
    LYRIC_RECYCLER       = (AppiumBy.ID, "com.zing.mp3:id/rcv")
    PIN_SONG_THUMB       = (AppiumBy.ID, "com.zing.mp3:id/imgPinSongThumb")
    PIN_SONG_TITLE       = (AppiumBy.ID, "com.zing.mp3:id/tvPinSongTitle")
    PIN_SONG_ARTIST      = (AppiumBy.ID, "com.zing.mp3:id/tvPinSongArtist")
    DEEP_LYRIC_BTN       = (AppiumBy.ID, "com.zing.mp3:id/btnDeepLyricTheme")

    # ── Song Info view ────────────────────────────────────────────────────────
    SONG_INFO_ALBUM      = (AppiumBy.ID, "com.zing.mp3:id/tvAlbumTitle")
    SONG_INFO_COMPOSER   = (AppiumBy.ID, "com.zing.mp3:id/tvComposer")
    SONG_INFO_PLAYS      = (AppiumBy.ID, "com.zing.mp3:id/tvPlays")
    SONG_INFO_FAVS       = (AppiumBy.ID, "com.zing.mp3:id/tvFavs")
    SONG_INFO_RELEASE    = (AppiumBy.ID, "com.zing.mp3:id/tvReleaseTitle")
    SONG_INFO_ARTIST_LBL = (AppiumBy.ID, "com.zing.mp3:id/tvArtistTitle")
    SONG_INFO_CATE       = (AppiumBy.ID, "com.zing.mp3:id/tvCateTitle")
    SONG_INFO_DISTRIBUTOR = (AppiumBy.ID, "com.zing.mp3:id/tvDistributorTitle")

    # ── Queue view ────────────────────────────────────────────────────────────
    QUEUE_CLOSE_BTN      = (AppiumBy.ID, "com.zing.mp3:id/btnClose")
    QUEUE_LIST           = (AppiumBy.ID, "com.zing.mp3:id/recyclerView")
    QUEUE_SELECT_BTN     = (AppiumBy.ID, "com.zing.mp3:id/btnSelect")
    QUEUE_TITLE_TOOLBAR  = (AppiumBy.ID, "com.zing.mp3:id/tvTitleToolbar")

    # ── Bottom Sheet (More options) ───────────────────────────────────────────
    BOTTOM_SHEET_SHARE   = (AppiumBy.ID, "com.zing.mp3:id/btnShare")
    BOTTOM_SHEET_TIMER   = (AppiumBy.ID, "com.zing.mp3:id/tvTimer")
    BOTTOM_SHEET_THEME   = (AppiumBy.ID, "com.zing.mp3:id/tvTheme")
    BOTTOM_SHEET_SETTING = (AppiumBy.ID, "com.zing.mp3:id/tvPlayerSetting")
    BOTTOM_SHEET_LAYOUT  = (AppiumBy.ID, "com.zing.mp3:id/themeLayout")

    # ── Reward Ads button ─────────────────────────────────────────────────────
    BTN_REWARD_ADS       = (AppiumBy.ID, "com.zing.mp3:id/btnRewardAds")

    # ── Reward Ads overlay (Ads-Reward scene) ────────────────────────────────
    # Xuất hiện khi user non-premium trigger reward ad — chặn toàn bộ Player UI
    ADS_REWARD_LAYOUT    = (AppiumBy.ID, "com.zing.mp3:id/layoutCountdown")
    ADS_REWARD_CTA_BTN   = (AppiumBy.ID, "com.zing.mp3:id/btnCta")

    # ── Lossless quality bottom sheet (Bts-Lossless scene) ───────────────────
    # Xuất hiện với Free/Plus khi mở bài có Lossless — hỏi có muốn nghe thử không
    BTS_LOSSLESS_LAYOUT  = (AppiumBy.ID, "com.zing.mp3:id/design_bottom_sheet")
    BTS_LOSSLESS_TRY     = (AppiumBy.ID, "com.zing.mp3:id/btnPrimary")    # "NGHE THỬ LOSSLESS"
    BTS_LOSSLESS_LATER   = (AppiumBy.ID, "com.zing.mp3:id/btnNegative")   # "ĐỂ SAU"

    # ── App Theme bottom sheet (Bts-AppTheme scene) ───────────────────────
    # Xuất hiện khi app gợi ý chọn chủ đề giao diện — title "Chọn chủ đề" + nút X
    BTS_APP_THEME_TITLE  = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/title' and @text='Chọn chủ đề']")
    BTS_APP_THEME_CLOSE  = (AppiumBy.ID, "com.zing.mp3:id/btnClose")

    # ── Download bottom sheet ─────────────────────────────────────────────────
    DOWNLOAD_BTN         = (AppiumBy.ID, "com.zing.mp3:id/btnDownload")
    DOWNLOAD_128         = (AppiumBy.ID, "com.zing.mp3:id/download128")
    DOWNLOAD_320         = (AppiumBy.ID, "com.zing.mp3:id/download320")
    DOWNLOAD_LL          = (AppiumBy.ID, "com.zing.mp3:id/downloadLl")
    DOWNLOAD_REMEMBER    = (AppiumBy.ID, "com.zing.mp3:id/cbRemember")

    # ── Add to Playlist ───────────────────────────────────────────────────────
    ADD_PLAYLIST_SEARCH  = (AppiumBy.ID, "com.zing.mp3:id/etSearchBar")
    ADD_PLAYLIST_LIST    = (AppiumBy.ID, "com.zing.mp3:id/recyclerView")


class AndroidPlaylistLocators:
    # ── Header thông tin playlist ─────────────────────────────────────────────
    COVER_IMAGE          = (AppiumBy.ID, "com.zing.mp3:id/imgThumb")
    PLAYLIST_TITLE       = (AppiumBy.ID, "com.zing.mp3:id/tvTitle")
    HEADER_ARTIST        = (AppiumBy.ID, "com.zing.mp3:id/tvHeaderArtist")     # "Zing MP3" / tên tác giả
    SONG_COUNT_DURATION  = (AppiumBy.ID, "com.zing.mp3:id/tvSubTitle")          # "100 bài hát • 7 giờ 25 phút"
    DESCRIPTION          = (AppiumBy.ID, "com.zing.mp3:id/tvDescription")

    # ── Nút hành động ────────────────────────────────────────────────────────
    BTN_SHUFFLE          = (AppiumBy.ID, "com.zing.mp3:id/btnShuffle")         # "PHÁT NGẪU NHIÊN"
    BTN_DOWNLOAD         = (AppiumBy.ID, "com.zing.mp3:id/btnDownload")        # "Tải xuống"
    BTN_FAV              = (AppiumBy.ID, "com.zing.mp3:id/btnFav")
    TV_FAV               = (AppiumBy.ID, "com.zing.mp3:id/tvFav")              # "Thích"
    MENU_MORE            = (AppiumBy.ID, "com.zing.mp3:id/menu_more")
    BTN_PLAY_PAUSE       = (AppiumBy.ID, "com.zing.mp3:id/btnPlayPause")

    # ── Nút thêm bài (User playlist) ─────────────────────────────────────────
    BTN_ADD_SONG         = (AppiumBy.ID, "com.zing.mp3:id/btnAddSong")

    # ── Danh sách bài hát ────────────────────────────────────────────────────
    SONG_LIST            = (AppiumBy.ID, "com.zing.mp3:id/recyclerView")
    FIRST_SONG_TITLE     = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle'])[1]")
    FIRST_SONG_ARTIST    = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvArtist'])[1]")
    FIRST_SONG_MENU_BTN  = (AppiumBy.XPATH,
        "(//android.widget.ImageButton[@resource-id='com.zing.mp3:id/btnMenu'])[1]")
    DOWNLOAD_INDICATOR   = (AppiumBy.ID, "com.zing.mp3:id/downloadIndicator")

    # ── CTA header / promotion ────────────────────────────────────────────────
    CTA_HEADER           = (AppiumBy.ID, "com.zing.mp3:id/cta_header")


class AndroidProfileLocators:
    # ── Header ───────────────────────────────────────────────────────────────
    PAGE_TITLE           = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/text' and @text='Cá nhân']")
    AVATAR               = (AppiumBy.ID, "com.zing.mp3:id/imgAvatar")
    BG_IMAGE             = (AppiumBy.ID, "com.zing.mp3:id/imgBg")
    IV_BADGE             = (AppiumBy.ID, "com.zing.mp3:id/ivBadge")

    # ── Non-login state ───────────────────────────────────────────────────────
    BTN_LOGIN            = (AppiumBy.ID, "com.zing.mp3:id/tvLogin")            # "ĐĂNG NHẬP"

    # ── Logged-in state ───────────────────────────────────────────────────────
    USER_NAME            = (AppiumBy.ID, "com.zing.mp3:id/tvName")
    USER_BADGE           = (AppiumBy.ID, "com.zing.mp3:id/layoutUserBadge")
    BTN_MANAGE_PLAN      = (AppiumBy.ID, "com.zing.mp3:id/tvMyHistory")        # "Quản lý gói đã dùng"
    BTN_ENTER_CODE       = (AppiumBy.ID, "com.zing.mp3:id/tvSetting")          # "Nhập Code"
    PLAN_COUNTDOWN       = (AppiumBy.ID, "com.zing.mp3:id/tvCountDown")        # "Kết thúc sau X ngày"
    LAYOUT_MANAGE_ACTIONS = (AppiumBy.ID, "com.zing.mp3:id/layoutManageActions")

    # ── Premium upsell card ───────────────────────────────────────────────────
    UPSELL_CARD          = (AppiumBy.ID, "com.zing.mp3:id/layoutRoot")
    UPSELL_PRICE         = (AppiumBy.ID, "com.zing.mp3:id/tvPromote")          # "Chỉ 15.000đ/tháng"
    UPSELL_DESC          = (AppiumBy.ID, "com.zing.mp3:id/tvDesc")
    BENEFIT_NO_ADS       = (AppiumBy.ID, "com.zing.mp3:id/tvBenefit1")         # "Loại bỏ toàn bộ quảng cáo"
    BENEFIT_DOWNLOAD     = (AppiumBy.ID, "com.zing.mp3:id/tvBenefit2")         # "Tải nhạc không giới hạn"
    BENEFIT_ORDER_PLAY   = (AppiumBy.ID, "com.zing.mp3:id/tvBenefit3")         # "Phát nhạc theo thứ tự"
    ADVANCED_FEATURE     = (AppiumBy.ID, "com.zing.mp3:id/tvPromoteFeature")   # "Trải nghiệm nâng cao"
    FEATURE_THEME        = (AppiumBy.ID, "com.zing.mp3:id/tvPromoteFeature1")  # "Tùy chỉnh giao diện"
    FEATURE_LOSSLESS     = (AppiumBy.ID, "com.zing.mp3:id/tvPromoteFeature2")  # "Âm thanh vượt trội (Lossless)"

    # ── Danh sách menu trong profile ─────────────────────────────────────────
    RECYCLER_VIEW        = (AppiumBy.ID, "com.zing.mp3:id/recyclerView")
    TV_TITLE             = (AppiumBy.ID, "com.zing.mp3:id/tvTitle")
    SWIPE_REFRESH        = (AppiumBy.ID, "com.zing.mp3:id/swipeRefreshLayout")


class AndroidChartLocators:
    # ── ZingChart main screen ────────────────────────────────────────────────
    ZING_CHART_VIEW      = (AppiumBy.ID,   "com.zing.mp3:id/zingChart")        # widget biểu đồ
    CHART_DATE_TIME      = (AppiumBy.ID,   "com.zing.mp3:id/tvZingChartDateTime")
    CHART_SUGGESTION     = (AppiumBy.ID,   "com.zing.mp3:id/tvSuggestion")
    IMG_SUGGESTION       = (AppiumBy.ID,   "com.zing.mp3:id/imgSuggestion")
    BTN_FAST_PLAY        = (AppiumBy.ID,   "com.zing.mp3:id/btnFastPlay")      # "Phát nhanh"

    # ── Danh sách bài hát chart ───────────────────────────────────────────────
    CHART_TOP1_ROW       = (AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.zing.mp3:id/tvRank' and @text='1']"
        "/ancestor::android.widget.LinearLayout[@clickable='true']")
    CHART_TOP1_THUMB     = (AppiumBy.XPATH,
        "(//android.widget.ImageView[@resource-id='com.zing.mp3:id/imgThumb'])[1]")
    CHART_TOP1_TITLE     = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvTitle'])[1]")
    CHART_TOP1_ARTIST    = (AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.zing.mp3:id/tvArtist'])[1]")
    CHART_RANK           = (AppiumBy.ID,   "com.zing.mp3:id/tvRank")
    CHART_CHANGE         = (AppiumBy.ID,   "com.zing.mp3:id/tvChange")
    CHART_SONG_LIST      = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")

    # ── Weekly chart tabs (V-pop, US-UK, K-pop) ──────────────────────────────
    CHART_WEEK_TABS      = (AppiumBy.ID,   "com.zing.mp3:id/viewPager")
    TAB_VPOP             = (AppiumBy.ACCESSIBILITY_ID, "V-pop")
    TAB_USUK             = (AppiumBy.ACCESSIBILITY_ID, "US-UK")
    TAB_KPOP             = (AppiumBy.ACCESSIBILITY_ID, "K-pop")
    BTN_CHART_WEEK       = (AppiumBy.ID,   "com.zing.mp3:id/btnChartWeek")
    TV_CHART_WEEK        = (AppiumBy.ID,   "com.zing.mp3:id/tvChartWeek")
    TV_ZING_CHART_TITLE  = (AppiumBy.ID,   "com.zing.mp3:id/tvZingChartTitle")

    # ── Shuffle / Actions ─────────────────────────────────────────────────────
    BTN_SHUFFLE          = (AppiumBy.ID,   "com.zing.mp3:id/btnShuffle")
    LAYOUT_CHART_HEADER  = (AppiumBy.ID,   "com.zing.mp3:id/layoutChartHeader")


class AndroidChartDetailLocators:
    """Màn hình chi tiết chart (chart-HCM, chart-HN) — dạng collapsing toolbar"""
    COLLAPSING_TOOLBAR   = (AppiumBy.ID,   "com.zing.mp3:id/collapsingToolbar")
    COVER_IMAGE          = (AppiumBy.ID,   "com.zing.mp3:id/imgCover")
    TV_HEADER            = (AppiumBy.ID,   "com.zing.mp3:id/tvHeader")
    SONG_LIST            = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    BTN_SHUFFLE          = (AppiumBy.ID,   "com.zing.mp3:id/btnShuffle")
    SONG_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    SONG_ARTIST          = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    SONG_RANK            = (AppiumBy.ID,   "com.zing.mp3:id/tvRank")
    SONG_CHANGE          = (AppiumBy.ID,   "com.zing.mp3:id/tvChange")
    BTN_MORE             = (AppiumBy.ID,   "com.zing.mp3:id/more")
    BTN_SONG_MENU        = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")


class AndroidRadioLocators:
    # ── Màn hình Radio — danh sách kênh ─────────────────────────────────────
    SEARCH_BTN           = (AppiumBy.ID,   "com.zing.mp3:id/search")
    RADIO_LIST           = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    RADIO_ITEM_VIEW      = (AppiumBy.ID,   "com.zing.mp3:id/radioItemView")
    RADIO_BG             = (AppiumBy.ID,   "com.zing.mp3:id/radioBg")
    RADIO_PROGRESS       = (AppiumBy.ID,   "com.zing.mp3:id/radioProgress")
    IV_CHANNEL_THUMB     = (AppiumBy.ID,   "com.zing.mp3:id/ivChannelThumb")
    IV_PROGRAM_THUMB     = (AppiumBy.ID,   "com.zing.mp3:id/ivProgramThumb")
    IV_PLAY_RADIO        = (AppiumBy.ID,   "com.zing.mp3:id/ivPlayRadio")
    TV_RADIO_TITLE       = (AppiumBy.ID,   "com.zing.mp3:id/tvRadioTitle")
    TV_PROGRAM_INFO      = (AppiumBy.ID,   "com.zing.mp3:id/tvProgramInfo")
    TV_VIEWER            = (AppiumBy.ID,   "com.zing.mp3:id/tvViewer")
    TV_OPEN_SCHEDULE     = (AppiumBy.ID,   "com.zing.mp3:id/tvOpenRadioSchedule")
    IV_VIEWER            = (AppiumBy.ID,   "com.zing.mp3:id/ivViewer")
    TAG_CONTAINER        = (AppiumBy.ID,   "com.zing.mp3:id/containerTagRadio")
    IC_LIVE_TAG          = (AppiumBy.ID,   "com.zing.mp3:id/icLiveTag")
    SWIPE_REFRESH        = (AppiumBy.ID,   "com.zing.mp3:id/swipeRefreshLayout")

    # ── Radio Player ─────────────────────────────────────────────────────────
    RADIO_LAYOUT         = (AppiumBy.ID,   "com.zing.mp3:id/radioLayout")
    RADIO_PLAYER_THUMB   = (AppiumBy.ID,   "com.zing.mp3:id/ivThumb")
    RADIO_PLAYER_NAME    = (AppiumBy.ID,   "com.zing.mp3:id/tvName")
    RADIO_PLAYER_TITLE   = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    RADIO_PLAYER_SUBTITLE = (AppiumBy.ID,  "com.zing.mp3:id/tvSubTitle")
    RADIO_PLAYER_TAG     = (AppiumBy.ID,   "com.zing.mp3:id/tvTag")
    RADIO_PLAYER_INFO    = (AppiumBy.ID,   "com.zing.mp3:id/tvInfo")
    BTN_FOLLOW           = (AppiumBy.ID,   "com.zing.mp3:id/btnFollow")
    BTN_REACTION         = (AppiumBy.ID,   "com.zing.mp3:id/btnReaction")
    REACTION_COUNT       = (AppiumBy.ID,   "com.zing.mp3:id/reactionCount")
    VIEWER_COUNT         = (AppiumBy.ID,   "com.zing.mp3:id/viewerCount")
    LIVE_INDICATOR       = (AppiumBy.ID,   "com.zing.mp3:id/liveIndicator")
    IV_CLOSE             = (AppiumBy.ID,   "com.zing.mp3:id/ivClose")
    IV_CLOSE_TOOLBAR     = (AppiumBy.ID,   "com.zing.mp3:id/ivCloseToolbar")
    IV_MORE_TOOLBAR      = (AppiumBy.ID,   "com.zing.mp3:id/ivMoreToolbar")
    TV_JOIN              = (AppiumBy.ID,   "com.zing.mp3:id/tvJoin")
    EDT_MESSAGE          = (AppiumBy.ID,   "com.zing.mp3:id/edtMessage")
    COMMENT_CONTAINER    = (AppiumBy.ID,   "com.zing.mp3:id/commentContainer")
    PIN_RECYCLER         = (AppiumBy.ID,   "com.zing.mp3:id/pinRecyclerView")
    IV_HEART             = (AppiumBy.ID,   "com.zing.mp3:id/ivHeart")
    THUMBNAIL_VIEW       = (AppiumBy.ID,   "com.zing.mp3:id/thumbnailView")


class AndroidMyMusicLocators:
    # ── Màn hình Thư viện (Thư viện/Library) ─────────────────────────────────
    TOOLBAR              = (AppiumBy.ID,   "com.zing.mp3:id/toolbar")
    SEARCH_BTN           = (AppiumBy.ID,   "com.zing.mp3:id/search")
    TABS                 = (AppiumBy.ID,   "com.zing.mp3:id/tabs")             # tab Playlist / Album
    VIEW_PAGER           = (AppiumBy.ID,   "com.zing.mp3:id/viewPagerPlaylist")
    RECENT_HEADER        = (AppiumBy.ID,   "com.zing.mp3:id/llRecentHeader")
    TV_RECENT            = (AppiumBy.ID,   "com.zing.mp3:id/tvRecent")
    RECENT_RECYCLER      = (AppiumBy.ID,   "com.zing.mp3:id/recentRecyclerView")
    RECYCLER_VIEW        = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    TV_COUNT             = (AppiumBy.ID,   "com.zing.mp3:id/tvCount")
    IMG_MORE             = (AppiumBy.ID,   "com.zing.mp3:id/imgMore")

    # ── Tab Playlist / Album (accessibility) ────────────────────────────────
    TAB_PLAYLIST         = (AppiumBy.ACCESSIBILITY_ID, "Playlist")
    TAB_ALBUM            = (AppiumBy.ACCESSIBILITY_ID, "Album")

    # ── Non-login prompt ──────────────────────────────────────────────────────
    TV_CLOSE_AD         = (AppiumBy.ID,   "com.zing.mp3:id/tvCloseAd")
    BTN_CLOSE_AD        = (AppiumBy.ID,   "com.zing.mp3:id/btnCloseAd")

    # ── Downloaded music section ──────────────────────────────────────────────
    BG_HEADER            = (AppiumBy.ID,   "com.zing.mp3:id/bgHeader")
    COLLAPSING_TOOLBAR   = (AppiumBy.ID,   "com.zing.mp3:id/collapsingToolbar")
    DETAIL_HEADER        = (AppiumBy.ID,   "com.zing.mp3:id/detail_header")
    BTN_PLAY_PAUSE       = (AppiumBy.ID,   "com.zing.mp3:id/btnPlayPause")
    BTN_SHUFFLE          = (AppiumBy.ID,   "com.zing.mp3:id/btnShuffle")
    BTN_PLAY             = (AppiumBy.ID,   "com.zing.mp3:id/btnPlay")
    TAB_LAYOUT           = (AppiumBy.ID,   "com.zing.mp3:id/tabLayout")
    MENU_SEARCH          = (AppiumBy.ID,   "com.zing.mp3:id/menu_search")
    MENU_MORE            = (AppiumBy.ID,   "com.zing.mp3:id/menu_more")
    MENU_DOWNLOAD        = (AppiumBy.ID,   "com.zing.mp3:id/menu_download")

    # ── Filter / Sort ─────────────────────────────────────────────────────────
    IMG_FILTER           = (AppiumBy.ID,   "com.zing.mp3:id/imgFilter")
    TV_FILTER            = (AppiumBy.ID,   "com.zing.mp3:id/tvFilter")
    TV_SORT              = (AppiumBy.ID,   "com.zing.mp3:id/tvSort")
    LL_FILTER            = (AppiumBy.ID,   "com.zing.mp3:id/llFilter")

    # ── Song list items ───────────────────────────────────────────────────────
    SONG_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    SONG_ARTIST          = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    SONG_SUBTITLE        = (AppiumBy.ID,   "com.zing.mp3:id/tvSubTitle")
    SONG_THUMB           = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    SONG_INDICATOR       = (AppiumBy.ID,   "com.zing.mp3:id/songIndicator")
    SONG_MENU            = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")

    # ── Error / empty state ───────────────────────────────────────────────────
    ERR_ICON             = (AppiumBy.ID,   "com.zing.mp3:id/errIcon")
    ERR_TITLE            = (AppiumBy.ID,   "com.zing.mp3:id/errTitle")
    ERR_MSG              = (AppiumBy.ID,   "com.zing.mp3:id/errMsg")

    # ── MySong (Bài hát của tôi) ──────────────────────────────────────────────
    SYNC_VIEW            = (AppiumBy.ID,   "com.zing.mp3:id/syncView")


class AndroidArtistLocators:
    # ── Header (collapsing) ───────────────────────────────────────────────────
    APP_BAR              = (AppiumBy.ID,   "com.zing.mp3:id/appBar")
    COLLAPSING_TOOLBAR   = (AppiumBy.ID,   "com.zing.mp3:id/collapsingToolbar")
    COVER_LAYOUT         = (AppiumBy.ID,   "com.zing.mp3:id/coverLayout")
    IMG_COVER            = (AppiumBy.ID,   "com.zing.mp3:id/imgCover")
    INFO_HEADER          = (AppiumBy.ID,   "com.zing.mp3:id/info_header")
    TV_FOLLOWER_NUMB     = (AppiumBy.ID,   "com.zing.mp3:id/tvFollowerNumb")   # "1.2M người theo dõi"
    BTN_FOLLOW           = (AppiumBy.ID,   "com.zing.mp3:id/btnFollow")
    BTN_PLAY             = (AppiumBy.ID,   "com.zing.mp3:id/btnPlay")
    BTN_MORE             = (AppiumBy.ID,   "com.zing.mp3:id/btnMore")
    MENU_MORE            = (AppiumBy.ID,   "com.zing.mp3:id/menu_more")
    TV_MORE              = (AppiumBy.ID,   "com.zing.mp3:id/tvMore")

    # ── Content ──────────────────────────────────────────────────────────────
    WRAP_VIEW_PAGER      = (AppiumBy.ID,   "com.zing.mp3:id/wrapViewPager")
    RECYCLER_VIEW        = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    SONG_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    SONG_ARTIST          = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    SONG_THUMB           = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    SONG_MENU_BTN        = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")
    SWIPE_REFRESH        = (AppiumBy.ID,   "com.zing.mp3:id/swipeRefreshLayout")

    # ── More button (accessibility) ───────────────────────────────────────────
    MORE_BTN_ACC         = (AppiumBy.ACCESSIBILITY_ID, "Thêm")


class AndroidSettingsLocators:
    # ── Toolbar ──────────────────────────────────────────────────────────────
    TOOLBAR_TITLE        = (AppiumBy.ID,   "com.zing.mp3:id/tvToolbarTitle")   # "Cài đặt"
    SCROLL_VIEW          = (AppiumBy.ID,   "com.zing.mp3:id/scrollView")

    # ── Setting items ─────────────────────────────────────────────────────────
    SETTING_DOWNLOAD     = (AppiumBy.ID,   "com.zing.mp3:id/settingDownload")
    SETTING_PLAYER       = (AppiumBy.ID,   "com.zing.mp3:id/settingPlayer")
    SETTING_NOTIFICATION = (AppiumBy.ID,   "com.zing.mp3:id/settingNotification")
    SETTING_HEADSET      = (AppiumBy.ID,   "com.zing.mp3:id/settingHeadset")
    SETTING_VIDEO        = (AppiumBy.ID,   "com.zing.mp3:id/settingVideo")
    SETTING_LIBRARY      = (AppiumBy.ID,   "com.zing.mp3:id/settingLibrary")
    SETTING_THEME_LAYOUT = (AppiumBy.ID,   "com.zing.mp3:id/settingThemeLayout")
    SETTING_VERSION      = (AppiumBy.ID,   "com.zing.mp3:id/settingVersion")
    TV_SETTING_THEME     = (AppiumBy.ID,   "com.zing.mp3:id/tvSettingTheme")
    IV_ARROW_THEME       = (AppiumBy.ID,   "com.zing.mp3:id/ivArrowTheme")
    IV_BADGE_THEME       = (AppiumBy.ID,   "com.zing.mp3:id/ivBadgeTheme")
    IV_ICON_THEME        = (AppiumBy.ID,   "com.zing.mp3:id/ivIconTheme")

    # ── Other section ─────────────────────────────────────────────────────────
    RATE_ME              = (AppiumBy.ID,   "com.zing.mp3:id/rateMe")
    FEEDBACK_REPORT      = (AppiumBy.ID,   "com.zing.mp3:id/feedbackAndReport")
    ABOUT_US             = (AppiumBy.ID,   "com.zing.mp3:id/aboutUs")
    PRIVACY              = (AppiumBy.ID,   "com.zing.mp3:id/privacy")
    TERMS                = (AppiumBy.ID,   "com.zing.mp3:id/terms")
    VERSION              = (AppiumBy.ID,   "com.zing.mp3:id/version")
    TV_VERSION           = (AppiumBy.ID,   "com.zing.mp3:id/tvVersion")

    # ── Logged-in only ────────────────────────────────────────────────────────
    LOGOUT               = (AppiumBy.ID,   "com.zing.mp3:id/logout")
    OTHER_SECTION        = (AppiumBy.ID,   "com.zing.mp3:id/other")


class AndroidNotiLocators:
    # ── Toolbar ──────────────────────────────────────────────────────────────
    TOOLBAR_TITLE        = (AppiumBy.ID,   "com.zing.mp3:id/tvToolbarTitle")   # "Thông báo"

    # ── Danh sách thông báo ───────────────────────────────────────────────────
    NOTI_LIST            = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    SWIPE_REFRESH        = (AppiumBy.ID,   "com.zing.mp3:id/swipeRefreshLayout")
    NOTI_THUMB           = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    NOTI_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    NOTI_CONTENT         = (AppiumBy.ID,   "com.zing.mp3:id/tvContent")


class AndroidSubscriptionLocators:
    # ── Danh sách gói ────────────────────────────────────────────────────────
    PACKAGE_LIST         = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    BTN_CLOSE            = (AppiumBy.ID,   "com.zing.mp3:id/btnClose")
    BTN_BUY              = (AppiumBy.ID,   "com.zing.mp3:id/btnBuy")
    TV_PACKAGE_NAME      = (AppiumBy.ID,   "com.zing.mp3:id/tvPackageName")
    TV_PACKAGE_DESC      = (AppiumBy.ID,   "com.zing.mp3:id/tvPackageDesc")
    TV_PRICE             = (AppiumBy.ID,   "com.zing.mp3:id/tvPrice")
    COLLAPSING_TOOLBAR   = (AppiumBy.ID,   "com.zing.mp3:id/collapsingToolbar")
    IMG_COVER            = (AppiumBy.ID,   "com.zing.mp3:id/imgCover")
    IMG_BADGE            = (AppiumBy.ID,   "com.zing.mp3:id/imgBadge")

    # ── Chi tiết gói (Plus / Premium) ────────────────────────────────────────
    BTN_BOTTOM_CTA       = (AppiumBy.ID,   "com.zing.mp3:id/btnBottomCta")
    TV_BADGE             = (AppiumBy.ID,   "com.zing.mp3:id/tvBadge")
    TV_TITLE             = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    TV_SUBTITLE          = (AppiumBy.ID,   "com.zing.mp3:id/tvSubTitle")
    TV_DEAL              = (AppiumBy.ID,   "com.zing.mp3:id/tvDeal")
    TV_ORIGINAL_PRICE    = (AppiumBy.ID,   "com.zing.mp3:id/tvOriginalPrice")
    TV_BOTTOM_DESC       = (AppiumBy.ID,   "com.zing.mp3:id/tvBottomDesc")
    TAB_LAYOUT           = (AppiumBy.ID,   "com.zing.mp3:id/tabLayout")
    WRAP_VIEW_PAGER      = (AppiumBy.ID,   "com.zing.mp3:id/wrapViewPager")

    # ── Tab Plus / Premium ────────────────────────────────────────────────────
    TAB_PLUS             = (AppiumBy.ACCESSIBILITY_ID, "Plus")
    TAB_PREMIUM          = (AppiumBy.ACCESSIBILITY_ID, "Premium")


class AndroidRecentLocators:
    """Màn hình Nghe gần đây — các tab Bài hát / Playlist / Nghệ sĩ / MV / Phòng nhạc"""

    # ── Toolbar ──────────────────────────────────────────────────────────────
    TOOLBAR_TITLE        = (AppiumBy.ID,   "com.zing.mp3:id/tvToolbarTitle")

    # ── Tabs ─────────────────────────────────────────────────────────────────
    TABS                 = (AppiumBy.ID,   "com.zing.mp3:id/wrapViewPager")
    TAB_BAI_HAT          = (AppiumBy.ACCESSIBILITY_ID, "Bài hát")
    TAB_PLAYLIST         = (AppiumBy.ACCESSIBILITY_ID, "Playlist")
    TAB_NGHE_SI          = (AppiumBy.ACCESSIBILITY_ID, "Nghệ sĩ")
    TAB_MV               = (AppiumBy.ACCESSIBILITY_ID, "MV")
    TAB_PHONG_NHAC       = (AppiumBy.ACCESSIBILITY_ID, "Phòng nhạc")

    # ── Danh sách ────────────────────────────────────────────────────────────
    RECYCLER_VIEW        = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    SONG_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    SONG_ARTIST          = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    SONG_THUMB           = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    SONG_MENU            = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")
    BTN_SHUFFLE          = (AppiumBy.ID,   "com.zing.mp3:id/btnShuffle")
    MENU_MORE            = (AppiumBy.ID,   "com.zing.mp3:id/menu_more")
    DOWNLOAD_INDICATOR   = (AppiumBy.ID,   "com.zing.mp3:id/downloadIndicator")

    # ── Nghệ sĩ ───────────────────────────────────────────────────────────────
    ARTIST_SUBTITLE      = (AppiumBy.ID,   "com.zing.mp3:id/tvSubtitle")
    BTN_FOLLOW           = (AppiumBy.ID,   "com.zing.mp3:id/btnFollow")

    # ── MV ────────────────────────────────────────────────────────────────────
    MV_DURATION          = (AppiumBy.ID,   "com.zing.mp3:id/tvDuration")


class AndroidNewReleaseLocators:
    """Màn hình Nhạc mới (NewRelease — Bài hát / Album)"""

    # ── Toolbar ──────────────────────────────────────────────────────────────
    TOOLBAR_TITLE        = (AppiumBy.ID,   "com.zing.mp3:id/tvToolbarTitle")

    # ── Tabs ─────────────────────────────────────────────────────────────────
    WRAP_VIEW_PAGER      = (AppiumBy.ID,   "com.zing.mp3:id/wrapViewPager")
    TAB_BAI_HAT          = (AppiumBy.ACCESSIBILITY_ID, "Bài hát")
    TAB_ALBUM            = (AppiumBy.ACCESSIBILITY_ID, "Album")

    # ── Filter tabs (Tất cả / Việt Nam / Âu Mỹ / Hàn Quốc) ──────────────────
    TAB_TAT_CA           = (AppiumBy.ACCESSIBILITY_ID, "Tất cả")
    TAB_VIET_NAM         = (AppiumBy.ACCESSIBILITY_ID, "Việt Nam")
    TAB_AU_MY            = (AppiumBy.ACCESSIBILITY_ID, "Âu Mỹ")
    TAB_HAN_QUOC         = (AppiumBy.ACCESSIBILITY_ID, "Hàn Quốc")

    # ── Danh sách ────────────────────────────────────────────────────────────
    RECYCLER_VIEW        = (AppiumBy.ID,   "com.zing.mp3:id/recyclerView")
    SONG_TITLE           = (AppiumBy.ID,   "com.zing.mp3:id/tvTitle")
    SONG_ARTIST          = (AppiumBy.ID,   "com.zing.mp3:id/tvArtist")
    SONG_THUMB           = (AppiumBy.ID,   "com.zing.mp3:id/imgThumb")
    SONG_MENU            = (AppiumBy.ID,   "com.zing.mp3:id/btnMenu")
    BTN_SHUFFLE          = (AppiumBy.ID,   "com.zing.mp3:id/btnShuffle")
    RELEASE_DATE         = (AppiumBy.ID,   "com.zing.mp3:id/tvReleaseDate")
    IMG_DOT              = (AppiumBy.ID,   "com.zing.mp3:id/imgDot")           # chấm "mới"


class AndroidKikiLocators:
    """Màn hình Kiki (nhận dạng giọng nói)"""
    MAIN_CONTAINER       = (AppiumBy.ID,   "com.zing.mp3:id/kiki_main_container_view")
    MICRO_BTN            = (AppiumBy.ID,   "com.zing.mp3:id/kiki_main_micro")
    MIC_CLICK_FIELD      = (AppiumBy.ID,   "com.zing.mp3:id/kiki_mic_click_field")
    COMPOUND_MIC         = (AppiumBy.ID,   "com.zing.mp3:id/kiki_main_compound_mic")
    EXIT_BTN             = (AppiumBy.ID,   "com.zing.mp3:id/kiki_main_frag_exit")
    RESULT_CONTAINER     = (AppiumBy.ID,   "com.zing.mp3:id/kiki_result_text_container")
    GUIDELINE_TITLE      = (AppiumBy.ID,   "com.zing.mp3:id/kiki_guideline_title")
    GUIDELINE_DETAIL     = (AppiumBy.ID,   "com.zing.mp3:id/kiki_guideline_detail")
    REPORT_ERROR         = (AppiumBy.ID,   "com.zing.mp3:id/kiki_report_error")
    PWR_TEXT             = (AppiumBy.ID,   "com.zing.mp3:id/kiki_main_frag_pwr_txt")