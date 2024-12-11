
APPIUM_CONFIG = {
    'appium_server': 'http://localhost:4723',
    'desired_capabilities': {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'LM-V409N',
        # 'deviceName': 'CPH2121',
        #  'deviceName': 'SM-G955N',
        'appActivity': 'MainActivity',
        'appPackage': 'com.vdsmart.eyeprosport'
        # Add other desired capabilities as needed
    }
}
