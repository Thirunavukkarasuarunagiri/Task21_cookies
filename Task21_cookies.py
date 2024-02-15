from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SauceDemoLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        # Find username and password fields, and login button
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")

        # Enter username and password
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        # Click the login button
        login_button = self.driver.find_element_by_id("login-button")
        login_button.click()
        WebDriverWait(self.driver, 10)

    def display_cookies(self):
        # Display cookies before login
        cookies_before_login = self.driver.get_cookies()
        print("Cookies before login:", cookies_before_login)

        # Login
        self.login()

        # Display cookies after login
        cookies_after_login = self.driver.get_cookies()
        print("Cookies after login:", cookies_after_login)
        WebDriverWait(self.driver, 10)

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


username = "standard_user"
password = "secret_sauce"

sauce_demo_login = SauceDemoLogin(username, password)

sauce_demo_login.display_cookies()

sauce_demo_login.close_browser()