import unittest
from appium import webdriver

from config.config import APPIUM_CONFIG

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options


class BaseTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     capabilities_options = UiAutomator2Options().load_capabilities(APPIUM_CONFIG['desired_capabilities'])
 
    #     cls.driver = webdriver.Remote(
    #         command_executor=APPIUM_CONFIG['appium_server'],
    #         options=capabilities_options
    #     )

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # @classmethod
    def setUp(self):
        capabilities_options = UiAutomator2Options().load_capabilities(APPIUM_CONFIG['desired_capabilities'])
 
        self.driver = webdriver.Remote(
            command_executor=APPIUM_CONFIG['appium_server'],
            options=capabilities_options
        )

    # @classmethod
    def tearDown(self):
        self.driver.quit()