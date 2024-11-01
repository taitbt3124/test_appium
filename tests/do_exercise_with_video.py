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

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestDoExerciseWithVideo(BaseTest):
    # def test_edit_time_route(self):
    #     time.sleep(15)

    #     accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
    #     accept.click()
    #     time.sleep(3)

    #     agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
    #     agree_button.click()
    #     time.sleep(2)

    #     language_choose = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View/android.view.ViewGroup[2]')  
    #     language_choose.click()
    #     time.sleep(1)

    #     agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
    #     agree_lang_button.click()
    #     time.sleep(5)

    #     skip_button = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(13)")  
    #     skip_button.click()
    #     time.sleep(3)

    #     login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]')  
    #     login_button.click()
    #     time.sleep(10)

    #     skip_alert_gps = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')  
    #     skip_alert_gps.click()
    #     time.sleep(3)

    #     skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="__CAROUSEL_ITEM_0_READY__"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
    #     if skip_button.is_displayed():
    #         skip_button.click()

    #     for _ in range(2): 
    #         self.driver.find_element(
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
    #         )

    #     el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(1)")
    #     el1.click()
    #     time.sleep(2)

    #     el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(1)")
    #     el2.click()
    #     time.sleep(2)

    #     el3 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(101)")
    #     el3.click()
    #     time.sleep(2)

    #     actions = ActionChains(self.driver)
    #     actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(1278, 519)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.pause(0.1)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #     actions = ActionChains(self.driver)
    #     actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(1278, 519)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.pause(0.1)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #     time.sleep(5)


    #     out_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(22)")
    #     out_video.click()
    #     time.sleep(2)

    #     submit_out_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(55)")
    #     submit_out_video.click()
    #     time.sleep(2)

    #     el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(55)")
    #     el1.click()
    #     time.sleep(2)

    #     actions = ActionChains(self.driver)
    #     actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(151, 546)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.pause(0.1)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()

    #     actions = ActionChains(self.driver)
    #     actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(542, 2262)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.pause(0.1)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()

    #     el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(23)")
    #     el2.click()
    #     time.sleep(2)


        
    #     try:
    #         success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')  # Replace with an actual ID of an element indicating success
    #         self.assertTrue(success_element.is_displayed())
    #         logger.info("Test_out_soon_of_exercise")
    #     except Exception as e:
    #         self.fail(f'Login test failed with exception: {e}')
    #         logger.error("Login test failed with exception:: %s", e)

    def test_edit_time_route_10_50(self):
        time.sleep(15)

        accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
        accept.click()
        time.sleep(3)

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

        practice_now = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(48)")
        practice_now.click()
        time.sleep(10)

        skip_take_a_photo = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId(\"progress-circle\").instance(13)')
        if skip_take_a_photo.is_displayed():
            skip_take_a_photo.click()
        time.sleep(3)


        # chooese_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=)
        # chooese_video.click()
        # time.sleep(3)


        
        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("Test_out_soon_of_exercise")
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)