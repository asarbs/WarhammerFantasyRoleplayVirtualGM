from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

import logging
import json
import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



from WarhammerFantasyRoleplayVirtualGM_app.models import *

logger = logging.getLogger('AuthenticationTests')
logger_selenium = logging.getLogger('selenium.webdriver.remote.remote_connection')

class RegressionTests(StaticLiveServerTestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.username = "test"
        self.email = "test@test.com"
        self.password = "test_password"
        
    @classmethod
    def setUpClass(cls) -> None:
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # chrome_options.add_argument("log-level=3")
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chrome_options)
        
        logger_selenium.setLevel(logging.WARNING)
        
        with open("/workspaces/WarhammerFantasyRoleplayVirtualGM/WarhammerFantasyRoleplayVirtualGM_site/tests/db.json") as db_dump_file:
            data = json.load(db_dump_file)
            models = {}
            for x in data:
                if "WarhammerFantasyRoleplayVirtualGM" in x['model']:
                    if x['model'] not in models:
                        models[x['model']] = []
                    models[x['model']].append(x)
                    
            for refBook in models['WarhammerFantasyRoleplayVirtualGM_app.refbook']:
                refBookObj = RefBook.objects.create(pk=refBook['pk'], name=refBook['fields']['name'])
                refBookObj.save()
            for reference in models['WarhammerFantasyRoleplayVirtualGM_app.reference']:
                referenceObj = Reference.objects.create(pk=reference['pk'], refBook_id=reference['fields']['refBook'], page=reference['fields']['page'])
                referenceObj.save()
            for skils in models['WarhammerFantasyRoleplayVirtualGM_app.skils']:
                skilsObj = Skils.objects.create(id=skils['pk'], 
                                                name=skils['fields']['name'], 
                                                characteristics=skils['fields']['characteristics'],
                                                description=skils['fields']['description'], 
                                                ref_id=skils['fields']['ref'], 
                                                skils_parent_id=None)
                skilsObj.save()
            for talent in models['WarhammerFantasyRoleplayVirtualGM_app.talent']:
                talentObj = Talent.objects.create(id=talent['pk'], 
                                                  name=talent['fields']['name'], 
                                                  max=talent['fields']['max'], 
                                                  tests=talent['fields']['tests'], 
                                                  description=talent['fields']['description'],
                                                  ref_id=talent['fields']['ref'],
                                                  talent_parent_id=None
                                                  )
                talentObj.save()
            for species in models['WarhammerFantasyRoleplayVirtualGM_app.species']:
                speciesObj = Species.objects.create(id=species['pk'],
                                                    name=species['fields']['name'],
                                                    random_interal_start=species['fields']['random_interal_start'],
                                                    random_interal_end=species['fields']['random_interal_end']
                                                    )
                for s_id in species['fields']['skills']:
                    speciesObj.skills.add(Skils.objects.get(id=s_id))
                for t_id in species['fields']['talents']:
                    speciesObj.talents.add(Talent.objects.get(id=t_id))
                speciesObj.save()
                
            for hair in models['WarhammerFantasyRoleplayVirtualGM_app.hair']:
                hairObj = Hair.objects.create(pk=hair['pk'], 
                                              name=hair['fields']['name'],
                                              species_id=hair['fields']['species'],
                                              random_table_start=hair['fields']['random_table_start'],
                                              random_table_end=hair['fields']['random_table_end'],
                                              )
                hairObj.save()
            for eyes in models['WarhammerFantasyRoleplayVirtualGM_app.eyes']:
                eyesObj = Eyes.objects.create(pk=eyes['pk'], 
                                              name=eyes['fields']['name'],
                                              species_id=eyes['fields']['species'],
                                              random_table_start=eyes['fields']['random_table_start'],
                                              random_table_end=eyes['fields']['random_table_end'],
                                              )
                eyesObj.save()
            for cla in models['WarhammerFantasyRoleplayVirtualGM_app.class']:
                claObj = Class.objects.create(pk=cla['pk'],
                                              name=cla['fields']['name'],
                                              )
                claObj.save()
            for career in models['WarhammerFantasyRoleplayVirtualGM_app.career']:
                careerObj = Career.objects.create(pk=career['pk'],
                                                  ch_class_id                   = career['fields']['ch_class'],
                                                  random_table_human_start      = career['fields']['random_table_human_start'],
                                                  random_table_human_end        = career['fields']['random_table_human_end'],
                                                  random_table_dwarf_start      = career['fields']['random_table_dwarf_start'],
                                                  random_table_dwarf_end        = career['fields']['random_table_dwarf_end'],
                                                  random_table_halfling_start   = career['fields']['random_table_halfling_start'],
                                                  random_table_halfling_end     = career['fields']['random_table_halfling_end'],
                                                  random_table_high_elf_start   = career['fields']['random_table_high_elf_start'],
                                                  random_table_high_elf_end     = career['fields']['random_table_high_elf_end'],
                                                  random_table_wood_elf_start   = career['fields']['random_table_wood_elf_start'],
                                                  random_table_wood_elf_end     = career['fields']['random_table_wood_elf_end'],
                                                  random_table_wood_ogre_start  = career['fields']['random_table_wood_ogre_start'],
                                                  random_table_wood_ogre_end    = career['fields']['random_table_wood_ogre_end']
                                                  )
                careerObj.save()
        for trappings in models['WarhammerFantasyRoleplayVirtualGM_app.trapping']:
            trappingsObj = Trapping.objects.create(id=trappings['pk'],
                                                   name   = trappings['fields']['name'],
                                                   description   = trappings['fields']['description'],
                                                   encumbrance   = trappings['fields']['encumbrance'],
                                                   price   = trappings['fields']['price'],
                                                   availability   = trappings['fields']['availability'],
                                                   to_view   = trappings['fields']['to_view']
                                                   )
            trappingsObj.save()
        for status in models['WarhammerFantasyRoleplayVirtualGM_app.status']:
            statusObj = Status.objects.create(id=status['pk'],
                                              tier  = status['fields']['tier'],
                                              level  = status['fields']['level'],
                                              )
            statusObj.save()
        for careerpath in models['WarhammerFantasyRoleplayVirtualGM_app.careerpath']:
            careerpathObj = CareerPath(id=careerpath['pk'],
                                       status_id=careerpath['fields']['status']
                                       )
            careerpathObj.save()
            for s_id in careerpath['fields']['skills']:
                careerpathObj.skills.add(Skils.objects.get(id=s_id))
            for t_id in careerpath['fields']['talents']:
                careerpathObj.talents.add(Talent.objects.get(id=t_id))      
            for t_id in careerpath['fields']['trappings']:
                careerpathObj.trappings.add(Trapping.objects.get(id=t_id))
            careerpathObj.save()
        for careersadvancescheme in models['WarhammerFantasyRoleplayVirtualGM_app.careersadvancescheme']:
            careersadvanceschemeObj = CareersAdvanceScheme(id=careersadvancescheme['pk'],
            career_id                       = careersadvancescheme['fields']['career'],
            characteristics_ws_initial      = careersadvancescheme['fields']['characteristics_ws_initial'],
            characteristics_bs_initial      = careersadvancescheme['fields']['characteristics_bs_initial'],
            characteristics_s_initial       = careersadvancescheme['fields']['characteristics_s_initial'],
            characteristics_t_initial       = careersadvancescheme['fields']['characteristics_t_initial'],
            characteristics_i_initial       = careersadvancescheme['fields']['characteristics_i_initial'],
            characteristics_ag_initial      = careersadvancescheme['fields']['characteristics_ag_initial'],
            characteristics_dex_initial     = careersadvancescheme['fields']['characteristics_dex_initial'],
            characteristics_int_initial     = careersadvancescheme['fields']['characteristics_int_initial'],
            characteristics_wp_initial      = careersadvancescheme['fields']['characteristics_wp_initial'],
            characteristics_fel_initial     = careersadvancescheme['fields']['characteristics_fel_initial'],
            advances_level_1_id             = careersadvancescheme['fields']['advances_level_1'],
            advances_level_2_id             = careersadvancescheme['fields']['advances_level_2'],
            advances_level_3_id             = careersadvancescheme['fields']['advances_level_3'],
            advances_level_4_id             = careersadvancescheme['fields']['advances_level_4']
            )
            careersadvanceschemeObj.save()
        
        return super(RegressionTests, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        return super(RegressionTests, cls).tearDownClass()
    
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(self.username, self.email, self.password)
        self.user.save()

        self.player = Player.objects.create(user=self.user)
        self.player.save()
        
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
        
        super().setUp()
    
    def tearDown(self) -> None:
        self.player.delete()
        self.user.delete()
        super().tearDown()
    

    def test_simpleLogin(self):        
       
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

    def test_createNewCampaign(self):
        self.browser.find_element(by=By.LINK_TEXT, value="Create Campaign").click()
        
        campaign_name = self.browser.find_element(by=By.ID, value="id_user-name")
        party_name =  self.browser.find_element(by=By.ID, value="id_user-party_name")
        submit_button = self.browser.find_element(by=By.CLASS_NAME, value="button")

        campaign_name_txt = "test campaign name"
        campaign_name.send_keys(campaign_name_txt)
        party_name_txt = "test party name"
        party_name.send_keys(party_name_txt)
        submit_button.click()
        new_campaign_in_menu = self.browser.find_element(by=By.LINK_TEXT, value=campaign_name_txt)

        ambition_test = "Lorem ipsum dolor sit amet."        
        self.browser.find_element(by=By.ID, value="ambitions_shortterm").send_keys(ambition_test)
        self.browser.find_element(by=By.ID, value="submit_ambitions_shortterm").click()
        self.assertEqual(ambition_test, self.browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div/div[1]/div[1]/ol/li[1]').text)
        
        ambition_test = "Suspendisse consectetur orci sed pharetra ornare."
        self.browser.find_element(by=By.ID, value="ambitions_longterm").send_keys(ambition_test)
        self.browser.find_element(by=By.ID, value="submit_ambitions_longterm").click()
        self.assertEqual(ambition_test, self.browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div/div[2]/div[1]/ol/li[1]').text)
        
        self.browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div/div[4]/div/a').click()