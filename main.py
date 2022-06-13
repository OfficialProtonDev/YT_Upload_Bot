from distutils.command.upload import upload
from msilib.schema import PublishComponent
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exc
from selenium.webdriver.common.keys import Keys
import time
from dateutil.tz import *
import configparser

class YoutubeBot:
    def __init__(self):
        chrome_options = uc.ChromeOptions()

        chrome_options.add_argument("--disable-extensions")

        chrome_options.add_argument("--disable-popup-blocking")

        chrome_options.add_argument("--profile-directory=Default")

        chrome_options.add_argument("--disable-plugins-discovery")

        chrome_options.add_argument("user_agent=DN")

        self.driver = uc.Chrome(options=chrome_options)

        self.executor_url = self.driver.command_executor._url
        self.session_id = self.driver.session_id

    def findByID(self, ID):
        while True:
                try:
                    found = self.driver.find_element(by=By.ID, value=ID)
                    #print("found: " + ID)
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    #print("finding: " + ID)
                    time.sleep(1)
        return found

    def findByXPath(self, xpath):
        while True:
                try:
                    found = self.driver.find_element(by=By.XPATH, value=xpath)
                    #print("found: " + xpath)
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    #print("finding: " + xpath)
                    time.sleep(1)
        return found

    def findByName(self, name):
        while True:
                try:
                    found = self.driver.find_element(by=By.NAME, value=name)
                    #print("found: " + name)
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    #print("finding: " + name)
                    time.sleep(1)
        return found

    def googleLogin(self, mail_address, password):
        self.driver.get("https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

        emailid=self.driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        emailid.send_keys(mail_address)
        self.driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()

        time.sleep(3)

        passw=self.driver.find_element(by=By.XPATH, value="//input[@name='password']")
        passw.send_keys(password)
        self.driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()

        time.sleep(3)

    def upload_videos(self):
        config = configparser.ConfigParser()

        config.readfp(open(r'config.txt'))

        email = config.get('User-Settings', 'email')
        password = config.get('User-Settings', 'password')
        channel_studio_page = config.get('User-Settings', 'channel_studio_page')
        video_path = config.get('User-Settings', 'video_path')
        vid_title = config.get('User-Settings', 'vid_title')
        vid_desc = config.get('User-Settings', 'vid_desc')
        loops = config.get('User-Settings', 'loops')

        self.googleLogin(email, password)

        for _ in range(int(loops)):
            self.driver.get(channel_studio_page)

            # takes you to the upload page
            uploadButton = self.findByID("create-icon")
            uploadButton.click()

            # click upload button
            uploadButton2 = self.findByID("text-item-0")
            uploadButton2.click()    

            uploadFile = self.findByXPath("//input[@type='file']")
            uploadFile.send_keys(video_path)

            # input title
            titleInput = self.findByXPath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            titleInput.clear()
            titleInput.send_keys(vid_title)

            # input description
            descInput = self.findByXPath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            descInput.clear()
            descInput.send_keys(vid_desc)

            # input not for kids
            notForKidsToggle = self.findByName("VIDEO_MADE_FOR_KIDS_NOT_MFK")
            notForKidsToggle.click()           

            # click next button
            nextButton = self.findByID("next-button")
            nextButton.click()      

            # click next button
            nextButton = self.findByID("next-button")
            nextButton.click()        

            # click next button
            nextButton = self.findByID("next-button")
            nextButton.click()  

            # input public  
            privacyToggle = self.findByName("PUBLIC")
            privacyToggle.click()          

            # find publish button
            publishButton = self.findByID("done-button")

            # check if ready
            self.findByXPath("//div[contains(text(), 'Processing 99% ...')]")

            # click publish
            publishButton.click()              

            self.findByID("dialog-title")

            print('Uploaded video')

        print("All videos uploaded.")
        time.sleep(1)
        exit()


def main():
    bot = YoutubeBot()
    bot.upload_videos()



if __name__ == '__main__':
    main()
