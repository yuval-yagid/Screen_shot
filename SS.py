"""Module to take an screenshot using selenium"""
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# pylint: disable=import-error
#from pyvirtualdisplay import Display



def _take_screenshot(browser, file_name):
    img = browser.get_screenshot_as_png()
    with open(file_name, "wb") as image:
        image.write(img)


def _init_browser(url, width=1000, height=500):
    window_width = int(width) if width is not None else 1000
    window_height = int(height) if height is not None else 500
#    display = Display(visible=0, size=(1366, 768))
#    display.start()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option(
        "prefs", {"download.prompt_for_download": False}
    )
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_window_size(window_width, window_height)
    browser.get(url)

    return browser



def take_selenium_screenshot(url, file_name="file_name", width=1000, height=500, **kwargs):
    """ Take an screenshot using selenium

        Keyword arguments:
        url -- URL Page to take the screenshot
        file_name -- Image path name
        width -- Browser width. Default 1000
        height -- Browser height. Default 500
        app_selector_xpath -- Target content XPath selector
        not_load_selector_xpath -- XPath selector to identify an empty page
        timeout -- The time to wait until the content load
    """
    app_selector_xpath ="//div[@id='root']" # kwargs.get("app_selector_xpath", "//div[@id='root']")
    #loading_selector_xpath = kwargs.get("loading_selector_xpath", "//div[contains(@class, 'selenium-data-loading')]")
    #not_load_selector_xpath = kwargs.get(
    #    "not_load_selector_xpath", "//div[contains(@class, 'selenium-data-not-loaded')]"
    #)
    timeout = 10 #int(kwargs.get("timeout", 10))
    # Init chromium
    browser = _init_browser(url, width, height)

    # Wait until the root element is loaded. Value in seconds
    WebDriverWait(browser, timeout)



    # Wait a little bit for DOM changes
    time.sleep(2)

    # Take the screenshot
    _take_screenshot(browser, file_name)

    if browser is not None:
        browser.quit()

def check_url (url):
    try:
        response = requests.get(url)
        print("URL is valid and exists on the internet")
    except requests.ConnectionError as exception:
        print("URL does not exist on Internet")
    except requests.exceptions.MissingSchema.response as exception:
        print("URL is not Valid")

if __name__ == "__main__":
    import sys

    PARAMS = {
        "url": str(sys.argv[1]),
        }
    check_url(**PARAMS)
    print('python version is:' + sys.version)
    
    file_name=str(sys.argv[1]).split('//')[1].split('.')[0]
    file_name=file_name+'.png'
    file_name_with_path='/output/'+file_name
    PARAMS = {
        "url": sys.argv[1],
        "file_name": file_name_with_path
    }
    print(file_name)
    
    take_selenium_screenshot(**PARAMS)
    