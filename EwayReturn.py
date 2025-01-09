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

                 #split all and stor seprately
                doc_date_array = Doc_Date.split("/")
                Doc_Date_Year = doc_date_array[2]
                Doc_Date_Month = doc_date_array[1]
                Doc_Date_Date = doc_date_array[0]

                #find The Transport ID Field 
                Trans_ID_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblTransportor")
                # Store in Variable
                Trans_ID_Name = Trans_ID_element.text
                Transport_ID_list = Trans_ID_Name.split("&")
                Transport_ID = Transport_ID_list[0]

                print("\n Transport ID No is",Transport_ID)

                #Find the Vehicle Number
                TPT_ID_table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GVVehicleDetails")
                TPT_ID_tbody = TPT_ID_table.find_element(By.TAG_NAME,"tbody")
                TPT_tr_list = TPT_ID_tbody.find_elements(By.TAG_NAME,"tr")
                TPT_td_list = TPT_tr_list[1].find_elements(By.TAG_NAME,"td")
                Vehicle_Tripsheet = TPT_td_list[1].text

                #split the string to Seprate Vechicle Number With Tripsheet Number
                vehicle_Tripsheet_list = Vehicle_Tripsheet.split("&")

                #store first string after spliting it
                vehicle = vehicle_Tripsheet_list[0]
                
                print("\n vehicle No is",vehicle)

                # Scroll down the page
                body = driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.END)
                time.sleep(1)  # Wait for the page to load

                #Find More Detail Print Element
                More_Details = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btn_detail")
                More_Details.click()

                HSN_table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GVItemList")
                HSN_tbody = HSN_table.find_element(By.TAG_NAME,"tbody")
                HSN_tr_list = HSN_tbody.find_elements(By.TAG_NAME,"tr")

                Number_Of_HSNS = len(HSN_tr_list)
                #Now Loop To collect Hsn Code One By one 

                HSN_Code = []
                Quantity = []
                Taxable_Amount = []
                for HSN_index,HSN_element in enumerate(HSN_tr_list):
                      if(HSN_index == 0):
                        print("DO Noting")
                      else:
                        HSN_td_list = HSN_element.find_elements(By.TAG_NAME,"td")
                        HSN_Code.append(HSN_td_list[0].text)
                        Quantity_NOS = HSN_td_list[2].text
                        Quantity_NOS_Split = Quantity_NOS.split(".")
                        Quantity.append(Quantity_NOS_Split[0])
                        Taxable_Amount.append(HSN_td_list[3].text)
                print("all Done")
                print(HSN_Code)
                print(Quantity)
                print(Taxable_Amount)
                driver.get("https://ewaybillgst.gov.in/BillGeneration/BillGeneration.aspx")  

                doc_date_txt = driver.find_element(By.ID,"txtDocDate")
                doc_date_txt.click()

                calender_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
                calender_year.click()
                calender_year.send_keys(Doc_Date_Year)

                calender_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
                calender_month.click()
                calender_month.send_keys(Doc_Date_Month)

                """calender_date = driver.find_element(By.CLASS_NAME,"ui-datepicker-calendar")
                calender_date_tbody = calender_date.find_element(By.TAG_NAME,"tbody")
                calender_date_tr = calender_date_tbody.find_elements(By.TAG_NAME,"tr")

                calender_date_Picked = calender_date_tr(By.LINK_TEXT ,Doc_Date_Date)
                calender_date_Picked.click()"""



                time.sleep(10)


except NoAlertPresentException:
        print("You Fail TO fill CAthca On time")
