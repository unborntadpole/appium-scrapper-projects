import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from PIL import Image
from io import BytesIO
import base64

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android'
}

url = 'http://localhost:4724'  # enter appium server address

phonenumber = ''  # enter the number here

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.execute_script('mobile: pressKey', {"keycode": 3})
driver.implicitly_wait(500)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Viber').click()
driver.implicitly_wait(500)
driver.execute_script('mobile: pressKey', {"keycode": 4})
driver.implicitly_wait(500)
driver.execute_script('mobile: pressKey', {"keycode": 4})
driver.implicitly_wait(500)
driver.execute_script('mobile: pressKey', {"keycode": 4})
driver.implicitly_wait(500)
driver.execute_script('mobile: pressKey', {"keycode": 4})
driver.implicitly_wait(500)
driver.execute_script('mobile: pressKey', {"keycode": 4})
driver.implicitly_wait(1000)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Viber').click()
driver.implicitly_wait(1000)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@resource-id="com.viber.voip:id/fab_compose"]').click()
driver.implicitly_wait(500)
driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/invite_contact_btn").click()
driver.implicitly_wait(500)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add contact").click()
driver.implicitly_wait(500)
driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/phone_number").send_keys(phonenumber)
driver.implicitly_wait(500)
driver.find_element(by=AppiumBy.ID, value="com.viber.voip:id/continue_btn").click()
time.sleep(1)

action = TouchAction(driver)
action.press(x=400, y=500).move_to(x=400, y=400).release().perform()
driver.implicitly_wait(500)

name = driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/display_name_text').text
if name == '':
    print("Account does not exist")
else:
    driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/done').click()
    time.sleep(3)
    image_element = driver.find_element(by=AppiumBy.ID, value='com.viber.voip:id/photo')
    location = image_element.location
    size = image_element.size
    # taking a screen shot
    screenshot = driver.get_screenshot_as_base64()
    # deleting the contact
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='More options').click()
    driver.implicitly_wait(500)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.viber.voip:id/title" and @text="Delete"]').click()
    driver.implicitly_wait(500)
    driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
    time.sleep(2)
    # processing the image
    image = Image.open(BytesIO(base64.b64decode(screenshot)))
    cropped_image = image.crop(
        (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
    cropped_image.save('viber_profile_pic.png')
    print(name)
driver.quit()
