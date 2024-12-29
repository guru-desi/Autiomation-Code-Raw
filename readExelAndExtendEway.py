import os
import pandas as pd
from bs4 import BeautifulSoup
import json
from datetime import datetime
from time import sleep
from datetime import  timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import sys

# WELCOME FORM SHUBHAM THE CREATOR OF THIS SCRIPT
# THIS SCRIPT IS FOR EXTENDING EWAY BILL AUTOMATICALLY
print("Welcome to the Eway Bill Extension Script Gs Sidhu")
print("This script will extend the eway bill automatically")
print("This script will not run between 08:00:00 and 16:00:00")
print("If you want to run this script between 08:00:00 and 16:00:00, please change the time in the script")
print("This script will read the eway.csv file and extend the eway bill which is about to expire today")
#sleep(3)

""" current_time = datetime.now().strftime("%H:%M:%S")
if "08:00:00" <= current_time < "16:00:00":
    exit()
 """
def read_user_credentials(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    user_name = data['user_name']
    password = data['password']
    return user_name, password

file_path = './user.json'
user_name, password = read_user_credentials(file_path)
print(user_name, password)

#sys.exit()
def read_eway_csv(eway_file_path):
    eway_list = []
    try:
        df = pd.read_csv(eway_file_path, dtype=str)
        eway_list = df.to_dict(orient='records')
    except FileNotFoundError:
        print("File not found.")
    return eway_list

eway_file_path = './eway.csv'
eway_list = read_eway_csv(eway_file_path)
#print as json
#print(json.dumps(eway_list, indent=4))

def filter_eway_by_valid_until(eway_list):
    current_date = datetime.now()
    current_time = current_date.time()

    # If current time is between 00:00:00 and 08:00:00, consider the previous date
    if datetime.strptime("00:00:00", "%H:%M:%S").time() <= current_time and current_time < datetime.strptime("08:00:00", "%H:%M:%S").time():
        current_date = current_date - timedelta(days=1)
    
    current_date_str = current_date.strftime("%d/%m/%Y")
    
    eway_about_to_expire = [eway for eway in eway_list if eway.get("Valid Untill") == current_date_str]
    return eway_about_to_expire

eway_about_to_expire = filter_eway_by_valid_until(eway_list)
print(json.dumps(eway_about_to_expire, indent=4))
#sys.exit()
class extendEwayBill:
    def __init__(self):
        self.login_url = "https://ewaybillgst.gov.in/Login.aspx"
        self.txt_username = user_name
        self.txt_password = password
        log_file = "log.txt"
        # CHECK IF LOG FILE EXISTS THEN DELETE IT
        if os.path.exists(log_file):
            os.remove(log_file)

        eway_file = "eway.txt"
        # CHECK IF LOG FILE EXISTS THEN DELETE IT
        if os.path.exists(eway_file):
            os.remove(eway_file)

        self.list_eway_cum_vehicle = eway_about_to_expire
        self.driver = webdriver.Firefox()
        self.openLogin()
        self.driver.close()
    
    def openLogin(self):
        print(self.login_url)   
        self.driver.get(self.login_url)
        current_url = self.driver.current_url

        # FILL dooncarrying IN USER_NAME
        txt_username = self.driver.find_element(By.ID, "txt_username")
        txt_username.send_keys( self.txt_username )

        txt_password = self.driver.find_element(By.ID, "txt_password")
        txt_password.send_keys(self.txt_password)


        # refresh the page
        self.driver.refresh()

        sleep(1)

        txt_username = self.driver.find_element(By.ID, "txt_username")
        txt_username.send_keys( self.txt_username )

        sleep(1)

        txt_password = self.driver.find_element(By.ID, "txt_password")
        txt_password.send_keys(self.txt_password)


        while current_url != "https://ewaybillgst.gov.in/MainMenu.aspx" :
            sleep(1)
            current_url = self.driver.current_url
        self.list_eway_cum_vehicle = self.getPrintEwayAndFindCurrentVehicle() 

        print(json.dumps(self.list_eway_cum_vehicle,indent=4))

        self.write_eway_to_file()
        self.extendEway()

    def write_eway_to_file(self):
        with open("eway.txt", "w") as f:
            for eway in self.list_eway_cum_vehicle:
                f.write(eway.get("EWB.No") + "," + eway.get("vehicle_no") + "\n")
    def getPrintEwayAndFindCurrentVehicle(self): #this function will loop eway eway and go to its prinT and get its vehicle number and add it to the list
        for eway_nos_list in self.list_eway_cum_vehicle:
            link = 'https://ewaybillgst.gov.in/BillGeneration/EBPrint.aspx?cal=1'; #this is the link to print eway bill
            self.driver.get(link)

            eway_no = eway_nos_list.get("EWB.No")
            # fill in ctl00_ContentPlaceHolder1_txt_ebillno id
            txt_ebillno = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txt_ebillno")
            txt_ebillno.send_keys(eway_no)
            # click ctl00_ContentPlaceHolder1_btn_go
            btn_go = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btn_go")
            while True:
                try:
                    btn_go.click()
                    print("Go Button clicked")
                    break
                except:
                    print("Go Button not clicked")
                    continue
            # get vehicle number

            # find table with id ctl00_ContentPlaceHolder1_GVVehicleDetails
            try:
                ctl00_ContentPlaceHolder1_lblValidFrom = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblValidFrom")
                ctl00_ContentPlaceHolder1_lblValidFrom_text = ctl00_ContentPlaceHolder1_lblValidFrom.text # 06/08/2024 06:12 PM [347Kms] GET box [] text and stip Kms i want number only 347
                eway_nos_list["kilo_meters"] = int(ctl00_ContentPlaceHolder1_lblValidFrom_text.split('[')[1].split('Kms')[0]) - 2
                print('KM',eway_nos_list["kilo_meters"])

                table = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GVVehicleDetails")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # make it into soup
                soup = BeautifulSoup(table.get_attribute('outerHTML'), 'html.parser')
                # find 1 index row and 
                vehicle_row = soup.find_all('tr')[1]
                # find its 1 index column
                vehicle_column = vehicle_row.find_all('td')[1]
                # split with & 
                vehicle = vehicle_column.text.split('&')[0]
                #trime it
                # add it to the list
                eway_nos_list["vehicle_no"] = vehicle.strip()
                print(vehicle)
            except NoSuchElementException:
                print("Vehicle not found")
                continue

        
        return self.list_eway_cum_vehicle

    def extendEway(self):
        print(self.list_eway_cum_vehicle)
        #sys.exit()
        for eway_no_vehicle in self.list_eway_cum_vehicle:
            print(eway_no_vehicle)
            eway_no = eway_no_vehicle.get("EWB.No")
            vehicle = eway_no_vehicle.get("vehicle_no")
            kilo_meters = eway_no_vehicle.get("kilo_meters")
            self.driver.get("https://ewaybillgst.gov.in/BillGeneration/EwbExtension.aspx")

            eway = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txt_no")
            eway.send_keys(eway_no)
            #create ctl00_ContentPlaceHolder1_Btn_go
            btn_go = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Btn_go")
            
            while True:
                try:
                    btn_go.click()
                    print("Go Button clicked")
                    break
                except:
                    print("Go Button not clicked")
                    continue
            #scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            while True:
                try:
                    rbn_extent_0 = self.driver.find_element(By.ID, "rbn_extent_0")
                    break
                except NoSuchElementException:
                    continue
            
            while True:
                try:
                    rbn_extent_0.click()
                    print("Radio clicked")
                    break
                except:
                    print("Radio not clicked")
                    continue
            
            while True:
                try:
                    ddl_extend_select = Select( self.driver.find_element(By.ID, "ddl_extend") )
                    break
                except NoSuchElementException:
                    continue
            
            ddl_extend_select.select_by_value('4')
            txtRemarks = self.driver.find_element(By.ID, "txtRemarks")
            txtRemarks.send_keys("Transhipment")

            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # GET VALUE OF txtFromPincode
            txtFromPincode = self.driver.find_element(By.ID, "txtFromPincode").get_attribute("value")
            #GET text of selected option of slFromState
            slFromState = Select(self.driver.find_element(By.ID, "slFromState")).first_selected_option.text
            # FILL txt_vehFromPlace WITH slFromState
            txt_vehFromPlace = self.driver.find_element(By.ID, "txt_vehFromPlace")
            txt_vehFromPlace.send_keys(slFromState)
            
            txtFromEnteredPinCode = self.driver.find_element(By.ID, "txtFromEnteredPinCode")
            txtFromEnteredPinCode.send_keys(txtFromPincode)
            
            while True:
                try:
                    ctl00_ContentPlaceHolder1_txtDocNo = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtDocNo").get_attribute("value")
                    break
                except NoSuchElementException:
                    continue

            # GET ctl00_ContentPlaceHolder1_txtDocNo VALUE
            
            txtDocDate = self.driver.find_element(By.ID, "txtDocDate").get_attribute("value")
            print(ctl00_ContentPlaceHolder1_txtDocNo)

            
            ctl00_ContentPlaceHolder1_txtVehicleNo = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtVehicleNo")
            ctl00_ContentPlaceHolder1_txtVehicleNo.send_keys(vehicle)

            ctl00_ContentPlaceHolder1_txtTransDocNo = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtTransDocNo")
            ctl00_ContentPlaceHolder1_txtTransDocNo.send_keys(txtDocDate)


            txtDistance = self.driver.find_element(By.ID, "txtDistance")
            #clear the text box
            sleep(2)
            txtDistance.clear()
            txtDistance.send_keys(kilo_meters)
            

            while True:
                try:
                    btnsbmt = self.driver.find_element(By.ID, "btnsbmt")
                    print("btnsbmt found")
                    break
                except NoSuchElementException:
                    print("btnsbmt not found")
                    continue
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            while True:
                try:
                    btnsbmt.click()
                    print("btnsbmt clicked")
                    break
                except:
                    print("btnsbmt not clicked")
                    continue
            # Wait until next page has loaded 
            current_url = self.driver.current_url
            start_time = datetime.now()
            while True:
                try:
                    sleep(1)
                    current_url = self.driver.current_url
                    print(current_url)
                    if current_url == "https://ewaybillgst.gov.in/BillGeneration/EwbExtension.aspx":
                        #append eway_no in log.txt with status failed
                        current_time = datetime.now()
                        elapsed_time = (current_time - start_time).total_seconds()
                        # if current_time - start_time > 30 seconds breack 
                        if elapsed_time > 30:
                            with open("log.txt", "a") as f:
                                f.write(eway_no + ",failed\n")
                            break
                    else:
                        #append eway_no in log.txt with status success
                        with open("log.txt", "a") as f:
                            f.write(eway_no + ",success\n")
                        
                        break
                except:
                    continue
         
object = extendEwayBill()


