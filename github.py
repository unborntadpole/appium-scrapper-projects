from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def github(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://github.com/")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign up")]'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'user[email]'))).send_keys(emailadd)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Continue")]'))).click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.ID, 'email-err')))
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(github('sam@gmail.com')['registered'])
# print(github('sasdsasdggcvqwerdf@gmail.com')['registered'])
