from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

# Code TO Fetch Username And PassWord From User at Realtime 
# Asking the user for Username & Password
#print("Welcome! to Regular Printing bill System")
#print("Please Enter Username & Password For Login  ")
input("Please Enter Username: ")
input("Please Enter Password: ")

# Eway Which You Want a Print 
Eway_list = []

driver = webdriver.Firefox()
driver.get("https://ewaybillgst.gov.in/Login.aspx")

# Find the username and password input fields
username_field = driver.find_element(By.NAME, "txt_username")
password_field = driver.find_element(By.NAME, "txt_password")

# Enter the username and password
username_field.send_keys(username)
password_field.send_keys(password)

driver.refresh()
time.sleep(1)

# Find the username and password input fields
username_field = driver.find_element(By.NAME, "txt_username")
# Enter the username and password
username_field.send_keys(username)
time.sleep(1)

# Find the username and password input fields
password_field = driver.find_element(By.NAME, "txt_password")
# Enter the username and password
password_field.send_keys(password)


time.sleep(15)
try:
        # Switch to the alert
        alert = driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()
        driver.get("https://ewaybillgst.gov.in/BillGeneration/EBPrint.aspx?cal=1")


        for element in Eway_list:

            time.sleep(2)
            driver.get("https://ewaybillgst.gov.in/BillGeneration/EBPrint.aspx?cal=1")

            # Find the Extend input fields
            Extend_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txt_ebillno")
            # Enter the Extend Eway
            Extend_field.send_keys(element)

            time.sleep(1)

            # Find the Go or Enter fields
            login_button = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btn_go")

            # This WIll make Action
            login_button.click()

            time.sleep(2)
            # Scroll down the page
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.END)
            time.sleep(1)  # Wait for the page to load

            link = driver.find_element(By.LINK_TEXT, 'Print')
            # To Click on it, just call click method:
            link.click()

            # Find the Submit or Enter fields
            #submit_button = driver.find_element(By.ID, "btnsbmt")

            # This WIll make Action
            #submit_button.click()

except NoAlertPresentException:
        print("You Fail TO fill CAthca On time")