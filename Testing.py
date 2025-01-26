from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from pynput import keyboard,mouse
from pynput.keyboard import Key, Controller

keyboard = Controller()
username = "PJ03_APLWB#1509"
password = "Asian@#321"

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

# Find the username and password input fields
password_field = driver.find_element(By.NAME, "txt_password")
# Enter the username and password
password_field.send_keys(password)

time.sleep(20)

try:
        # Switch to the alert
        alert = driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()
        print("\n")
        driver.get("https://ewaybillgst.gov.in/BillGeneration/BillGeneration.aspx")  

        doc_date_txt = driver.find_element(By.ID,"txtDocDate")
        doc_date_txt.click()
        time.sleep(3)

        calender_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
        calender_year.click()
        chars_year = "2023"
        for char1 in chars_year:
            keyboard.press(char1)
            keyboard.release(char1)
            time.sleep(0.1)  # Adjust the delay as needed

        calender_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
        calender_month.click()
        chars_month = "Jun"
        for char in chars_month:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.1)  # Adjust the delay as needed

        date = driver.find_element(By.CLASS_NAME,"ui-datepicker-calendar")
        tbody = date.find_element(By.TAG_NAME,"tbody")
        tr_date = tbody.find_elements(By.TAG_NAME,"tr")
        for index_tr_date,element_tr_date in enumerate(tr_date):
                td_date = element_tr_date.find_elements(By.TAG_NAME,"td")
                for index_td_date,element_td_date in enumerate(td_date):
                    try:   
                        td_text = element_td_date.find_element(By.CLASS_NAME,"ui-state-default")
                        if(td_text.text =="21"):
                            print("If Condition Executed", td_text.text)
                            td_text.click()
                            break
                        else:
                            print("Not Found Yet", element_td_date.text)

                    except NoSuchElementException:
                          print("Cell is Empty")
        time.sleep(30)
except NoAlertPresentException:
        print("You Fail TO fill CAthca On time")




