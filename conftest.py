import os
import time
import subprocess
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_DIR = os.path.join(BASE_DIR, "videos")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# =========================================================
# FFmpeg PATH
# =========================================================

FFMPEG_PATH = (
    r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"
)


# =========================================================
# DRIVER FIXTURE
# =========================================================

@pytest.fixture
def driver():

    print("\n========== DRIVER SETUP ==========")

    chrome_options = Options()

    # Browser visible
    chrome_options.add_argument("--start-maximized")

    # Microphone permission
    chrome_options.add_argument(
        "--use-fake-ui-for-media-stream"
    )

    # Fake microphone device
    chrome_options.add_argument(
        "--use-fake-device-for-media-stream"
    )

    # Selenium stability
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")

    # DO NOT use headless
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.set_window_size(1920, 1080)

    # Open website
    driver.get("https://kordic.io/features.html")

    print("Website opened:")
    print(driver.current_url)

    time.sleep(5)

    yield driver

    print("\n========== DRIVER TEARDOWN ==========")

    try:
        driver.quit()
    except Exception:
        pass


# =========================================================
# VIDEO RECORDING FIXTURE
# =========================================================

@pytest.fixture
def video_recording(driver):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    video_path = os.path.join(
        VIDEO_DIR,
        f"test_{timestamp}.mp4"
    )

    print("\n========== VIDEO RECORDING START ==========")

    print("FFmpeg path:")
    print(FFMPEG_PATH)

    print("Video output path:")
    print(video_path)

    # Verify FFmpeg exists
    if not os.path.exists(FFMPEG_PATH):
        raise FileNotFoundError(
            f"FFmpeg not found at: {FFMPEG_PATH}"
        )

    # Start Windows desktop screen recording
    ffmpeg_process = subprocess.Popen(
        [
            FFMPEG_PATH,

            # Windows desktop capture
            "-f", "gdigrab",

            # Recording FPS
            "-framerate", "15",

            # Show mouse cursor
            "-draw_mouse", "1",

            # Capture entire desktop
            "-i", "desktop",

            # Video codec
            "-c:v", "libx264",

            # Fast encoding for automation
            "-preset", "ultrafast",

            # Compatible MP4
            "-pix_fmt", "yuv420p",

            # Overwrite if file exists
            "-y",

            video_path
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("FFmpeg recording started.")

    # Give FFmpeg a moment to initialize
    time.sleep(2)

    yield video_path

    # =====================================================
    # STOP RECORDING
    # =====================================================

    print("\n========== VIDEO RECORDING STOP ==========")

    try:
        ffmpeg_process.stdin.write(b"q")
        ffmpeg_process.stdin.flush()

        ffmpeg_process.wait(timeout=10)

    except Exception:
        try:
            ffmpeg_process.terminate()
            ffmpeg_process.wait(timeout=5)
        except Exception:
            pass

    # Verify video was created
    if os.path.exists(video_path):

        file_size = os.path.getsize(video_path)

        print("Video recording saved successfully.")
        print(f"Video path: {video_path}")
        print(f"Video size: {file_size / (1024 * 1024):.2f} MB")

    else:

        print("WARNING: Video file was not created.")


# =========================================================
# SCREENSHOT DIRECTORY FIXTURE
# =========================================================

@pytest.fixture
def screenshot_dir():

    return SCREENSHOT_DIR