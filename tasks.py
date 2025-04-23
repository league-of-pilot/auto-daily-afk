from screen_utils import match_template
import pyautogui

def run_task(name, img):
    if name == "close_overlay":
        pyautogui.click(50, 50)  # click 1 góc để đóng
    elif name == "go_home":
        found, center = match_template(img, "templates/home_icon.png")
        if found:
            pyautogui.click(center)
    elif name == "click_daily_quest":
        found, center = match_template(img, "templates/daily_btn.png")
        if found:
            pyautogui.click(center)
