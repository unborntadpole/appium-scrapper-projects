from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def paytm_lpg_cylinder(pno):
    try:
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument(r"--user-data-dir=C:\Users\samri\AppData\Local\Google\Chrome\User Data\Profile 1")
        driver = webdriver.Chrome(chrome_options)
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get('https://paytm.com/cylinder-gas-recharge')
        details = []
        details1 = hp_gas(wait, pno)
        if details1 != {}:
            details.append(details1)
        details2 = bharatgas(wait, pno)
        if details2 != {}:
            details.append(details2)
        details3 = indane(wait, pno)
        if details3 != {}:
            details.append(details3)
        return details

    except:
        return {}



def extract(wait):  # this extract is based on bharat gas and has not been tried on hp gas or indane
    details = {}
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Consumer Details")]')))
        try:
            details['consumer_name1'] = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div[2]/ul/li[3]/div[1]/div/div[2]/div[1]/div[2]'))).text
        except:
            pass
        try:
            details['distributor_name'] = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div[2]/ul/li[3]/div[1]/div/div[2]/div[2]/div[2]'))).text
        except:
            pass
        try:
            details['consumer_name2'] = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div[2]/ul/li[3]/div[1]/div/div[2]/div[3]/div[2]'))).text
        except:
            pass
        try:
            details['distributor_id'] = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/div[2]/ul/li[3]/div[1]/div/div[2]/div[4]/div[2]'))).text
        except:
            pass
        return details
    except:
        return details


def hp_gas(wait, pno):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"HP Gas")]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Mobile No./ Consumer No./ LPG ID")]'))).send_keys(pno)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Proceed")]'))).click()
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_3znP')))
            return {}
        except:
            return extract(wait)
    except:
        return {}


def bharatgas(wait, pno):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Bharatgas")]'))).click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"Registered Mobile Number or LPG ID")]'))).send_keys(pno)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Proceed")]'))).click()
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_3znP')))
            return {}
        except:
            return extract(wait)
    except:
        return {}


def indane(wait, pno):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Indane")]'))).click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"Booking Type Value")]'))).send_keys('Mobile Number')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"Enter Registered Mobile Number")]'))).send_keys(pno)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Proceed")]'))).click()
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_3znP')))
            return {}
        except:
            return extract(wait)
    except:
        return {}


# driver code
print(paytm_lpg_cylinder('9049808980'))
