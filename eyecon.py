import time
import io
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from PIL import Image
from io import BytesIO
import base64


def eyecon():
    try:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android',
            'appPackage': 'com.eyecon.global',
            'appActivity': '.MainScreen.MainActivity',
            'noReset': 'true',
        }

        url = 'http://localhost:4724'  # enter appium server address
        phonenumber = ''

        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        wait = WebDriverWait(driver, 10)
        driver.activate_app('com.eyecon.global')
        driver.terminate_app("com.eyecon.global")
        driver.execute_script('mobile: pressKey', {"keycode": 3})
        driver.implicitly_wait(200)
        driver.activate_app('com.eyecon.global')
        wait.until(ec.presence_of_element_located((AppiumBy.ID, 'com.eyecon.global:id/EIB_stats')))
        driver.find_element(by=AppiumBy.ID, value="com.eyecon.global:id/EIB_stats").click()
        driver.find_element(by=AppiumBy.ID, value='com.eyecon.global:id/et_search').send_keys(phonenumber)
        driver.find_element(by=AppiumBy.ID, value="com.eyecon.global:id/search").click()
        time.sleep(10)

        try: # this is to clear the advertisements
            if driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="towerVideo"]/android'
                                                            '.view.View/android.view.View[5]').is_displayed():
                driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.view.View[@resource-id="towerVideo"]/android.view.View/android'
                                          '.view.View[5]').click()
        except:
            print('ad type 1 not found')
        # try: # this is also to clear advertisements
        #     driver.find_element(by=AppiumBy.).click()
        # except:
        #     print('as type 2 not found')

        wait.until(ec.presence_of_element_located((AppiumBy.ID, 'com.eyecon.global:id/EA_photo')))
        name = driver.find_element(by=AppiumBy.ID, value='com.eyecon.global:id/TV_name').text
        image_element = driver.find_element(by=AppiumBy.ID, value='com.eyecon.global:id/EA_photo')
        location = image_element.location
        size = image_element.size
        # taking a screen shot
        screenshot = driver.get_screenshot_as_base64()
        # processing the image
        image = Image.open(BytesIO(base64.b64decode(screenshot)))
        cropped_image = image.crop(
            (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        image_bytes = io.BytesIO()
        cropped_image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        driver.terminate_app("com.eyecon.global")
        driver.quit()
        return {
            'name': name,
            'photo': encoded_image,
        }
    except:
        return {
            'name': 'User not found'
        }


# # Runner code
# output = eyecon()
# print(output['name'])
# image2 = Image.open(BytesIO(base64.b64decode(output['photo'])))
# image2.save('output.png')
