from facebook.face_base import Facebook
from selenium.webdriver.common.by import By
import json 
from facebook.auth_face import login_face
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Crawler(Facebook):
    def __init__(self, proxy=None, headless=True):
        super().__init__(proxy, headless)

    def login_crawler(self):
        URL_FACEBOOK_HOME = "https://www.facebook.com/"
        default_file = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\cookies\\default_cookie_fb.json'
        
        with open(default_file, 'r') as file:
            cookie_input = json.load(file)
        
        login_face(self.driver, URL_FACEBOOK_HOME, cookie_input) 

    def __save_links_to_file(self, links, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for link in links:
                    file.write(link + '\n')
                    file.flush()

            print("Links saved to file successfully.")

        except Exception as e:
            print(f"Error occurred while saving links: {str(e)}")

    def crawl_group_id(self, max_links=50):
        self.login_crawler()
        sleep(2)
        key_input = input("Enter your key to find groups: ")
        group_url = f"https://www.facebook.com/search/groups/?q={key_input}"
        self.driver.get(group_url)

        sleep(6)
        selector = 'a[role="presentation"]'
        
        # Updated regex pattern to match group URLs
        pattern = re.compile(r'https://www\.facebook\.com/groups/([a-zA-Z0-9]+)/')

        group_names = []

        # Infinite scroll loop
        while len(group_names) < max_links:
            # Scroll the page to load more groups
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for new groups to load (use a small delay if necessary)
            sleep(3)

            # Retrieve the current set of group links
            current_links = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for link in current_links:
                href = link.get_attribute('href')
                link.get_attribute("innerText")
                match = pattern.match(href)
                if match:
                    group_name = match.group(1)
                    if group_name not in group_names:
                        group_names.append(group_name)
                        if len(group_names) >= max_links:
                            break

            print('Found group names: ', len(group_names))

        # Extract group names from links
        group_names_list = group_names[:max_links]
        print(f'Total group names: {len(group_names_list)}')

        file_path = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\craw\\group_name.txt'
        self.__save_links_to_file(group_names_list, file_path)

        return group_names_list




    def crawl_uid_group(self, max_links=10):
        self.login_crawler()
        sleep(2)

        url_group = input("Enter your group id:")
        group_url = f"https://www.facebook.com/groups/{url_group}"
        self.driver.get(group_url)


        selector = 'a[role="link"]'
        
        # Regex pattern to match the desired URL format
        pattern = re.compile(r'https://www\.facebook\.com/groups/\d+/user/(\d+)/')

        uid_links = []

        # Infinite scroll loop
        while len(uid_links) < max_links:
            # Scroll the page to load more UIDs
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for new UIDs to load (use a small delay if necessary)
            sleep(3)

            # Retrieve the current set of UID links
            current_links = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for link in current_links:
                href = link.get_attribute('href')
                match = pattern.match(href)
                if match:
                    uid = match.group(1)
                    if uid not in uid_links:
                        uid_links.append(uid)
                        if len(uid_links) >= max_links:
                            break

            print('Found UIDs: ', len(uid_links))

        # Extract UID URLs from links
        uid_urls = uid_links[:max_links]
        print(f'Total UIDs: {len(uid_urls)}')

        file_path = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\craw\\uid_group.txt'
        self.__save_links_to_file(uid_urls, file_path)

        return uid_urls

    # #not done
    # def crawl_uid_like_post(self):
    #     # self.driver.set_window_size(600, 700)
    #     self.login_crawler()
    #     sleep(2)

        
    #     link_post = "https://www.facebook.com/permalink.php?story_fbid=pfbid025fm4E7XuryipeWse6mEnPPZ5UVqq9qhyrykSwLRyDtj7dkWjKxreFgUsaKsgKiail&id=100079084535437"
    #     self.driver.get(link_post)
    #     sleep(3)
    #     like_button = self.driver.find_element(By.CSS_SELECTOR, 'span[class="x1e558r4"]')
    #     like_button.click()

    #     sleep(3)
        
    
    #     # Lấy các link chứa ID
    #     links = self.driver.find_elements(By.CSS_SELECTOR, 'a[role="link"]')
    #     sleep(5)
    #     # Lưu các ID vào file
    #     with open('facebook_ids.txt', 'a') as file:
    #         for link in links:
    #             href = link.get_attribute('href')
    #             # user_id = re.search('id=(\d+)', href).group(1)
    #             # file.write(user_id + '\n')\
    #             file.write(href + '\n')
    #             print("write file!")

    #     # Xóa các thẻ div chứa link đó
    #     for link in links:
    #         print("delete link")
    #         self.driver.execute_script("arguments[0].parentNode.parentNode.parentNode.removeChild(arguments[0].parentNode.parentNode);", link)

    #     # Đợi một chút để tải thêm người dùng mới
    #     sleep(111115)

    #     # Đóng webdriver
    #     self.driver.quit()