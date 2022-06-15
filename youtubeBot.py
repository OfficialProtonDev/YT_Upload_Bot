from distutils.command.upload import upload
from fileinput import close
from msilib.schema import PublishComponent
from xml.etree.ElementTree import tostring
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exc
from selenium.webdriver.common.keys import Keys
import time
from dateutil.tz import *
import time


class YoutubeBot:
    def __init__(self, email, password, vid_path, vid_title, vid_desc, loops):

        self.email = email
        self.password = password
        self.vid_path = vid_path
        self.vid_title = vid_title
        self.vid_desc = vid_desc
        self.loops = loops

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

    def googleLogin(self):
        self.driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fstudio.youtube.com%252F&hl=en&passive=false&service=youtube&uilel=0&flowName=GlifWebSignIn&flowEntry=AddSession")

        emailid = self.driver.find_element(
            by=By.XPATH, value="//input[@name='identifier']")
        emailid.send_keys(self.email)
        self.driver.find_element(
            by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()

        time.sleep(3)

        passw = self.driver.find_element(
            by=By.XPATH, value="//input[@name='password']")
        passw.send_keys(self.password)
        self.driver.find_element(
            by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()

        time.sleep(3)

    def attemptClickUntilXPATHFound(self, element, path):
        while True:
            try:
                found = self.driver.find_element(by=By.XPATH, value=path)
                #print("found it")
                break
            except exc.NoSuchElementException:
                #print("not done click again")
                self.tryClick(element)
                time.sleep(0.1)
        return found

    def tryClick(self, element):
        try:
            element.click()
        except exc.ElementClickInterceptedException or exc.ElementNotInteractableException or exc.ElementNotVisibleException or exc.NoSuchElementException:
            pass

    def upload_videos(self):
        self.googleLogin()

        for _ in range(int(self.loops)):
            # takes you to the upload page
            uploadButton = self.findByID("create-icon")
            self.tryClick(uploadButton)

            start_time = time.time()

            # click upload button
            uploadButton2 = self.findByID("text-item-0")
            self.tryClick(uploadButton2)

            uploadFile = self.findByXPath("//input[@type='file']")
            uploadFile.send_keys(self.vid_path)

            # input title
            titleInput = self.findByXPath(
                "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            titleInput.clear()
            titleInput.send_keys(self.vid_title)

            # input description
            descInput = self.findByXPath(
                "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            descInput.clear()
            descInput.send_keys(self.vid_desc)

            # input not for kids
            notForKidsToggle = self.findByName("VIDEO_MADE_FOR_KIDS_NOT_MFK")
            self.tryClick(notForKidsToggle)

            # click next button
            nextButton = self.findByID("next-button")

            privacyToggle = self.attemptClickUntilXPATHFound(
                nextButton, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")

            # input public
            self.tryClick(privacyToggle)

            # find publish button
            publishButton = self.findByID("done-button")

            # check if processing
            self.findByXPath(
                "//div[contains(text(), 'Processing will begin shortly')]")

            # click publish until the close button appears
            closeButton = self.attemptClickUntilXPATHFound(
                publishButton, "/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button")

            # click the close button
            self.tryClick(closeButton)

            finish_time = time.time() - start_time

            print('Uploaded video in ', finish_time)

        print("All videos uploaded")
        exit()