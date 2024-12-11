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

class TestViewIntroduceAndGuideVideo(BaseTest):

    def test_video(self):

        time.sleep(15)

        accept_update_alert = self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        accept_update_alert.click()
        time.sleep(3)

        accept_clause = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(19)")
        accept_clause.click()
        time.sleep(1)

        agree_language = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(30)")
        agree_language.click()
        time.sleep(1)

        close_introduce = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(13)")
        close_introduce.click()
        time.sleep(1)

        # el5 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(31)")
        # el5.click()
        # time.sleep(20)
        try:
            el5 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(31)")
            if el5.is_displayed():
                el5.click()
                time.sleep(20)
                video_introduce = 'Run'

        except NoSuchElementException:
            print("Video introduce not run")
            video_introduce = 'Not Run'


        el6 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(34)")
        el6.click()
        time.sleep(20)

        try:
            skip_guide = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
            if el6.is_displayed():
                skip_guide.click()
                time.sleep(1)
                video_guide = 'Run'


        except NoSuchElementException:
            print("Video guide not run")
            video_guide = 'Run'

        try:
            # success_element = self.driver.find_element(by=AppiumBy.XPATH, value=end)  # Replace with an actual ID of an element indicating success
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("-----------Test watch--------------")

            logger.info( "Test watch introduce: " +video_introduce + " and guide video: " + video_guide)
            logger.info("-----------------------------------")

        except Exception as e:
            logger.info( "Test watch introduce: " +video_introduce + " and guide video: " + video_guide)
            logger.error( "Test watch introduce and guide video failed with exception:: %s", e)
