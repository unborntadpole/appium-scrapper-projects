from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def myanimelist(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://myanimelist.net/")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign Up")]'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'email'))).send_keys(emailadd)
        driver.find_element(By.NAME, 'user_name').click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"You already have an account associated with this e-mail address.")]')))
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(myanimelist('sam@gmail.com')['registered'])
# print(myanimelist('sasdsasdggcvqwerdf@gmail.com')['registered'])
