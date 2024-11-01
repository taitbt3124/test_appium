
APPIUM_CONFIG = {
    'appium_server': 'http://localhost:4723',
    'desired_capabilities': {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'CPH2121',
        #  'deviceName': 'SM-G955N',
        'appActivity': 'MainActivity',
        'appPackage': 'com.vdsmart.eyeprosport'
        # 'noReset': True 
        # Add other desired capabilities as needed
    }
}



# {
#   "platformName": "Android",
#   "appium:automationName": "uiautomator2",
#   "appium:deviceName": "SM-G955N",
#   "appium:appActivity": "MainActivity",
#   "appium:appPackage": "com.vdsmart.eyeprosport"
# }