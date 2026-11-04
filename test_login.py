
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username.send_keys("tomsmith")

        password = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password.send_keys("SuperSecretPassword!")

        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        login_button.click()

        message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged into a secure area!" in message.text

        print("Login test passed")

    finally:
        driver.quit()




       



  

