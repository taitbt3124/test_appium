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

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestViewTraningRoute(BaseTest):
    def test_edit_time_route(self):
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

        language_choose = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View/android.view.ViewGroup[2]')  
        language_choose.click()
        time.sleep(1)

        agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
        agree_lang_button.click()
        time.sleep(5)

        skip_button = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(13)")  
        skip_button.click()
        time.sleep(3)

        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]')  
        login_button.click()
        time.sleep(10)

        skip_alert_gps = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')  
        skip_alert_gps.click()
        time.sleep(3)

        skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="__CAROUSEL_ITEM_0_READY__"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
        if skip_button.is_displayed():
            skip_button.click()

        click_chatbot = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(8)")
        click_chatbot.click()
        time.sleep(3)
        print("1")


        chat_now = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(39)")
        chat_now.click()
        time.sleep(5)
        print("12")


        choose_question = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
        choose_question.click()
        time.sleep(5)



        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("Tese_change_time_done")
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)