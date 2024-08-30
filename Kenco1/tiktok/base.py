import os
import undetected_chromedriver as uc
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tiktok:
    def __init__(self, proxy=None, headless=False):
        self.results_path = os.path.abspath('backend/tiktok/results')
        self.driver = self._set_driver(proxy, headless)

        # Ensure that the folders exist
        os.makedirs(self.results_path, exist_ok=True)


    @staticmethod
    def _makedir(path):
        # Check if the directory doesn't exist
        if not os.path.exists(path):
            #Create the directory
            os.makedirs(path)

        # Return the path of the created directory
        return path

    @staticmethod
    def _set_driver(proxy, headless):
        #Creating a ChromeOptions Object for configuring Chrome browser options
        chrome_options = uc.ChromeOptions()
        # Setting headless mode based on the 'headless' parameter
        chrome_options.headless = headless
        #Adding an argument to set the brownser language to English
        chrome_options.add_argument('--lang=en')
        #Disabling the 'credentials_enalbe_sevice' option to prevent credentials
        chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False})

        #Configuring proxy settings if a proxy is provided
        if proxy is not None:
            proxy_options = {
                'proxy': {
                    'http': proxy,
                    'https': proxy,
                    'no_proxy': 'localhost: 127.0.0.1'
                }
            }
        else:
            #No proxy provided, setting proxy_options to None
            proxy_options = None

        #Creating a Chrome driver instance with configured options and proxy settings
        driver = uc.Chrome(options=chrome_options, seleniumire_options=proxy_options)
        driver.set_window_size(900, 700)
        #Return the configured Chrome driver
        return driver

    def _wait_for_element_located(self, by, value, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {by}={value}")

    def _wait_for_element_clickable(self, by, value, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {by}={value}")

    def wait_for_element_invisible(self, by, value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element((by, value))
            )
        except TimeoutException:
            print("Element did not disappear within the specified timeout")
