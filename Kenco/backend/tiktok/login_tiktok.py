from tiktok.auth_tiktok import login_
from tiktok.base import Tiktok 


class Login(Tiktok):
    def login_cookie(self):
        URL_home = "https://www.tiktok.com/"
        cookie_input = input("Enter new cookie: ")
        login_(self.driver, URL_home, cookie_input)