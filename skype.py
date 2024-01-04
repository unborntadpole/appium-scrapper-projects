from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def skype(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get('https://www.skype.com/en/')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign in")]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign up")]'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'MemberName'))).send_keys(emailadd)
        wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.ID, 'MemberNameError'))).click()
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(skype('sam@outlook.com')['registered'])
# print(skype('sasdsasdggcvqwerdf@gmail.com')['registered'])
