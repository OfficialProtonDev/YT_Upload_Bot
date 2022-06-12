from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exc
from selenium.webdriver.common.keys import Keys
import time
from dateutil.tz import *
import os
import sys

mail_address = ''
password = ''
channel_studio_page = ''

vid_title = ""

loops = 5

class TikTokBot:
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
        print(self.executor_url, self.session_id)

    def upload_video(self):

        self.driver.get("https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

        emailid=self.driver.find_element(by=By.XPATH, value="//input[@name='identifier']")
        emailid.send_keys(mail_address)
        self.driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()
        

        time.sleep(3)

        passw=self.driver.find_element(by=By.XPATH, value="//input[@name='password']")
        passw.send_keys(password)
        self.driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']").click()

        time.sleep(3)

        for _ in range(loops):
            self.driver.get(channel_studio_page)

            path = r"C:\YT_Bot\qauz3i.mp4"

            time.sleep(1)

            # takes you to the upload page
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="create-icon").click()
                    print("clicked create button")
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    print("finding create button")
                    time.sleep(1)
      

                # click upload button
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="text-item-0").click()
                    print("clicked upload button")
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    print("finding upload button")
                    time.sleep(1)      

            while True:
                try:
                    s = self.driver.find_element(by=By.XPATH, value="//input[@type='file']")
                    s.send_keys(path)
                    print("sent file")
                    break
                except exc.NoSuchElementException or exc.ElementClickInterceptedException:
                    print("finding upload file button")
                    time.sleep(1)

                # input title
            while True:
                try:
                    s = self.driver.find_element(by=By.ID, value="textbox")
                    s.clear()
                    s.send_keys(vid_title)
                    print("sent title")
                    break
                except exc.NoSuchElementException:
                    print("finding title")
                    time.sleep(1)  

            # input not for kids
            while True:
                try:
                    self.driver.find_element(by=By.NAME, value="VIDEO_MADE_FOR_KIDS_NOT_MFK").click()
                    print("set nfk")
                    break
                except exc.NoSuchElementException or exc.ElementNotInteractableException:
                    print("finding nfk toggle")
                    time.sleep(1)            

                # click next button
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="next-button").click()
                    print("clicked next button")
                    break
                except exc.NoSuchElementException:
                    print("finding next button")
                    time.sleep(1)     

                # click next button
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="next-button").click()
                    print("clicked next button")
                    break
                except exc.NoSuchElementException:
                    print("finding next button")
                    time.sleep(1)        

            # click next button
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="next-button").click()
                    print("clicked next button")
                    break
                except exc.NoSuchElementException:
                    print("finding next button")
                    time.sleep(1)   

                # input public     
            while True:
                try:
                    self.driver.find_element(by=By.NAME, value="PUBLIC").click()
                    print("set public")
                    break
                except exc.NoSuchElementException or exc.ElementNotInteractableException:
                    print("finding privacy toggle")
                    time.sleep(1)      

            time.sleep(10)

            # click publish button
            while True:
                try:
                    self.driver.find_element(by=By.ID, value="done-button").click()
                    print("clicked publish button")
                    break
                except exc.NoSuchElementException or exc.ElementNotInteractableException:
                    print("finding publish button")
                    time.sleep(1)               

            while True:
                try:
                    self.driver.find_element(by=By.ID, value="dialog-title")
                    break
                except exc.NoSuchElementException or exc.ElementNotInteractableException:
                    print("waiting")
                    time.sleep(1)  

            print('done')

            time.sleep(1)

        time.sleep(5)
        exit()


def main():
    bot = TikTokBot()
    bot.upload_video()



if __name__ == '__main__':
    main()
