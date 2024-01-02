from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def swiggy_number(pno):
    try:
        # Enter an email address here that is already known to be registered to a Swiggy account
        dummy_email = ''  # Any account will do as there is no actual notification sent.
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        driver.get("https://www.swiggy.com/")
        # driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[2]').click()
        driver.find_element(By.XPATH, '//*[contains(text(),"Sign up")]').click()
        driver.find_element(By.NAME, 'mobile').send_keys(pno)
        driver.find_element(By.NAME, 'name').send_keys('xyz')
        driver.find_element(By.NAME, 'email').send_keys(dummy_email)
        driver.find_element(By.XPATH, '//*[contains(text(),"CONTINUE")]').click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Mobile number already exists")]')))
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


def swiggy_email(emailadd):  # WARNING! An OTP is sent to this number if no account is found registered to the email.
    try:
        dummy_number = '9123456789'  # this number nust NOT be registered in Swiggy.
        # WARNING! An OTP is sent to this number if no account is found registered to the email.
        # This number must be in your possession.
        driver = webdriver.Chrome()
        temp = 0
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        driver.get("https://www.swiggy.com/")
        # driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[2]').click()
        driver.find_element(By.XPATH, '//*[contains(text(),"Sign up")]').click()
        driver.find_element(By.NAME, 'mobile').send_keys(dummy_number)
        driver.find_element(By.NAME, 'name').send_keys('xyz')
        driver.find_element(By.NAME, 'email').send_keys(emailadd)
        driver.find_element(By.XPATH, '//*[contains(text(),"CONTINUE")]').click()
        try:
            search_incorrect_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Email id already exists")]')))
            temp = 1
        except:
            temp = 0
        driver.quit()
        return {"registered": temp}
    except:
        return {"registered": 'null'}


# DRIVER CODE
# print(swiggy_number('')['registered'])
# print(swiggy_number('9123456789')['registered'])
# print(swiggy_email('its@gmail.com')['registered'])
# print(swiggy_email('sasjkbcvbiusdgbamnsbdc@gmail.com')['registered'])