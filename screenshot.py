from pathlib import Path
from datetime import datetime


def take_screenshot(driver, name):
    """
    Takes a screenshot of the current browser.
    """

    date_folder = datetime.now().strftime("%Y-%m-%d")

    screenshot_dir = Path("screenshots") / date_folder
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%H-%M-%S")

    file_path = screenshot_dir / f"{timestamp}_{name}.png"

    driver.save_screenshot(str(file_path))

    print(f"Screenshot saved: {file_path}")

    return file_path