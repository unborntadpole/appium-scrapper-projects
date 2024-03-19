import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def hp_number(pno):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--enable-cookies")
        driver = webdriver.Chrome(options=options)
        temp = 0
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        driver.get("https://hp.com")
        wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
        driver.get('https://global-navbar-backend.id.hp.com/api/v1/session/login?final_redirect_url=https%3A%2F%2Fwww.hp.com%2Fin-en%2Fhome.html')
        wait.until(EC.visibility_of_element_located((By.ID, 'switch-username'))).click()
        wait.until(EC.visibility_of_element_located((By.ID, 'isoCode'))).send_keys('+91')
        wait.until(EC.visibility_of_element_located((By.ID, 'isoCode'))).send_keys(Keys.ENTER)
        driver.find_element(By.ID, 'phoneNumber').send_keys(pno)
        driver.find_element(By.ID, 'phoneNumber').send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, 'phoneNumber').send_keys(Keys.BACKSPACE)
        time.sleep(2)  # this is necessary or else the program goes on endlessly
        driver.find_element(By.ID, 'phoneNumber').send_keys(pno)  # Doing this twice as it loads the phone number in US format
        driver.find_element(By.ID, 'phoneNumber').send_keys(Keys.ENTER)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Phone number is not valid")]')))
            temp = hp_number(pno)['registered']
        except:
            try:
                search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"HP account not found")]')))
                temp = 0
            except:
                try:
                    search_incorrect_text = wait.until(
                        EC.visibility_of_element_located((By.ID, 'password')))
                    temp = 1
                except:
                    temp = 'null'
        driver.delete_all_cookies()
        driver.quit()
        return {"registered": temp}
    except Exception as ep:
        print(ep)
        return {"registered": 'null'}


def hp_email(emailadd):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--enable-cookies")
        driver = webdriver.Chrome(options=options)
        temp = 0
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        driver.get("https://hp.com")
        # onetrust-accept-btn-handler
        wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
        driver.get('https://global-navbar-backend.id.hp.com/api/v1/session/login?final_redirect_url=https%3A%2F%2Fwww.hp.com%2Fin-en%2Fhome.html')
        wait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys(emailadd)
        driver.find_element(By.ID, 'user-name-form-submit').click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"HP account not found")]')))
            temp = 0
        except:
            try:
                search_incorrect_text = wait.until(
                    EC.visibility_of_element_located((By.ID, 'password')))
                temp = 1
            except:
                temp = 'null'
        driver.delete_all_cookies()
        driver.quit()
        return {"registered": temp}
    except Exception as ep:
        # print(ep)
        return {"registered": 'null'}


# DRIVER CODE
# print(hp_number('')['registered'])
# print(hp_email('')['registered'])
