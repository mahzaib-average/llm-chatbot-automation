import time

from pages.login_page import LoginPage
from utils.screenshot import take_screenshot


def test_start_chat(driver, video_recording):

    print("\n========== TEST START ==========")

    login_page = LoginPage(driver)

    # =========================================================
    # 1. OPEN CHATBOT
    # =========================================================

    print("1. Opening chatbot...")

    login_page.open_chatbot()

    take_screenshot(driver, "01_chatbot_opened")

    # =========================================================
    # 2. NAME
    # =========================================================

    print("7. Entering name...")

    login_page.enter_name("John Doe")

    take_screenshot(driver, "02_name_entered")

    # =========================================================
    # 3. COUNTRY
    # =========================================================

    print("10. Opening country dropdown...")

    login_page.open_country_dropdown()

    print("13. Selecting UAE...")

    login_page.select_uae()

    take_screenshot(driver, "03_uae_selected")

    # =========================================================
    # 4. PHONE
    # =========================================================

    print("17. Entering phone number...")

    login_page.enter_phone("501234567")

    take_screenshot(driver, "04_phone_entered")

    # =========================================================
    # 5. EMAIL
    # =========================================================

    print("20. Entering email...")

    login_page.enter_email("john.doe@example.com")

    take_screenshot(driver, "05_email_entered")

    # =========================================================
    # 6. START CHAT
    # =========================================================

    print("23. Starting chat...")

    login_page.click_start_chat()

    take_screenshot(driver, "06_chat_started")

    # =========================================================
    # 7. TEXT MESSAGE
    # =========================================================

    print("26. Entering Hello message...")

    login_page.enter_message("Hello")

    print("29. Sending Hello message...")

    login_page.send_message()

    time.sleep(3)

    take_screenshot(driver, "07_text_message_sent")

    # =========================================================
    # 8. VOICE RECORDING
    # =========================================================

    print("33. Starting voice recording...")

    login_page.start_recording()

    print("38. Recording for 7 seconds...")

    time.sleep(7)

    print("39. Sending voice recording...")

    login_page.send_recording()

    time.sleep(3)

    take_screenshot(driver, "08_voice_recording_sent")

    # =========================================================
    # 9. END CHAT
    # =========================================================

    print("44. Ending chat...")

    login_page.click_end_chat()

    time.sleep(2)

    take_screenshot(driver, "09_chat_ended")

    # =========================================================
    # 10. STAR RATING
    # =========================================================

    print("48. Selecting 5-star rating...")

    login_page.select_star_rating()

    take_screenshot(driver, "10_five_star_rating")

    # =========================================================
    # 11. FEEDBACK
    # =========================================================

    print("52. Entering feedback...")

    login_page.enter_feedback(
        "The chatbot experience was very good."
    )

    take_screenshot(driver, "11_feedback_entered")

    # =========================================================
    # 12. SUBMIT FEEDBACK
    # =========================================================

    print("55. Submitting feedback...")

    login_page.submit_feedback()

    take_screenshot(driver, "12_feedback_submitted")

    print("\n========== TEST PASSED ==========")

    time.sleep(5)
