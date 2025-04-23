from screen_utils import take_screenshot, detect_screen_state
from tasks import run_task
from log_window import LogWindow
import time

screen_state = None
task_state = None
log = LogWindow()

def log_step(msg):
    log.log(msg)
    print(msg)

while True:
    screenshot = take_screenshot()
    screen_state = detect_screen_state(screenshot)
    log_step(f"[screen] {screen_state}")

    if screen_state == "loading":
        log_step("Waiting for loading to complete...")
        time.sleep(10)
        continue

    if screen_state == "ads_overlay":
        log_step("Detected ad overlay - closing...")
        run_task("close_overlay", screenshot)
        time.sleep(10)
        continue

    if screen_state != "home":
        log_step("Trying to return to home...")
        run_task("go_home", screenshot)
        time.sleep(2)
        continue

    if screen_state == "home":
        if task_state is None:
            task_state = "goto_daily"
            log_step("Navigating to daily quest...")
            run_task("click_daily_quest", screenshot)
            time.sleep(5)
            continue

    time.sleep(1)
