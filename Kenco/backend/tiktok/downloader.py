import os

import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


from tiktok.base import Tiktok


class Downloader(Tiktok):
    URL = 'https://snaptik.app/'

    def __init__(self, key, proxy=None, headless=False):
        super().__init__(proxy, headless)
        self.video_save_path = os.path.join(self.results_path, key)
        self.links_file_path = os.path.join(self.video_save_path, f'{key}.txt')

        # Ensure that the folders exist
        os.makedirs(self.video_save_path, exist_ok=True)

    def read_links_file(self):
        # Handling the scenario where the file is not found
        if not os.path.isfile(self.links_file_path):
            print(f"File '{self.links_file_path}' not found.")
            return []

        # Reading data from the file and handling the scenario of an empty file
        with open(self.links_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print(f"File '{self.links_file_path}' is empty.")
                return []

        return lines

    def __input_url(self, link):
        # Use the _wait_for_element_clickable method to wait until the input element with CSS selector 'input#url' is clickable
        input_element = self._wait_for_element_clickable(By.CSS_SELECTOR, 'input#url')

        # Use the send_keys method to input the specified 'link' into the found input element
        input_element.send_keys(link)

    def __get_normal_link(self):
        # Find the element by its CSS selector
        download_link_element = self._wait_for_element_located(By.CSS_SELECTOR, 'a.button.download-file', 20)

        # Extract the 'href' attribute, which contains the link
        download_link = download_link_element.get_attribute('href')

        return download_link

    @staticmethod
    def __json_processing(request_link):
        # Send a GET request to the specified source link
        response = requests.get(request_link)

        if response.status_code == 200:  # Check if the request was successful (status code 200)
            try:
                # Attempt to decode the JSON data from the response
                json_data = response.json()
                # Extract the 'url' field from the JSON data
                final_link = json_data.get('url')
                return final_link
            except Exception as e:  # Handle exceptions, including JSON decoding errors
                print(f"Error decoding JSON: {e}")
                print("Response content:")
                print(response.text)
        else:
            # Print an error message if the request did not succeed
            print(f"Failed to retrieve JSON data. Status code: {response.status_code}")

    def __get_hd_link(self):
        # Find the element by its CSS selector
        try:
            element = self._wait_for_element_located(By.CSS_SELECTOR, 'button.btn-download-hd', 20)

            # Get the value of the 'data-tokenhd' attribute
            token_value = element.get_attribute('data-tokenhd')

            # Construct the URL for the HD video link request using the extracted token value
            hd_link_request = f'https://snaptik.app/getHdLink.php?token={token_value}'

            # Call the __json_processing method to retrieve the final video link
            final_video_link = self.__json_processing(hd_link_request)

            return final_video_link
        except NoSuchElementException:
            self.driver.refresh()

            sleep(5)
            return self.download()


    @staticmethod
    def __download_video(url, save_path,  max_retries=3):
        try:
            # Send a GET request to the specified URL with streaming enabled
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            print(f'Downloading video...')

            # Open a file to save the video content
            with open(save_path, 'wb') as file:
                # Iterate through the response content in chunks and write to the file
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print('Video has been successfully downloaded and saved\n')
        except requests.exceptions.RequestException as e:
            # Handle exceptions related to the requests library
            print(f'Error occurred while downloading the video: {e}')
            retries += 1
            if retries < max_retries:
                print(f'Retrying... ({retries}/{max_retries})')
                sleep(2)  # Wait for 2 seconds before retrying
            else:
                print('Failed to download video after several attempts.\n')

    def download(self, link, mode='hd'):
        # Use the Selenium WebDriver instance to navigate to a specified URL
        self.driver.get(self.URL)

        # Calling the method to input the link into the search field
        self.__input_url(link)

        # Check the mode specified for video quality
        if mode == 'hd':
            # If HD mode is selected, get the HD video link
            video_link = self.__get_hd_link()
        else:
            # If not in HD mode, get the normal video link
            video_link = self.__get_normal_link()

        # Extracting the last part of the URL after the last '/'
        filename = f'{link.strip().split("/")[-1]}.mp4'

        # Creating the full file save path by joining the save_path and the filename
        file_save_path = os.path.join(self.video_save_path, filename)

        # Check if the video_link is not None (indicating a successful JSON processing)
        if video_link:
            # Call the method for downloading video using the final link
            self.__download_video(video_link, file_save_path)
        else:
            print('Failed to obtain the final video link.')
