from facebook.auth_face import login_face
from tiktok.base import Tiktok 


class Login(Tiktok):
    def login_cookie(self):
        URL_face_home = "https://www.facebook.com/"
        cookie_input = ""
        login_face(self.driver, URL_face_home, cookie_input)
