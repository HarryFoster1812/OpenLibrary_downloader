from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import keyboard
from convert import *

s=Service(ChromeDriverManager().install())

def opensite():
    site = input("Site: ")
    driver = webdriver.Chrome(service=s)
    driver.get("https://openlibrary.org/account/login")

    username = driver.find_element_by_id('username')
    username.send_keys('tdonlkuyrunqizgdzi@kvhrr.com')

    password = driver.find_element_by_id('password')
    password.send_keys('QAZ123wsx456edc789,' + Keys.RETURN)

    time.sleep(5)
    driver.get(site)

    borrowbook(driver)

def borrowbook(driver):
    driver.find_elements_by_class_name("cta-btn--borrow")[0].click()
    time.sleep(10)
    gatherlinks(driver)

def gatherlinks(driver):
    links = []

    driver.find_element_by_class_name("onepg").click()
    nextbutton = driver.find_element_by_class_name("book_flip_next")
    length = driver.find_element_by_class_name("BRcurrentpage").get_attribute("innerText").split("of ")[1].strip(")")
    for i in range(int(length)-1):

        links.append(driver.find_element_by_class_name(f"pagediv{i+1}").find_element_by_class_name("BRpageimage").get_attribute('src'))
        nextbutton.click()
        time.sleep(1)
    
    download_images(driver, links, length)

def download_images(driver, links, length):
    for i in enumerate(links):
        driver.get(i[1])

        location = str(pyautogui.position()).strip("Point(x=").strip(")").split(", y=")
        location[0], location[1] = int(location[0])+78, int(location[1])+48
        
        pyautogui.click(button='right')
        pyautogui.click(x=location[0], y=location[1])
        time.sleep(0.5)
        pyautogui.click(x=807, y=59)
        keyboard.send("ctrl+a")
        keyboard.send("\b")
        keyboard.write("Documents\Programming\Python Scripts\Projects\OpenLibrary_downloader\Images")
        keyboard.send('enter')
        pyautogui.click(x=516, y=586)
        keyboard.write(f"pic{str(i[0]).zfill(len(length))}")
        pyautogui.click(x=995, y=679)
    convert()

def convert():
    images = initialise_images()
    SaveAsPdf(images)
    delete_files()

if  __name__== "__main__":
    opensite()