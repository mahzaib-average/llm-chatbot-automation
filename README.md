# LLM Chatbot Automation

## 📌 Project Overview

This project is a Selenium-based end-to-end test automation framework developed using **Python, Pytest, and the Page Object Model (POM)**.

The framework automates and validates the complete user journey of an LLM chatbot, including chatbot initialization, user information, country selection, text messaging, voice recording, chat termination, rating, and feedback submission.

The project is designed with a clean and maintainable automation framework structure suitable for QA automation and portfolio demonstration.

---

## 🛠️ Tech Stack

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Google Chrome**
- **FFmpeg**
- **Git**
- **GitHub**

---

## 🤖 Automated Test Scenario

The current end-to-end test covers the following flow:

1. Open the Kordic website
2. Open the chatbot
3. Wait for the chatbot iframe
4. Switch into the chatbot iframe
5. Enter user name
6. Open country dropdown
7. Select United Arab Emirates
8. Enter phone number
9. Enter email address
10. Start the chat
11. Enter a text message
12. Send the text message
13. Start voice recording
14. Record voice for 7 seconds
15. Send the voice recording
16. End the chat
17. Select a 5-star rating
18. Enter feedback
19. Submit feedback

---

## 🏗️ Project Structure

```text
llm-chatbot-automation/
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── screenshot.py
│
├── screenshots/
│
├── videos/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Page Object Model

This framework follows the **Page Object Model (POM)** design pattern to separate test logic from page interaction logic.

### `pages/login_page.py`

Contains chatbot page locators and interaction methods, including:

- Opening the chatbot
- Handling the chatbot iframe
- Entering name
- Selecting country
- Entering phone number
- Entering email
- Starting chat
- Sending text messages
- Starting voice recording
- Sending voice recording
- Ending chat
- Selecting star rating
- Entering feedback
- Submitting feedback

### `tests/test_login.py`

Contains the end-to-end test scenario and controls the execution flow.

The test file calls reusable methods from the Page Object instead of directly interacting with Selenium elements.

### `utils/screenshot.py`

Contains reusable screenshot functionality.

Screenshots are automatically captured at important stages of the test execution.

### `conftest.py`

Contains reusable Pytest fixtures and WebDriver configuration.

It handles:

- Chrome WebDriver setup
- Browser configuration
- Microphone permissions
- Fake microphone configuration
- Website initialization
- Screenshot directory setup
- Video recording configuration

---

## 📸 Screenshot Capture

The framework automatically captures screenshots at important checkpoints during test execution.

Examples include:

- Chatbot opened
- Name entered
- Country selected
- Phone number entered
- Email entered
- Chat started
- Text message sent
- Voice recording sent
- Chat ended
- Rating selected
- Feedback entered
- Feedback submitted

Screenshots are stored locally in:

```text
screenshots/
```

Generated screenshots are excluded from source control using `.gitignore`.

---

## 🎥 Video Recording

The automation framework supports browser test video recording using **FFmpeg**.

Video recordings are stored locally in:

```text
videos/
```

Video files are excluded from GitHub because generated recordings can become large.

---

## ⚙️ Prerequisites

Before running the project, install:

- Python 3.x
- Google Chrome
- Selenium
- Pytest
- FFmpeg

Verify Python:

```bash
python --version
```

Verify Pytest:

```bash
pytest --version
```

Verify FFmpeg:

```bash
ffmpeg -version
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mahzaib-average/llm-chatbot-automation.git
```

Navigate to the project directory:

```bash
cd llm-chatbot-automation
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

Run the test suite:

```bash
pytest -v
```

For detailed console output:

```bash
pytest -v -s
```

The `-s` option displays the test execution messages in the terminal.

---

## ✅ Expected Result

A successful execution should display:

```text
========================
1 passed
========================
```

The test also generates screenshots and a video recording locally.

---

## 🧪 Test Coverage

| Test Area | Status |
|---|---|
| Chatbot Launch | ✅ |
| iframe Handling | ✅ |
| Name Entry | ✅ |
| Country Selection | ✅ |
| Phone Number | ✅ |
| Email | ✅ |
| Chat Initialization | ✅ |
| Text Messaging | ✅ |
| Voice Recording | ✅ |
| Voice Message Submission | ✅ |
| End Chat | ✅ |
| Star Rating | ✅ |
| Feedback | ✅ |
| Screenshot Capture | ✅ |
| Video Recording | ✅ |

---

## 🔍 Automation Framework Highlights

This project demonstrates the following QA automation practices:

- Page Object Model architecture
- Reusable Pytest fixtures
- Selenium WebDriver automation
- iframe handling
- Dynamic web interaction
- Text message automation
- Voice recording automation
- Microphone permission handling
- Screenshot capture
- Video recording
- Separation of test and page logic
- Reusable utility functions
- Pytest-based test execution
- Git and GitHub version control

---

## 📂 Test Artifacts

The framework generates test artifacts locally:

### Screenshots

```text
screenshots/
```

### Videos

```text
videos/
```

These generated artifacts are excluded from GitHub using `.gitignore`.

---

## 🔐 Test Data

The current automation uses sample test data for demonstration purposes.

Example:

```text
Name: John Doe
Country: United Arab Emirates
Phone: 501234567
Email: john.doe@example.com
Message: Hello
Feedback: The chatbot experience was very good.
```

Sensitive credentials or private information should not be stored in the repository.

---

## 🧱 Framework Design Principles

The framework follows these principles:

- Maintainable test structure
- Reusable page methods
- Separation of concerns
- Reusable fixtures
- Reusable utilities
- Clear test execution flow
- Source control best practices
- Generated test artifacts excluded from Git

---

## 🚀 Future Improvements

The framework can be extended with:

- Multiple test scenarios
- Data-driven testing
- Explicit waits instead of fixed waits
- Environment-based configuration
- HTML test reports
- Allure reporting
- CI/CD integration using GitHub Actions
- Cross-browser testing
- API validation
- Test data management
- Enhanced logging
- Failure screenshots
- Automatic test artifact management

---


 👩‍💻 Author

**QA Automation Engineer**


- Software Quality Assurance
- Selenium WebDriver
- Python
- Pytest
- Page Object Model
- UI Test Automation
- Test Framework Design
- Screenshot Automation
- Video Recording
- Git
- GitHub
