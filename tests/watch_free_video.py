# tests/test_login.py
import time
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.base_test import BaseTest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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

class FreeVideo(BaseTest):

    # def test_vie_class_5(self):
    #     app_language = '//android.view.View/android.view.ViewGroup[2]'
    #     ex_class_scroll_num = -1
    #     ex_class = '//android.widget.TextView[@text="Bài 5 (Miễn Phí): Yoga giảm đau thần kinh toạ hiệu quả"]'
    #     ex_video_scroll_num = -1
    #     ex_video = '//android.widget.TextView[@text="1. Khởi động"]'
    #     ex_video_agree ='//android.widget.TextView[@text="Tập luyện thường"]'
    #     quantity_video = 13
    #     description = "test_vie_class_5 "
    #     self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)

    def test_vie_class_7(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. Khởi động"]'
        ex_video_agree ='//android.widget.TextView[@text="Tập luyện thường"]'
        quantity_video = 17
        description = "test_vie_class_7"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)     
    
    def test_vie_class_10(self):
        app_language = '//android.view.View/android.view.ViewGroup[2]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. Khởi động"]'
        ex_video_agree ='//android.widget.TextView[@text="Tập luyện thường"]'
        quantity_video = 16
        description = "test_vie_class_10"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)          

    # def test_us_class_5(self):
    #     app_language = '//android.view.View/android.view.ViewGroup[1]'
    #     ex_class_scroll_num = -1
    #     ex_class = '//android.widget.TextView[@text="Class 5 (FREE): Yoga effectively reduces sciatic pain"]'
    #     ex_video_scroll_num = -1
    #     ex_video = '//android.widget.TextView[@text="1. Warm up"]'
    #     ex_video_agree ='//android.widget.TextView[@text="Practice with Video"]'
    #     quantity_video = 13
    #     description = "test_us_class_5"
    #     self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)

    def test_us_class_7(self):
        app_language = '//android.view.View/android.view.ViewGroup[1]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.TextView[@text="Class 7  (FREE): Yoga increases endurance and burns fat throughout the body"]'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. Warm up"]'
        ex_video_agree ='//android.widget.TextView[@text="Practice with Video"]'
        quantity_video = 17
        description = "test_us_class_7"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)     
    
    def test_us_class_10(self):
        app_language = '//android.view.View/android.view.ViewGroup[1]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. Warm Up"]'
        ex_video_agree ='//android.widget.TextView[@text="Practice with Video"]'
        quantity_video = 16
        description = "test_us_class_10"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)  

    # def test_jp_class_5(self):
    #     app_language = '//android.view.View/android.view.ViewGroup[3]'
    #     ex_class_scroll_num = -1
    #     ex_class = '//android.widget.TextView[@text="レッスン 5 (サンプル): ヨガは坐骨神経痛を効果的に軽減します"]'
    #     ex_video_scroll_num = -1
    #     ex_video = '//android.widget.TextView[@text="1. ウォームアップ"]'
    #     ex_video_agree ='//android.widget.TextView[@text="ビデオで練習する"]'
    #     quantity_video = 13
    #     description = "test_jp_class_5"
    #     self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)

    def test_jp_class_7(self):
        app_language = '//android.view.View/android.view.ViewGroup[3]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.TextView[@text="レッスン 7 (デモ): ヨガは持久力を高め、体全体の脂肪を燃焼します"]'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. 準備し始める"]'
        ex_video_agree ='//android.widget.TextView[@text="ビデオで練習する"]'
        quantity_video = 17
        description = "test_jp_class_7"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)     
    
    def test_jp_class_10(self):
        app_language = '//android.view.View/android.view.ViewGroup[3]'
        ex_class_scroll_num = 3
        ex_class = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
        ex_video_scroll_num = -1
        ex_video = '//android.widget.TextView[@text="1. ウォームアップ"]'
        ex_video_agree ='//android.widget.TextView[@text="ビデオで練習する"]'
        quantity_video = 16
        description = "test_jp_class_10"
        self.common_step(app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description)  


    def common_step(self,app_language,ex_class_scroll_num, ex_class, ex_video_scroll_num, ex_video, ex_video_agree, quantity_video, description):
        time.sleep(15)

        try:
            accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
            if accept.is_displayed():
                accept.click()
                time.sleep(3)
        except NoSuchElementException:
            print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")
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

        # ex_class scroll
        # ---------------
        if ex_class_scroll_num > -1:
            for _ in range(ex_class_scroll_num): 
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
                )
        choose_ex_free = self.driver.find_element(AppiumBy.XPATH, value=ex_class)
        choose_ex_free.click()
        time.sleep(2)

        if ex_video_scroll_num > -1:
            for _ in range(ex_video_scroll_num): 
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
                )

        take_one_vid = self.driver.find_element(by=AppiumBy.XPATH, value=ex_video)  
        take_one_vid.click()
        time.sleep(2) 

        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value=ex_video_agree)  
        agree_button.click()
        time.sleep(10)  

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
        actions.w3c_actions.pointer_action.move_to_location(1225, 567)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(10)
        
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1225, 567)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1225, 567)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1862, 545)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

