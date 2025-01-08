from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import random
import requests
import os

adClickCount=0
def getLocation():
    """
    Fetch a random location using an external API.
    The API key and other sensitive data are retrieved from environment variables.
    """
    url = "https://www.browserstack.com/local/api/v1/inbound-ip-geolocation"

    # Retrieve API authorization from environment variables
    auth_key = os.getenv('BROWSERSTACK_API_KEY')
    if not auth_key:
        raise EnvironmentError("BROWSERSTACK_API_KEY not found in environment variables.")

    headers = {
        'Authorization': f'Basic {auth_key}',
        'Cookie': os.getenv('BROWSERSTACK_COOKIE', '')  # Optional cookie
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Return a random location from the API response
    loc = random.choice(list(response.json().keys()))
    return loc

def handle_ads(driver):
    elements_to_check = [
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue to app"]', "Continue to app clicked"),
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Skip video"]', "Skip video clicked"),
        (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/close_icon"]', "Close icon clicked"),
        (AppiumBy.XPATH, '//android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View[6]/android.view.View/android.widget.TextView', "bottom close clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.TextView[1]', "bottom close clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button', "bottom close clicked"),
        # (AppiumBy.XPATH, '(//android.widget.Button)[1]', "bottom close clicked"),
        (AppiumBy.XPATH, '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Button', "bottom close clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button', "ads clicked"),

    ]
    for locator, xpath, message in elements_to_check:
        try:
            element = WebDriverWait(driver,3).until(EC.presence_of_element_located((locator, xpath)))
            if element.is_displayed():
                element.click()
                print(message)
                break
        except (TimeoutException, NoSuchElementException):
            continue
def click_ads(driver):
    elements_to_check = [
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View', "ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]', "ads clicked"),
        (AppiumBy.XPATH, '//android.widget.TextView[@text="INSTALL"]', "install ads clicked"),
        (AppiumBy.XPATH, '//android.view.View[@resource-id="skyscraper"]', "install ads by id clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.TextView', "install ads clicked by xpath"),
        (AppiumBy.XPATH, '//android.view.View[@content-desc="details%3Fid%3Dcom.zzkko%26adGroupId%3D107c3e8943d546e6%26gclid%3DEAIaIQobChMIt_zk3P67iAMVLoNQBh2NmBb_EAEYASAAEgJWuvD_BwE%26referrer%3Dgclid%253DEAIaIQobChMIt_zk3P67iAMVLoNQBh2NmBb_EAEYASAAEgJWuvD_BwE%2526gbraid%253D0AAAAADOVYZhQyWR-nOZ4n_MkvdKFUOJAL%2526gad_source%253D5%26gref%3DEikQAhohChsKEwi3_OTc_ruIAxUug1AGHY2YFv8QARgBIAASAla68P8HARiYw9WcAyIKCAEYFCABMAE4AQ%23Intent%3Bscheme%3Dmarket%3Bpackage%3Dcom.android"]', "install ads desc ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.TextView', "install 2nd page btnads clicked"),
    ]
    for locator, xpath, message in elements_to_check:
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((locator, xpath)))
            if element.is_displayed():
                element.click()
                print(message)
                break
        except (TimeoutException, NoSuchElementException):
            continue
def click_ads(driver):
    global adClickCount
    adClickFlag=False
    elements_to_check = [
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[8]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.TextView', "install ads clicked"),
        (AppiumBy.XPATH, '//android.widget.TextView[@text="INSTALL"]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]', "install ads clicked"),
        
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[8]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.TextView', "install ads clicked"),
        (AppiumBy.XPATH, '//android.widget.TextView[@text="INSTALL"]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View', "install ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]', "install ads clicked"),
                	
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View', "ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]', "ads clicked"),
        (AppiumBy.XPATH, '//android.view.View[@resource-id="skyscraper"]', "install ads by id clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.TextView', "install ads clicked by xpath"),
        (AppiumBy.XPATH, '//android.view.View[@content-desc="details%3Fid%3Dcom.zzkko%26adGroupId%3D107c3e8943d546e6%26gclid%3DEAIaIQobChMIt_zk3P67iAMVLoNQBh2NmBb_EAEYASAAEgJWuvD_BwE%26referrer%3Dgclid%253DEAIaIQobChMIt_zk3P67iAMVLoNQBh2NmBb_EAEYASAAEgJWuvD_BwE%2526gbraid%253D0AAAAADOVYZhQyWR-nOZ4n_MkvdKFUOJAL%2526gad_source%253D5%26gref%3DEikQAhohChsKEwi3_OTc_ruIAxUug1AGHY2YFv8QARgBIAASAla68P8HARiYw9WcAyIKCAEYFCABMAE4AQ%23Intent%3Bscheme%3Dmarket%3Bpackage%3Dcom.android"]', "install ads desc ads clicked"),
        (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.TextView', "install 2nd page btnads clicked"),

    ]
    for locator, xpath, message in elements_to_check:
        if(adClickFlag==False):
            try:
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((locator, xpath)))
                if element.is_displayed():
                    element.click()
                    print(message)
                    # break
            except (TimeoutException, NoSuchElementException):
                continue
            if driver.current_package != "com.hd.video.downloader.xv":
                adClickCount+=1
                adClickFlag=True
        else:
            break

def random_int_1_to_7():
    return random.randint(1, 7)

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720

options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "deviceName": "Samsung Galaxy S22 Ultra",
    "platformName": "android",
    "platformVersion": "12.0",
    "interactiveDebugging" : True

    # Add your caps here
})





driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
current_package_name = driver.current_package
print(current_package_name)
time.sleep(20)

def flow1_clickads(driver):
    click_ads(driver)
    print('current_package 1: ',driver.current_package)
    time.sleep(10)
    current_package_name = driver.current_package
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    print('current_package 2: ',current_package_name)
    current_package_name = driver.current_package
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
        current_package_name = driver.current_package
        if current_package_name != "com.hd.video.downloader.xv":
            driver.press_keycode(4)
        else:
            driver.activate_app("com.hd.video.downloader.xv")
    current_package_name = driver.current_package
    print(driver.current_package)
    handle_ads(driver)
    print('current_package 3: ',current_package_name)
    current_package_name = driver.current_package
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    print('current_package 4: ',current_package_name)
    current_package_name = driver.current_package
    chooseLanguage(driver)
    print('current_package 5: ',current_package_name)
    current_package_name = driver.current_package
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    print('current_package 6: ',current_package_name)
    current_package_name = driver.current_package
    time.sleep(2)
    next_3dots(driver)

def flow2_skipads(driver):
    handle_ads(driver)
    print('current_package : ',current_package_name)
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
        if current_package_name != "com.hd.video.downloader.xv":
            driver.activate_app("com.hd.video.downloader.xv")
        handle_ads(driver)
    chooseLanguage(driver)
    time.sleep(2)
    next_3dots(driver)

def flow3_skipads_clicklast(driver):
    flow2_skipads(driver)
    click_ads(driver)
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    else:
        driver.activate_app("com.hd.video.downloader.xv")
        flow2_skipads(driver)
        handle_ads(driver)
    handle_ads(driver)

def chooseLanguage(driver):
    if current_package_name != "com.hd.video.downloader.xv":
        driver.press_keycode(4)
        if current_package_name != "com.hd.video.downloader.xv":
            driver.press_keycode(4)
        else:
            driver.activate_app("com.hd.video.downloader.xv")
    handle_ads(driver)
    language_random_int=random_int_1_to_7()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,f'(//android.widget.LinearLayout[@resource-id="com.hd.video.downloader.xv:id/ll"])[{language_random_int}]'))).click()
    except:
        try:
            handle_ads(driver)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,f'(//android.widget.LinearLayout[@resource-id="com.hd.video.downloader.xv:id/ll"])[{language_random_int}]'))).click()
        except Exception as e:
            print(e)

def next_3dots(driver):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/next"]'))).click()
        print('first next selected')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        print('second next selected')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        print('third next selected')
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//*[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        except:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//*[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
            except:
                pass
    except:
        handle_ads(driver)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/next"]'))).click()
        print('first next selected')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        print('second next selected')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        print('third next selected')
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//*[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
        except:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//*[@resource-id="com.hd.video.downloader.xv:id/btnNext"]'))).click()
            except:
                pass

def last_process(driver):
    flow2_skipads(driver)
    time.sleep(20)
    print(driver.current_package)
    handle_ads(driver)
    if current_package_name == "com.hd.video.downloader.xv":
        driver.press_keycode(4)
    time.sleep(2)
    print(driver.current_package)
    handle_ads(driver)
    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'))).click()
    except:
        pass
    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/start"]'))).click()
    except:
        pass
    time.sleep(2)


flow2_skipads(driver)
flow1_clickads(driver)
flow3_skipads_clicklast(driver)