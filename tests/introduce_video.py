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

class IntroduceVideo(BaseTest):



# --------------TEST ACCESS TO LESSION 10 PART 1(JAPAN) --------------
    def test_play_video10_2_japan(self):
        app_language = '//android.view.View/android.view.ViewGroup[3]'
        ex_class_scroll_num = 2
        ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'
        ex_video_scroll_num = 1
        ex_video = '//android.widget.TextView[@text="2. 呼吸法"]'
        description = "Test play video 2 class 10 Japan"

        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, description)

    # def test_play_video10_3_japan(self):
    #     app_language = '//android.view.View/android.view.ViewGroup[3]'
    #     ex_class_scroll_num = 2
    #     ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'
    #     ex_video_scroll_num = 1
    #     ex_video = '//android.widget.TextView[@text="3. 目のエクササイズ"]'
    #     description = "Test play video 3 class 10 Japan"

    #     self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, description)

    def common_step(self,app_language, ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, description):
        # Wait for the login screen to load
        time.sleep(15)

        # accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
        # accept.click()
        # time.sleep(5)


        try:
            accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
            if accept.is_displayed():
                accept.click()
                time.sleep(3)
        except NoSuchElementException:
            print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")

        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Đồng ý và tiếp tục"]')  
        agree_button.click()
        time.sleep(2)

        choose_language = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tiếng việt (VI)"]')  
        choose_language.click()
        time.sleep(1)           


        choose_language_done = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Đồng ý và tiếp tục"]')  
        choose_language_done.click()
        time.sleep(5)

        skip = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup')  
        skip.click()
        time.sleep(5)

        choose_introduction = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup')  
        choose_introduction.click()
        time.sleep(1) 

        # Optionally, verify login success
        # For example, check if a specific element is visible after login
        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("TEST VIDEO INTRODUCTION IN VIETNAMESE LANGUAGE success")
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)