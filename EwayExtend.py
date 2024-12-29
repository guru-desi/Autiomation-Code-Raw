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
print("Welcome! to Auto Eway bill Extend System")
print("Please Enter Username & Password For Login  ")
username = input("Please Enter Username: ")
password = input("Please Enter Password: ")

#Other Some PreDefined Variables You Can Change As You Wished 
remark = ""
current_palace = ""
current_pincode = ""
vehicle = ""

Eway_list = [1,2,5,3]

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

for element in Eway_list:


    time.sleep(2)
    driver.get("https://ewaybillgst.gov.in/BillGeneration/EwbExtension.aspx")

    # Find the Extend input fields
    Extend_field = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_no")
    # Enter the Extend Eway
    Extend_field.send_keys(element)

    time.sleep(1)

    # Find the Go or Enter fields
    login_button = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$Btn_go")

    # This WIll make Action
    login_button.click()

    time.sleep(2)  

    #Checking Eway Is Extendable Or Not 

    #You can't extend this EWB as extension is allowed only 8 hours before expiry of validity time of EWB..!!

    try:
        # Switch to the alert
        alert = driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()
        print("Alert was present Please Check This Eway",element)
        driver.get("https://ewaybillgst.gov.in/BillGeneration/EwbExtension.aspx")

    except NoAlertPresentException:        
        # Scroll down the page
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)  # Wait for the page to load

        # Locate and click the radio button
        radio_button = driver.find_element(By.ID, 'rbn_extent_0')  # Replace with the actual ID of the radio button
        radio_button.click()
        # Scroll down the page
       # body = driver.find_element(By.TAG_NAME, 'body')
       # body.send_keys(Keys.PAGE_DOWN)
       # time.sleep(2)  # Wait for the page to load

        # Locate the  element by its ID
        dropdown_element = driver.find_element(By.ID, "ddl_extend")

        # Create a Select object
        dropdown = Select(dropdown_element)

        # Select an option by visible text
        dropdown.select_by_visible_text("Transhipment")

        # Alternatively, select an option by its value attribute
        # dropdown.select_by_value("VALUE_OF_OPTION")

        # Or select an option by its index (0-based)
        # dropdown.select_by_index(INDEX_OF_OPTION)

        # Find the Remark input fields
        Extend_field = driver.find_element(By.ID, "txtRemarks")
        # Enter the Remark
        Extend_field.send_keys(remark)

        time.sleep(1)

        # Find the Place input fields
        Extend_field = driver.find_element(By.ID, "txt_vehFromPlace")
        # Enter the Place
        Extend_field.send_keys(current_palace)

        time.sleep(1)

        # Find the PinCode input fields
        Extend_field = driver.find_element(By.ID, "txtFromEnteredPinCode")
        # Enter the pincode
        Extend_field.send_keys(current_pincode)

        time.sleep(1)

        # Find the Vehicle input fields
        Extend_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtVehicleNo")
        # Enter the Vehicle
        Extend_field.send_keys(vehicle)

        time.sleep(1)

        # Locate and click the radio button
        radio_button = driver.find_element(By.ID, 'rbn_extent_0')  # Replace with the actual ID of the radio button
        radio_button.click()

        time.sleep(1)

        # Scroll down the page
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.END)
        time.sleep(1)  # Wait for the page to load


        # Find the Submit or Enter fields
        submit_button = driver.find_element(By.ID, "btnsbmt")

        # This WIll make Action
        submit_button.click()
        time.sleep(5)

        print("Eway",element,"is Extended")    

    