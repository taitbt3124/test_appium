import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='SM-G955N',
    appActivity='.MainActivity',
    appPackage='com.vdsmart.eyeprosport'
    # noReset= True 
)

appium_server_url = 'http://localhost:4723'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def test_login_khoe360(self) -> None:
        # Wait for the login screen to load
        time.sleep(15)

        accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
        accept.click()
        time.sleep(5)

        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
        agree_button.click()
        time.sleep(2)

        VN_choose = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tiếng việt (VI)"]')  
        VN_choose.click()
        time.sleep(1)

        agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
        agree_lang_button.click()
        time.sleep(5)

        skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Bỏ qua"]')  
        skip_button.click()
        time.sleep(2)

        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup')  
        login_button.click()
        time.sleep(2)

        # Locate and interact with login elements
        username_field = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="username"]')  # Replace with actual ID
        password_field = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="password"]')  # Replace with actual ID
        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="login"]/android.view.ViewGroup')  # Replace with actual ID

        # Input username and password
        username_field.send_keys('yoga123')  # Replace with a valid username
        password_field.send_keys('Yoga123@')  # Replace with a valid password
        
        time.sleep(1)
        # Click the login button
        login_button.click()
        
        # Wait for a while to ensure the login process is complete
        time.sleep(5)

        # Optionally, verify login success
        # For example, check if a specific element is visible after login
        try:
            success_element = self.driver.find_element(by=AppiumBy.ID, value='com.android.packageinstaller:id/permission_message')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
        


if __name__ == '__main__':
    unittest.main()




# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='SM-G955N',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
#     language='en',
#     locale='US'
# )