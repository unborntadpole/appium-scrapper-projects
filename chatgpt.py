from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def chatgpt(emailadd):
    try:
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://platform.openai.com/login?launch")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign up")]'))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'email'))).send_keys(emailadd)
        driver.find_element(By.XPATH, '//*[contains(text(),"Continue")]').click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('asdassdasdasd')
        driver.find_element(By.XPATH, '//*[contains(text(),"Continue")]').click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.ID, 'error-element-email')))
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(chatgpt('sam@gmail.com')['registered'])
# print(chatgpt('sasdsasdggcvqwerdf@gmail.com')['registered'])
