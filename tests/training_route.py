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

    # def test_fill_servey(self):

    #     # self.common_step()
    #     time.sleep(15)

    #     try:
    #         accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
    #         if accept.is_displayed():
    #             accept.click()
    #             time.sleep(3)
    #     except NoSuchElementException:
    #         print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")

    #     agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
    #     agree_button.click()
    #     time.sleep(2)

    #     VN_choose = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tiếng việt (VI)"]')  
    #     VN_choose.click()
    #     time.sleep(1)

    #     agree_lang_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')  
    #     agree_lang_button.click()
    #     time.sleep(5)

    #     skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Bỏ qua"]')  
    #     skip_button.click()
    #     time.sleep(2)

    #     login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]')  
    #     login_button.click()
    #     time.sleep(10)

    #     skip_alert_gps = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')  
    #     skip_alert_gps.click()
    #     time.sleep(10)

    #     # skip_ad = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(100)")
    #     # skip_ad.click()
    #     # time.sleep(2)

    #     try:
    #         skip_ad = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(100)")
    #         skip_ad.click()
    #         time.sleep(5)
    #     except NoSuchElementException:
    #         print("Không tìm thấy element skip ad")
    #         time.sleep(5)

    #     # accept_alert = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(80)")  
    #     # accept_alert.click()
    #     # time.sleep(2)

    #     time.sleep(5)
    #     fill_survey = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(51)")
    #     fill_survey.click()
    #     time.sleep(2)


    #     choose_sex = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(26)")  
    #     choose_sex.click()
    #     time.sleep(2)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(34)")  
    #     next.click()
    #     time.sleep(2)

    #     choose_age = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(31)")  
    #     choose_age.click()
    #     time.sleep(2)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(39)")  
    #     next.click()
    #     time.sleep(2)

    #     height = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Chiều cao\")")
    #     height.send_keys("178")
    #     time.sleep(1)


    #     weight = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Cân nặng\")")
    #     weight.send_keys("82")
    #     time.sleep(1)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(32)")
    #     next.click()
    #     time.sleep(1)

    #     choose_lever = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(28)")
    #     choose_lever.click()
    #     time.sleep(1)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(39)")
    #     next.click()
    #     time.sleep(1)


    #     choose_disease = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(0)")
    #     choose_disease.click()
    #     time.sleep(1)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(47)")
    #     next.click()
    #     time.sleep(1)

    #     health = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(0)")
    #     health.click()
    #     time.sleep(1)

    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(48)")
    #     next.click()
    #     time.sleep(1)

    #     status = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(0)")
    #     status.click()
    #     time.sleep(1)


    #     next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(45)")
    #     next.click()
    #     time.sleep(1)

    #     only_weekday = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(40)")
    #     only_weekday.click()
    #     time.sleep(1)

    #     choose_time = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(35)")
    #     choose_time.click()
    #     time.sleep(1)

    #     set_time = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(8)")
    #     set_time.click()
    #     time.sleep(1)

    #     send = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(43)")
    #     send.click()
    #     time.sleep(5)


    #     # choose_age = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(29)")  
    #     # choose_age.click()
    #     # time.sleep(2)

    #     #         skip_alert_gps = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')  
    #     # skip_alert_gps.click()
    #     # time.sleep(2)

    #     # end_survey = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(55)")
    #     # end_survey.click()
    #     # time.sleep(10)

    #     # accept_route = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(20)")
    #     # accept_route.click()
    #     # time.sleep(3)

    #     # route = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.TextView\").instance(38)")
    #     # route.click() 
    #     # time.sleep(3)

    #     try:
    #         success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup')  # Replace with an actual ID of an element indicating success
    #         self.assertTrue(success_element.is_displayed())
    #         logger.info("Login test fill servey success")
    #     except Exception as e:
    #         self.fail(f'Login test failed with exception: {e}')
    #         logger.error("Login test failed with exception:: %s", e)


    # def test_list_training_route(self):
    #     # self.common_step()
    #     time.sleep(15)

    #     try:
    #         accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')
    #         if accept.is_displayed():
    #             accept.click()
    #             time.sleep(3)
    #     except NoSuchElementException:
    #         print("Không tìm thấy element 'accept'. Tiếp tục thực hiện các bước tiếp theo.")

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
    #     time.sleep(10)

    #     try:
    #         skip_ad = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(100)")
    #         skip_ad.click()
    #         time.sleep(5)
    #     except NoSuchElementException:
    #         print("Không tìm thấy element skip ad")
    #         time.sleep(5)


    #     # skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="__CAROUSEL_ITEM_0_READY__"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
    #     # skip_button.click()
    #     # time.sleep(3)

    #     # skip_take_picture = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Bài 14: Suối nguồn tươi trẻ\").instance(6)")
    #     # skip_take_picture.click()
    #     # time.sleep(3)

    #     practice_now = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(50)")
    #     practice_now.click()
    #     time.sleep(10)

    #     # skip_take_a_photo = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId(\"progress-circle\").instance(13)')
    #     # skip_take_a_photo.click()
    #     # time.sleep(3)

    #     skip_take_picture = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Bài 14: Suối nguồn tươi trẻ\").instance(6)")
    #     skip_take_picture.click()
    #     time.sleep(3)

    #     for _ in range(5): 
    #         self.driver.find_element(
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
    #         )
    #     time.sleep(3)

    #     for _ in range(5): 
    #         self.driver.find_element(
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward();'
    #         ) 
    #     time.sleep(3)

    #     # choose_old_class = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(58)")
    #     # choose_old_class.click()
    #     # time.sleep(3)

    #     # skip_alert = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(87)")
    #     # skip_alert.click()
    #     # time.sleep(3)

    #     # choose_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(1)")
    #     # choose_video.click()
    #     # time.sleep(1)

    #     # exercise_normal = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Tập luyện thường\")")
    #     # exercise_normal.click()
    #     # time.sleep(1)



    #     # for i in range(7):
    #     #     self.repeat_video()  

    #     try:
    #         success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]')  # Replace with an actual ID of an element indicating success
    #         self.assertTrue(success_element.is_displayed())
    #         logger.info("View workout schedule success")
    #     except Exception as e:
    #         self.fail(f'Login test failed with exception: {e}')
    #         logger.error("Login test failed with exception:: %s", e)


    # def test_list_training_route_past_VIE(self):
    #     app_language ='//android.view.View/android.view.ViewGroup[2]'
    #     skip_alert="new UiSelector().resourceId(\"progress-circle\").instance(13)"
    #     video="new UiSelector().resourceId(\"progress-circle\").instance(0)"
    #     result ="View workout schedule in past(VIE) success"
    #     self.common_step(app_language,skip_alert,video,result)

    # def test_list_training_route_future_VIE(self):
    #     app_language ='//android.view.View/android.view.ViewGroup[2]'
    #     skip_alert="new UiSelector().resourceId(\"progress-circle\").instance(13)"
    #     video="new UiSelector().resourceId(\"progress-circle\").instance(3)"
    #     result ="View workout schedule in future(VIE) success"
    #     self.common_step(app_language,skip_alert,video,result)

    # def test_list_training_route_past_EN(self):
    #     app_language ='//android.view.View/android.view.ViewGroup[1]'
    #     skip_alert="new UiSelector().text(\"Class 12: 15 Minutes for a Flexible and Healthy Spine\").instance(6)"
    #     video="new UiSelector().resourceId(\"progress-circle\").instance(0)"
    #     result ="View workout schedule in past(ENG) success"
    #     self.common_step(app_language,skip_alert,video,result)

    # def test_list_training_route_future_EN(self):
    #     app_language ='//android.view.View/android.view.ViewGroup[1]'
    #     skip_alert="new UiSelector().text(\"Class 12: 15 Minutes for a Flexible and Healthy Spine\").instance(6)"
    #     video="new UiSelector().resourceId(\"progress-circle\").instance(3)"
    #     result ="View workout schedule in future(ENG) success"
    #     self.common_step(app_language,skip_alert,video,result)

    # def test_list_training_route_future_EN(self):
    #     app_language ='//android.view.View/android.view.ViewGroup[3]'
    #     skip_alert="new UiSelector().text(\"Class 12: 15 Minutes for a Flexible and Healthy Spine\").instance(6)"
    #     video="new UiSelector().resourceId(\"progress-circle\").instance(3)"
    #     result ="View workout schedule in future(JP) success"
    #     self.common_step(app_language,skip_alert,video,result)


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

        try:
            skip_ad = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(100)")
            skip_ad.click()
            time.sleep(5)
        except NoSuchElementException:
            print("Không tìm thấy element skip ad")
            time.sleep(5)

        skip_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="__CAROUSEL_ITEM_0_READY__"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
        skip_button.click()

        practice_now = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(48)")
        practice_now.click()
        time.sleep(10)

        skip_take_a_photo = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId(\"progress-circle\").instance(13)')
        skip_take_a_photo.click()
        time.sleep(3)
        for _ in range(1): 
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward();'
            )
        hide_chatbot_alert = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Xin chào , bạn vẫn chưa hoàn thành lộ trình tập yoga của tuần này. Hãy tăng thời gian tập luyện lên ít nhất 15 phút mỗi buổi.\").instance(1)")
        hide_chatbot_alert.click()
        time.sleep(2)

        edit_time = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(49)")
        edit_time.click()
        time.sleep(2)

        choose_time = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(36)")
        choose_time.click()
        time.sleep(2)

        set_time = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(7)")
        set_time.click()
        time.sleep(5)

        submit = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(45)")
        submit.click()
        time.sleep(5)

        

        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Cập nhật thời gian tập luyện thành công"]')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info("Tese_change_time_done")
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)


    def common_step(self,app_language,skip_alert,video,result):
        time.sleep(15)

        accept = self.driver.find_element(by=AppiumBy.ID, value='android:id/button1')  
        accept.click()
        time.sleep(3)

        agree_button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')  
        agree_button.click()
        time.sleep(2)

        language_choose = self.driver.find_element(by=AppiumBy.XPATH, value=app_language)  
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

        skip_take_a_photo = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=skip_alert)
        if skip_take_a_photo.is_displayed():
            skip_take_a_photo.click()
        time.sleep(3)


        chooese_video = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=video)
        chooese_video.click()
        time.sleep(3)
        


        try:
            success_element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')  # Replace with an actual ID of an element indicating success
            self.assertTrue(success_element.is_displayed())
            logger.info(result)
        except Exception as e:
            self.fail(f'Login test failed with exception: {e}')
            logger.error("Login test failed with exception:: %s", e)



    def repeat_video(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1250, 547)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(10)


        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1250, 547)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        # try to merge 178-192
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1250, 547)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        # time.sleep(1)   
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1963, 541)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
      