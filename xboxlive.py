from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def xboxlive(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get('https://www.xbox.com/en-IN/live')
        wait.until(EC.visibility_of_element_located((By.ID, 'mectrl_main_trigger'))).click()
        wait.until(EC.visibility_of_element_located((By.ID, 'signup'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'MemberName'))).send_keys(emailadd)
        wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Someone already has this email address. Try another name or ")]'))).click()
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(xboxlive('sam@outlook.com')['registered'])
# print(xboxlive('sasdsasdggcvqwerdf@gmail.com')['registered'])
