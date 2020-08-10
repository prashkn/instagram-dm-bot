from selenium import webdriver
from time import sleep

#replace some of the strings with your own messages

class IGbot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')\
            .click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')\
            .click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')\
            .send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')\
            .click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[3]')\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[5]/a')\
            .click()
        sleep(1)
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonlikes1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtoncomments1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtoncomment_likes1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonlike_and_comment_on_photo_user_tagged1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonfollow_request_accepted1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtoncontact_joined1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonpending_direct_share1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtondirect_share_activity1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonnotification_reminders1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonfirst_post1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonview_count1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonreport_updated1']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][id='igCoreRadioButtonlive_broadcast1']").click()
        sleep(1)
        self.driver.get("https://www.instagram.com/accounthere/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        for x in range(20):
            self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')\
                .send_keys('messagehere')
            self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')\
                .click()
            sleep(0.75)


IGbot('usernamehere', 'passwordhere')

