from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from PIL import Image
import io
from io import BytesIO
import base64


def amazonpay(phonenumber):
    try:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android'
        }

        url = 'http://localhost:4724'  # enter appium server address

        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.activate_app('in.amazon.mShop.android.shopping')
        driver.terminate_app('in.amazon.mShop.android.shopping')
        driver.activate_app('in.amazon.mShop.android.shopping')
        driver.implicitly_wait(1000)

        driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@text=\"Send Money\"]").click()
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").send_keys(phonenumber)
        driver.implicitly_wait(1000)
        driver.find_element(by=AppiumBy.XPATH , value='//android.view.ViewGroup[@resource-id="ZU"]').click()
        driver.implicitly_wait(1000)

        name = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="IJ"]').text
        image_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="II"]')
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
        driver.implicitly_wait(500)
        driver.terminate_app('in.amazon.mShop.android.shopping')
        driver.quit()
        return output
    except:
        return{'name': 'User Not Found'}


# # runner code
# output = amazonpay('')
# print(output['name'])
# image2 = Image.open(BytesIO(base64.b64decode(output['photo'])))
# image2.save('output.png')
