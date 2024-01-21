from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from PIL import Image
import io
from io import BytesIO
import base64


def cred(phonenumber):
    try:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android'
        }

        url = 'http://localhost:4724'  # enter appium server address

        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.activate_app('com.dreamplug.androidapp')
        driver.terminate_app('com.dreamplug.androidapp')
        driver.activate_app('com.dreamplug.androidapp')
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id=\"com.dreamplug.androidapp:id/2131431923\" and @text=\"PAY CONTACTS\"]').click()
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="pay to").click()
        driver.implicitly_wait(1000)
        element_for_ref = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='SUGGESTIONS')
        location1 = element_for_ref.location
        size1 = element_for_ref.size
        tap_location = [location1['x'] + size1['width'], location1['y'] + size1['height']]
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").send_keys(phonenumber)
        driver.implicitly_wait(1000)
        driver.execute_script('mobile: pressKey', {"keycode": 4})
        action = TouchAction(driver)
        action.press(x=tap_location[0], y=tap_location[1])
        action.release()
        action.perform()
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='VIEW HISTORY').click()
        driver.implicitly_wait(500)
        image_element = driver.find_element(by=AppiumBy.ID, value='com.dreamplug.androidapp:id/2131428275')
        location = image_element.location
        size = image_element.size
        # taking a screenshot
        screenshot = driver.get_screenshot_as_base64()
        # adjusting the crop location
        location['y'] = size['height'] // 4
        # processing the image
        image = Image.open(BytesIO(base64.b64decode(screenshot)))
        cropped_image = image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height'] // 2))
        image_bytes = io.BytesIO()
        cropped_image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        output = {
            'photo_with_name': encoded_image,
        }
        driver.implicitly_wait(500)
        driver.terminate_app('com.dreamplug.androidapp')
        driver.quit()
        return output
    except:
        return {'name': 'User Not Found'}


# # runner code
# output = cred('')
# image2 = Image.open(BytesIO(base64.b64decode(output['photo_with_name'])))
# image2.save('output.png')
