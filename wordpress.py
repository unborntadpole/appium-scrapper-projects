from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wordpress(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://wordpress.com/")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Get Started")]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Continue with Email")]'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'email'))).send_keys(emailadd)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'button'))).click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"This email address is already associated with an account. Please consider ")]'))).click()
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(wordpress('sam@gmail.com')['registered'])
# print(wordpress('sasdsasdggcvqwerdf@gmail.com')['registered'])
