from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from pynput import keyboard,mouse
from pynput.keyboard import Key, Controller

username = ""
password = ""

keyboard = Controller()

Eway_list = [""]

print("\n Total Eway Bill Print Will be",len(Eway_list))
print("@ First Print The Print DialogBox Freez for 30 Sec For Changing The Setting \n So Stick With Us...")

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

        print("\n")

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
                print("SR",index,"This Eway ",element,"is Invalid")   

            except NoAlertPresentException:

                time.sleep(2)

                # Find the GSt fields
                Gst_Number_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtSypplyTo")
                # Store in Variable
                Gst_number_name = Gst_Number_element.text
                Gst_number = Gst_number_name.split(" ,")
                Gst_number_NoSpace = Gst_number[0].replace(" ", "")

                print("\n GST No is",Gst_number_NoSpace)
                
                # Find the PJ NUmber fields
                PJ_Number_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblDocDet")
                # Store in Variable
                PJ_number = PJ_Number_element.text

                print("\n PJ_number No is",PJ_number)

                # Find the DocDate fields
                Doc_Date_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblDocDt")
                # Store in Variable
                Doc_Date = Doc_Date_element.text
                print("\n Doc_Date No is",Doc_Date)

                Trans_ID_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblTransportor")
                # Store in Variable
                Trans_ID_Name = Trans_ID_element.text
                Transport_ID_list = Trans_ID_Name.split("&")
                Transport_ID = Transport_ID_list[0]

                print("\n Transport ID No is",Transport_ID)

                Select_Table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GVVehicleDetails")
                Select_Tbody = Select_Table.find_element(By.TAG_NAME,"tbody")
                Select_TR_list = Select_Tbody.find_elements(By.TAG_NAME,"tr")
                Select_TD_list = Select_TR_list[1].find_elements(By.TAG_NAME,"td")
                Vehicle_Tripsheet = Select_TD_list[1].text
                vehicle_Tripsheet_list = Vehicle_Tripsheet.split("&")
                vehicle = Vehicle_Tripsheet_list[0]
                
                print("\n vehicle No is",vehicle)


except NoAlertPresentException:
        print("You Fail TO fill CAthca On time")
