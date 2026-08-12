import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # =========================================================
    # OPEN CHATBOT
    # =========================================================

    def open_chatbot(self):

        print("1. Clicking chatbot button...")

        self.driver.switch_to.default_content()

        chatbot_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/button")
            )
        )

        chatbot_button.click()

        print("2. Waiting for chatbot iframe...")

        iframe = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "iframe[src*='widget.gacs.kordic.io']"
                )
            )
        )

        print("3. Iframe FOUND!")
        print("   Iframe src:", iframe.get_attribute("src"))

        self.driver.switch_to.frame(iframe)

        print("4. Switched inside iframe!")

        self.wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        time.sleep(2)

        print("5. Chatbot UI is ready!")

    # =========================================================
    # ENTER NAME
    # =========================================================

    def enter_name(self, name):

        print("6. Entering name...")

        name_input = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[contains(translate(@placeholder,'NAME','name'),'name')]"
                )
            )
        )

        name_input.clear()
        name_input.send_keys(name)

        print("7. Name entered successfully!")

    # =========================================================
    # OPEN COUNTRY DROPDOWN
    # =========================================================

    def open_country_dropdown(self):

        print("8. Opening country dropdown...")

        # First try buttons that contain an image/flag.
        locators = [

            (
                By.XPATH,
                "//button[.//img]"
            ),

            (
                By.XPATH,
                "//button[contains(@class,'cursor-pointer') and .//svg]"
            ),

            (
                By.XPATH,
                "//button[contains(@class,'rounded') and .//img]"
            ),

            (
                By.XPATH,
                "//button[contains(@class,'flex') and .//img]"
            ),

            (
                By.XPATH,
                "//div[.//img]/button"
            )
        ]

        dropdown = None

        for locator in locators:

            try:

                elements = self.driver.find_elements(*locator)

                for element in elements:

                    try:

                        if element.is_displayed() and element.is_enabled():

                            dropdown = element
                            break

                    except Exception:
                        continue

                if dropdown is not None:
                    break

            except Exception:
                continue

        if dropdown is None:

            print("Country dropdown button was not found.")

            # Diagnostic information
            print("Visible buttons:")

            buttons = self.driver.find_elements(By.TAG_NAME, "button")

            for index, button in enumerate(buttons):

                try:

                    if button.is_displayed():

                        print(
                            index,
                            "| text:",
                            button.text,
                            "| title:",
                            button.get_attribute("title"),
                            "| aria:",
                            button.get_attribute("aria-label")
                        )

                except Exception:
                    pass

            raise Exception(
                "Country dropdown button could not be located."
            )

        print("9. Country dropdown button FOUND!")

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            dropdown
        )

        time.sleep(0.5)

        try:
            dropdown.click()

        except Exception:

            ActionChains(self.driver) \
                .move_to_element(dropdown) \
                .click() \
                .perform()

        print("10. Country dropdown opened!")

        time.sleep(1)

    # =========================================================
    # SELECT UAE
    # =========================================================

    def select_uae(self):

        print("11. Selecting United Arab Emirates...")

        uae = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='United Arab Emirates']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            uae
        )

        time.sleep(0.5)

        try:
            uae.click()

        except Exception:

            ActionChains(self.driver) \
                .move_to_element(uae) \
                .click() \
                .perform()

        print("12. United Arab Emirates selected!")

    # =========================================================
    # ENTER PHONE
    # =========================================================

    def enter_phone(self, phone):

        print("13. Entering UAE phone number...")

        phone_input = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[@type='tel' or contains(translate(@placeholder,'PHONE','phone'),'phone')]"
                )
            )
        )

        phone_input.clear()
        phone_input.send_keys(phone)

        print("14. Phone number entered successfully!")

    # =========================================================
    # ENTER EMAIL
    # =========================================================

    def enter_email(self, email):

        print("15. Entering email...")

        email_input = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[@type='email' or contains(translate(@placeholder,'EMAIL','email'),'email')]"
                )
            )
        )

        email_input.clear()
        email_input.send_keys(email)

        print("16. Email entered successfully!")

    # =========================================================
    # START CHAT
    # =========================================================

    def click_start_chat(self):

        print("17. Clicking Start Chat...")

        start_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(normalize-space(.),'Start Chat') or contains(normalize-space(.),'Start chat')]"
                )
            )
        )

        start_button.click()

        print("18. Start Chat clicked successfully!")

        time.sleep(2)

    # =========================================================
    # ENTER TEXT MESSAGE
    # =========================================================

    def enter_message(self, message):

        print("19. Entering chat message...")

        textarea = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "textarea[placeholder='Type your message']"
                )
            )
        )

        textarea.click()
        textarea.send_keys(message)

        print("20. Chat message entered successfully!")

    # =========================================================
    # SEND TEXT MESSAGE
    # =========================================================

    def send_message(self):

        print("21. Clicking Send...")

        send_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[title='Send message (Enter)']"
                )
            )
        )

        print("22. Send button FOUND!")

        send_button.click()

        print("23. Text message sent successfully!")

    # =========================================================
    # START RECORDING
    # =========================================================

    def start_recording(self):

        print("24. Starting voice recording...")

        record_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[title='Start recording']"
                )
            )
        )

        print("25. Start recording button FOUND!")

        record_button.click()

        print("26. Recording started!")

    # =========================================================
    # SEND RECORDING
    # =========================================================

    def send_recording(self):

        print("27. Waiting for Send recording button...")

        send_recording_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[title='Send recording']"
                )
            )
        )

        print("28. Send recording button FOUND!")

        send_recording_button.click()

        print("29. Recording sent successfully!")

    # =========================================================
    # END CHAT
    # =========================================================

    def click_end_chat(self):

        print("30. Ending chat...")

        end_chat = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[normalize-space()='End Chat']/ancestor::button[1]"
                )
            )
        )

        print("31. End Chat button FOUND!")

        end_chat.click()

        print("32. End Chat clicked successfully!")

        time.sleep(2)

    # =========================================================
    # SELECT 5 STAR RATING
    # =========================================================

    def select_star_rating(self):

        print("33. Selecting 5-star rating...")

        # IMPORTANT:
        # The SVG itself does NOT have a JavaScript .click()
        # method in the way our previous script expected.
        #
        # Therefore we locate the SVG and use Selenium ActionChains.

        star = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "svg.w-8.h-8.cursor-pointer"
                )
            )
        )

        print("34. Star FOUND!")

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            star
        )

        time.sleep(0.5)

        ActionChains(self.driver) \
            .move_to_element(star) \
            .click() \
            .perform()

        print("35. 5-star rating selected!")

        time.sleep(1)

    # =========================================================
    # ENTER FEEDBACK
    # =========================================================

    def enter_feedback(self, feedback):

        print("36. Entering feedback...")

        feedback_box = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "textarea[placeholder='Share your thoughts about our service...']"
                )
            )
        )

        feedback_box.click()
        feedback_box.clear()
        feedback_box.send_keys(feedback)

        print("37. Feedback entered successfully!")

    # =========================================================
    # SUBMIT FEEDBACK
    # =========================================================

    def submit_feedback(self):

        print("38. Submitting feedback...")

        submit_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(normalize-space(.),'Submit Feedback')]"
                )
            )
        )

        print("39. Submit Feedback button FOUND!")

        submit_button.click()

        print("40. Feedback submitted successfully!")

        time.sleep(2)

    # =========================================================
    # KEEP BROWSER OPEN
    # =========================================================

    def wait_after_test(self):

        print("41. Keeping browser open...")

        time.sleep(5)