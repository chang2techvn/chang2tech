import os
import json
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from tiktok.base import Tiktok
from tiktok.auth_tiktok import login_


class Parser(Tiktok):
    URL = 'https://www.tiktok.com/'
    LOGIN_URL = 'https://www.tiktok.com/login/phone-or-email/email'

    def __init__(self, email, password, proxy=None, headless=False):
        super().__init__(proxy, headless)
        self.email = email
        self.password = password
        self.cookies_path = os.path.join(os.path.abspath('backend/tiktok/data'), 'cookies')
        self.cookies_file_path = os.path.join(self.cookies_path, f'{self.email}.pkl')

        os.makedirs(self.cookies_path, exist_ok=True)

    def __input_keyword(self, keyword):
        # Find the input element using Selenium and input data into it
        search_input = self._wait_for_element_clickable(By.CSS_SELECTOR, 'input[data-e2e="search-user-input"]', 60)
        search_input.send_keys(keyword)

        # Press the Enter key
        search_input.send_keys(Keys.ENTER)

    def __switch_to_video_tab(self):
        # Find and click the video tab
        video_tab = self.driver.find_element(By.ID, 'tabs-0-tab-search_video')
        video_tab.click()

    def __parsing_processing(self, selector, timeout=1):
        # Waiting until the first element becomes clickable
        self._wait_for_element_clickable(By.XPATH, selector, 120)
        
        # Find initial set of video links
        video_links = self.driver.find_elements(By.XPATH, selector)
        prev_video_count = len(video_links)
        sleep(2)
        # Infinite scroll loop
        while True:
            # Cuộn trang bằng JavaScript
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)

            # Retrieve current set of video links
            video_links = self.driver.find_elements(By.XPATH, selector)
            current_video_count = len(video_links)
            print('Found videos: ', len(video_links))

            # Break the loop if the count remains the same (no new videos loaded)
            if current_video_count == prev_video_count:
                break

            # On each iteration, we update the value of 'prev_video_count'
            # by assigning it the value of 'current_video_count'
            prev_video_count = current_video_count

        # Extract video URLs from links
        video_urls = [link.get_attribute('href') for link in video_links]
        print(f'Total links: {len(video_urls)}\n')

        return video_urls

    def __save_links_to_file(self, links, file_path):
        try:
            # Attempt to open the file for appending, using UTF-8 encoding.
            with open(file_path, 'w', encoding='utf-8') as file:
                # Iterate through the provided links and write each one to a new line in the file.
                for link in links:
                    file.write(link + '\n')
                    file.flush()  # Flush the buffer to ensure immediate writing.

                # Display a success message indicating that the links were saved to the file.
                print("Links saved to file.")

        except Exception as e:
            # If an exception occurs during the file operation, print an error message.
            print(f"Error occurred while saving links: {str(e)}")

    # @staticmethod
    # def __cookies_file_exists(cookies_filename):
    #     return os.path.exists(cookies_filename)
        # # Check if cookies file exists
        # if self.__cookies_file_exists(self.cookies_file_path):
        #     print('Cookies found. Logging into the account with the cookies...')

        #     # Load cookies from the existing file
        #     with open(self.cookies_file_path, "rb") as cookies_file:
        #         cookies = pickle.load(cookies_file)

        #     # Navigate to the login URL and add cookies to the current session
        #     self.driver.get(self.LOGIN_URL)
        #     for cookie in cookies:
        #         self.driver.add_cookie(cookie)

        #     # Refresh the page after adding cookies
        #     self.driver.get(self.LOGIN_URL)
        # else:
        #     try:
        #         print('Logging into the account...')

        #         # Navigate to the login URL
        #         self.driver.get(self.LOGIN_URL)

        #         # Find and fill in the email input field
        #         input_email = self._wait_for_element_located(By.CSS_SELECTOR, 'input[type="text"]')
        #         input_email.send_keys(self.email)

        #         # Find and fill in the password input field
        #         input_password = self._wait_for_element_located(By.CSS_SELECTOR, 'input[type="password"]')
        #         input_password.send_keys(self.password)

        #         # Find and click the login button
        #         login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="login-button"]')
        #         login_button.click()

        #         sleep(30)

        #         # Wait for the login button to become invisible (indicating successful login)
        #         self._wait_for_element_invisible(By.CSS_SELECTOR, 'button[data-e2e="login-button"]')

        #         # Get the current session cookies and save them to a file
        #         cookies = self.driver.get_cookies()
        #         with open(self.cookies_file_path, "wb") as cookies_file:
        #             pickle.dump(cookies, cookies_file)
        #     except Exception as e:
        #         # Raise an exception in case of a login error
        #         raise Exception("Login error: \n", e)

    def parse_by_keyword(self, key, mode='top'):
        #login account by cookie 

        # Đường dẫn tới tệp cookies
        # cookies_file_path = r'C:\Users\ADMIN\Desktop\chang2tech\Kenco\backend\tiktok\data\cookies\default.pkl'

        # Load cookies from the existing file
        default_file = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\tiktok\\data\\cookies\\default.json'
        with open(default_file, 'r') as file:
            cookie_input = json.load(file)

        URL_home = "https://www.tiktok.com/"
        login_(self.driver, URL_home, cookie_input)

        save_path = os.path.join(self.results_path, key)
        os.makedirs(save_path, exist_ok=True)

        file_path = os.path.join(save_path, f'{key}.txt')

        self.driver.get(self.URL)
        sleep(10)
        self.__input_keyword(key)
    

        # XPath expressions for finding links on the Top and Videos tabs
        top_tab_xpath = '//div[@data-e2e="search_top-item"]//a[@tabindex="-1"]'
        video_tab_xpath = '//div[@data-e2e="search_video-item"]//a[@tabindex="-1"]'

        if mode == 'top':
            video_links = self.__parsing_processing(top_tab_xpath, 15)
        else:
            video_links = self.__parsing_processing(video_tab_xpath, 15)

        self.__save_links_to_file(video_links, file_path)


    def __get_user_videos(self, key):
        # login
        default_file = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\tiktok\\data\\cookies\\default.json'
        with open(default_file, 'r') as file:
            cookie_input = json.load(file)

        URL_home = "https://www.tiktok.com/"
        login_(self.driver, URL_home, cookie_input)

        # Navigate to the user's TikTok page
        self.driver.get(f'{self.URL}@{key}')
        sleep(5)

        # # Click on the 'Videos' tab on the user's profile page
        # videos_tab = self._wait_for_element_clickable(By.XPATH, '//div[contains(@class, "share-tab")][2]', 30)
        # videos_tab.click()
        # sleep(2)

        # Use the existing __parsing_processing method to get video URLs
        video_links = self.__parsing_processing('//div[@data-e2e="user-post-item"]//a', 15)

        return video_links


    def parse_by_user_id(self, key):

        # Ensure the results directory exists
        save_path = os.path.join(self.results_path, key)
        os.makedirs(save_path, exist_ok=True)

        # Define the path for the output file
        file_path = os.path.join(save_path, f'{key}.txt')

        # Get video links for the given user ID
        video_links = self.__get_user_videos(key)

        # Save the video links to the file
        self.__save_links_to_file(video_links, file_path)
