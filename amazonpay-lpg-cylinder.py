from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from PIL import Image
import io
from io import BytesIO
import base64

# user details are returned in a dictionary under key 'name' as a base64 coded image
# if not user is found text is returned 'User not found' under same key 'name'

def run_app(driver):
    try:
        driver.activate_app('in.amazon.mShop.android.shopping')
        driver.terminate_app('in.amazon.mShop.android.shopping')
        driver.activate_app('in.amazon.mShop.android.shopping')
        driver.implicitly_wait(15)
        driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Amazon Pay\"]").click()
        driver.implicitly_wait(15)
        driver.find_element(by=AppiumBy.XPATH,
                            value="//android.view.View[@content-desc=\"Pay Bills\"]/android.widget.TextView[1]").click()
        driver.implicitly_wait(15)
        driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Image[@text=\"Book Gas Cylinder\"]").click()
        driver.implicitly_wait(15)
    except Exception as e1:
        # print('failure in app launch', e1, sep='\n')
        pass


def extract(driver):
    try:
        name = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="text"])[4]').text
        image_element = driver.find_element(by=AppiumBy.XPATH, value='//android.webkit.WebView[@text="LPG Gas Cylinder"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
        location = image_element.location
        size = image_element.size
        # taking a screenshot
        screenshot = driver.get_screenshot_as_base64()
        # processing the image
        image = Image.open(BytesIO(base64.b64decode(screenshot)))
        cropped_image = image.crop(
            (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        image_bytes = io.BytesIO()
        cropped_image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        output = {
            'name': name,
            'photo': encoded_image,
        }
        return output
    except Exception as e1:
        # print('failure in extraction', e1, sep='\n')
        return {'name': 'User not found'}


def bharat_gas(driver, pno):
    try:
        run_app(driver)
        driver.find_element(by=AppiumBy.XPATH,
                            value='//android.webkit.WebView[@text=\"LPG Gas Cylinder\"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]').click()
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.XPATH,
                            value='//android.webkit.WebView[@text="LPG Gas Cylinder"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys(
            pno)
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button").click()
        driver.implicitly_wait(5)
        output = extract(driver)
        return output
    except Exception as e1:
        # print('failure in bharatgas', e1, sep='\n')
        return {'name': 'User not found'}


def hp_gas(driver, pno):
    try:
        run_app(driver)
        driver.find_element(by=AppiumBy.XPATH,
                            value='//android.webkit.WebView[@text="LPG Gas Cylinder"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]').click()
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.XPATH,
                            value='//android.webkit.WebView[@text="LPG Gas Cylinder"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys(
            pno)
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button").click()
        driver.implicitly_wait(5)
        output = extract(driver)
        return output
    except Exception as e1:
        # print('failure in hp gas', e1, sep='\n')
        return {'name': 'User not found'}


def indane_gas(driver, pno):
    try:
        run_app(driver)
        driver.find_element(by=AppiumBy.XPATH,
                            value="//android.webkit.WebView[@text=\"LPG Gas Cylinder\"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]").click()
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.XPATH,
                            value="//android.webkit.WebView[@text=\"LPG Gas Cylinder\"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText").send_keys(
            pno)
        driver.implicitly_wait(5)
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button").click()
        driver.implicitly_wait(5)
        output = extract(driver)
        return output
    except Exception as e1:
        # print('failure in indane gas', e1, sep='\n')
        return {'name': 'User not found'}


def amazonpay_lpg_cylinder(pno):  # main function
    try:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android'
        }

        url = 'http://localhost:4724'  # enter appium server address

        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        bharat_output = bharat_gas(driver, pno)
        hp_output = hp_gas(driver, pno)
        indane_output = indane_gas(driver, pno)
        output = [bharat_output, hp_output, indane_output]
        driver.terminate_app('in.amazon.mShop.android.shopping')
        driver.quit()
        for dic in output:
            if dic['name'] != 'User not found':
                temp_dic = {}
                temp_dic['name'] = dic['photo']
                return temp_dic
        return {'name': 'User not found'}
    except Exception as e1:
        # print('failure in main code', e1, sep='\n')
        return {'name': 'User not found'}


# # runner code
# output = amazonpay_lpg_cylinder('9049808980')
# if output['name'] == 'User not found':
#     print(output['name'])
# else:
#     image2 = Image.open(BytesIO(base64.b64decode(output['name'])))
#     image2.save('amazonpay-lpg-cylinder-output.png')
