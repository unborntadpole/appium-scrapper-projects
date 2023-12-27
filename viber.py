import io
import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from PIL import Image
from io import BytesIO
import base64


def viber(phonenumber):
    try:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android'
        }

        url = 'http://localhost:4724'  # enter appium server address
        
        # Note: THERE SHOULD NOT BE ANY CONTACTS SAVED ON DEVICE THAT HAVE A VIBER ACCOUNT.
        
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.activate_app('com.viber.voip')
        driver.terminate_app('com.viber.voip')
        driver.activate_app('com.viber.voip')
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.ImageButton[@resource-id="com.viber.voip:id/fab_compose"]').click()
        driver.implicitly_wait(100)
        driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/invite_contact_btn").click()
        driver.implicitly_wait(100)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add contact").click()
        driver.implicitly_wait(100)
        driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/phone_number").send_keys(phonenumber)
        driver.implicitly_wait(500)
        driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/continue_btn").click()
        time.sleep(1)

        action = TouchAction(driver)
        action.press(x=400, y=500).move_to(x=400, y=400).release().perform()
        driver.implicitly_wait(500)

        name = driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/display_name_text').text
        if name == '':
            output = {'name': 'User not found'}
        else:
            driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/done').click()
            time.sleep(3)
            image_element = driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/photo')
            location = image_element.location
            size = image_element.size
            # taking a screenshot
            screenshot = driver.get_screenshot_as_base64()
            # deleting the contact
            driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='More options').click()
            driver.implicitly_wait(500)
            driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.TextView[@resource-id="com.viber.voip:id/title" and @text="Delete"]').click()
            driver.implicitly_wait(500)
            driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
            time.sleep(2)
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
        driver.implicitly_wait(500)
        driver.terminate_app('com.viber.voip')
        driver.quit()
        return output
    except:
        return{'name': 'User Not Found'}

# # runner code
# output = viber()
# print(output['name'])
# image2 = Image.open(BytesIO(base64.b64decode(output['photo'])))
# image2.save('output.png')
