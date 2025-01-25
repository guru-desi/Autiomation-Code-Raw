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
print("Welcome! to Check Eway Validation")
print("Please Enter Username & Password For Login  ")
username = input("Please Enter Username: ")
password = input("Please Enter Password: ")

# Eway Which You Want a Print 
Eway_list = [351909661693,35109661693]

driver = webdriver.Edge()
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

        print("Ignore Previouse Message!!!")
        print("Log in Successfully Done!!!")
        print("Now Sit Back Crab Coffee!!! I'll Collect Validation Data For You ")


        for index,element in enumerate(Eway_list):

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

            try:
                alert = driver.switch_to.alert
                alert.accept()
                print("This Eway ",element,"is Invalid")   

            except NoAlertPresentException:

                time.sleep(2)

                valid_span = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_lblValidTo" )

                print("This Eway ",element,"is Valid For ",valid_span.text)


except NoAlertPresentException:
        print("You Fail TO fill CAthca On time")
