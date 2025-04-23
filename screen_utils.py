import cv2
import numpy as np
import pyautogui

TEMPLATE_THRESHOLD = 0.85

def take_screenshot():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def match_template(img, template_path):
    template = cv2.imread(template_path, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if max_val > TEMPLATE_THRESHOLD:
        h, w = template.shape
        center = (max_loc[0] + w//2, max_loc[1] + h//2)
        return True, center
    return False, None

def detect_screen_state(img):
    checks = {
        "home": "templates/home_icon.png",
        "loading": "templates/loading_icon.png",
        "ads_overlay": "templates/close_x.png",
        "daily_quest_btn": "templates/daily_btn.png"
    }

    for state, path in checks.items():
        found, _ = match_template(img, path)
        if found:
            return state
    return "unknown"
