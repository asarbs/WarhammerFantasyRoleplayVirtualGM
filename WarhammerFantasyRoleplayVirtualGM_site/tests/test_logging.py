from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


from WarhammerFantasyRoleplayVirtualGM_app.models import Player

logger = logging.getLogger('AuthenticationTests')

class AuthenticationTests(StaticLiveServerTestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.username = "test"
        self.email = "test@test.com"
        self.password = "test_password"
        
    @classmethod
    def setUpClass(cls) -> None:
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chrome_options)
        return super(AuthenticationTests, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        return super(AuthenticationTests, cls).tearDownClass()

    def runTest(self):
        user = User.objects.create_superuser(self.username, self.email, self.password)
        user.save()

        player = Player.objects.create(user=user)
        player.save()

        
        self.browser.get(f"{self.live_server_url}/login/")
        title = self.browser.title 
        self.assertEqual("Warhammer Fantasy Roleplay - Companion", title)
        
        self.browser.implicitly_wait(0.5)

        login_box =     self.browser.find_element(by=By.ID, value="id_username")
        password_box =  self.browser.find_element(by=By.ID, value="id_password")
        submit_button = self.browser.find_element(by=By.CLASS_NAME, value="button")

        login_box.send_keys(self.username)
        password_box.send_keys(self.password)
        submit_button.click()
        
        self.browser.implicitly_wait(0.5)
        
        logged_text_box = self.browser.find_element(by=By.CLASS_NAME, value="user").find_element(by=By.TAG_NAME, value="span")
        self.assertEqual(f"Logged in as: {self.username}", logged_text_box.text)


        self.browser.implicitly_wait(0.5)
        player.delete()
        user.delete()
        


