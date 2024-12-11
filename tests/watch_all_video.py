# tests/test_login.py
import time
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.base_test import BaseTest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WatchAllVideo(BaseTest):

    def test_excircise_01(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "1"
        quantity_video = 14
        description = "test_excircise_01"
        self.common_step(app_language,keys,quantity_video,description)    

    def test_excircise_02(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "2"
        quantity_video = 11
        description = "test_excircise_02"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_03(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "3"
        quantity_video = 12
        description = "test_excircise_03"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_04(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "4"
        quantity_video = 8
        description = "test_excircise_04"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_05(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "5"
        quantity_video = 13
        description = "test_excircise_05"
        self.common_step(app_language,keys,quantity_video,description)  
        

    def test_excircise_06(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "6"
        quantity_video = 13
        description = "test_excircise_06"
        self.common_step(app_language,keys,quantity_video,description)    

    def test_excircise_07(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "7"
        quantity_video = 17
        description = "test_excircise_07"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_08(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "9"
        quantity_video = 13
        description = "test_excircise_08"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_09(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "9"
        quantity_video = 17
        description = "test_excircise_09"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_10(self):      
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "10"
        quantity_video = 16
        description = "test_excircise_10"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_11(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "11"
        quantity_video = 7
        description = "test_excircise_11"
        self.common_step(app_language,keys,quantity_video,description)    

    def test_excircise_12(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "12"
        quantity_video = 6
        description = "test_excircise_12"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_13(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "13"
        quantity_video = 6
        description = "test_excircise_13"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_14(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "14"
        quantity_video = 7
        description = "test_excircise_14"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_15(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "15"
        quantity_video = 9
        description = "test_excircise_15"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_16(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "16"
        quantity_video = 13
        description = "test_excircise_16"
        self.common_step(app_language,keys,quantity_video,description)    

    def test_excircise_17(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "17"
        quantity_video = 15
        description = "test_excircise_17"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_18(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "18"
        quantity_video = 8
        description = "test_excircise_18"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_19(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "19"
        quantity_video = 15
        description = "test_excircise_19"
        self.common_step(app_language,keys,quantity_video,description)  

    def test_excircise_20(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        keys = "20"
        quantity_video = 18
        description = "test_excircise_20"
        self.common_step(app_language,keys,quantity_video,description)


    def common_step(self,app_language,keys,quantity_video,description):
        time.sleep(20)

        try:
            accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
            if accept.is_displayed():
                accept.click()
                time.sleep(3)
        except NoSuchElementException:
            time.sleep(3)

        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
        agree_button.click()
        time.sleep(2)


        choose_language = self.driver.find_element(by=AppiumBy.XPATH, value=app_language)  
        choose_language.click()
        time.sleep(2)           


        choose_language_done = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
        choose_language_done.click()
        time.sleep(2)

        skip = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup')  
        skip.click()
        time.sleep(2)
        
        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]')  
        login_button.click()
        time.sleep(5)

        skip_alert_gps = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')  
        skip_alert_gps.click()
        time.sleep(15)

        # skip_botchat = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(64)")
        # skip_botchat.click()
        # time.sleep(3)

        choose_search = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(58)")
        choose_search.click()
        time.sleep(1)
        
        class_input = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
        class_input.send_keys(keys)
        time.sleep(3)

        choose_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(27)")
        choose_video.click()
        choose_video.click()
        time.sleep(10)
        
        try:
            # Attempt to locate the element
            el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Tại sao bạn nên tập bài này:\")")
            
            if el1.is_displayed():  # Check if the element is visible
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();')
                time.sleep(3)
                el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(22)")
                el1.click()
                time.sleep(3)
                el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Tập luyện thường\")")
                el2.click()
                time.sleep(3)
        
        except NoSuchElementException:

            first_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(78)")
            first_video.click()
            time.sleep(3)

            practice_with_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(94)")
            practice_with_video.click()
            time.sleep(3)

        for i in range(quantity_video):
            self.repeat_next_video() 
        try:
            # success_element = self.driver.find_element(by=AppiumBy.XPATH, value=end)  # Replace with an actual ID of an element indicating success
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info( description + " success")
        except Exception as e:
            self.fail( description + " fail")
            logger.error( description + " failed with exception:: %s", e)

    def repeat_next_video(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1130, 536)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(10)
        
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1130, 536)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1130, 536)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1789, 539)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

