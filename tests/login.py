# tests/test_login.py
import time
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.base_test import BaseTest
# from appium import webdriver
# from appium.webdriver.common.actionchains import ActionChains

from appium.webdriver.common.appiumby import AppiumBy
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Login(BaseTest):

    # def test_login_khoe360(self):

    #     username_field = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="username"]')  # Replace with actual ID
    #     password_field = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="password"]')  # Replace with actual ID
    #     login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="login"]/android.view.ViewGroup')  # Replace with actual ID

    #     # Input username and password
    #     username_field.send_keys('yoga123')  # Replace with a valid username
    #     password_field.send_keys('Yoga123@')  # Replace with a valid password
        
    #     time.sleep(1)
    #     # Click the login button
    #     login_button.click()
        
    #     # Wait for a while to ensure the login process is complete
    #     time.sleep(5)


    def test_login_with_gmail(self):
        time.sleep(15)

        # accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
        # if accept.is_displayed():
        #     accept.click()
        #     time.sleep(3)

        try:
            accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
            if accept.is_displayed():
                accept.click()
                time.sleep(3)
        except NoSuchElementException:
            print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")
        
        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
        agree_button.click()
        time.sleep(2)

        choose_laguage = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tiếng việt (VI)"]')  
        choose_laguage.click()
        time.sleep(1)


        agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
        agree_lang_button.click()
        time.sleep(5)

        skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Bỏ qua"]')  
        skip_button.click()
        time.sleep(5)
    
        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]')  
        login_button.click()
        time.sleep(5)

        choose_available_account = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[2]')  
        choose_available_account.click()
        time.sleep(10)

        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.android.permissioncontroller:id/content_container"]/android.widget.LinearLayout')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("Login test gmail success")
            logger.info("-----------------------------------")

        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)


    def test_login_with_facebook(self):

        time.sleep(15)

        try:
            accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
            if accept.is_displayed():
                accept.click()
                time.sleep(3)
        except NoSuchElementException:
            print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")
        
        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
        agree_button.click()
        time.sleep(2)

        choose_laguage = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tiếng việt (VI)"]')  
        choose_laguage.click()
        time.sleep(1)

        agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
        agree_lang_button.click()
        time.sleep(5)

        skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Bỏ qua"]')  
        skip_button.click()
        time.sleep(5)

        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]')  
        login_button.click()
        time.sleep(10)

        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.android.permissioncontroller:id/content_container"]/android.widget.LinearLayout')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("-------------Login test------------")
            logger.info("Login test with facebook success")
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)

        

