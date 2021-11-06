



def main() :
    print('hello wirld')
    from selenium import webdriver

    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    driver.get('https://www.spotify.com')
    screenshot = driver.save_screenshot('my_screenshot.png')
    driver.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
