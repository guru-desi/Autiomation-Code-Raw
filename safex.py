from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

PJ_No = [""]

driver = webdriver.Firefox()

driver.get("https://www.safexpress.com/")

cookie = driver.find_element(By.CLASS_NAME , "cc-allow")
cookie.click()

alert = driver.find_element(By.CLASS_NAME , "btn-close")
alert.click()

radio = driver.find_element(By.ID, "invoice_number")
radio.click()

for element in PJ_No:

    invoice_field = driver.find_element(By.CLASS_NAME, "waybill-tracking")
    invoice_field.clear()
    invoice_field.send_keys(element)

    submit = driver.find_element(By.CLASS_NAME, "track-button")
    submit.click()

    # Locate the specific div
    div_locator = (By.CLASS_NAME ,"text-start")
    wait = WebDriverWait(driver, 50)
    div_element = wait.until(EC.visibility_of_element_located(div_locator))

    # Locate the third span within the div
    span_elements = div_element.find_elements(By.TAG_NAME, 'span')
    if len(span_elements) >= 3:
        third_span = span_elements[2]
        third_span_text = span_elements[2].text
    else:
        print('There are less than 3 span elements within the div.')

    print("invoice",element,"wayBill",third_span_text)

