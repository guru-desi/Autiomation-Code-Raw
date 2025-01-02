from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

PJ_No = ["PJ2401260251","PJ2401260248","PJ2401260249","PJ2401260253","PJ2401260291","PJ2401260450","PJ2401260494","PJ2401260489","PJ2401260491","PJ2401260493","PJ2401260495","PJ2401260504","PJ2401260507","PJ2401260594","PJ2401260602","PJ2401260252","PJ2401260603","PJ2401260122","PJ2401260029","PJ2401260052","PJ2401260100","PJ2401260199","PJ2401260632","PJ2401260130","PJ2401260197","PJ2401260028","PJ2401260103","PJ2401260128","PJ2401259763","PJ2401260027","PJ2401260030","PJ2401260595","PJ2401260023","PJ2401259781","PJ2407001215","PJ2407001216","PJ2401259994","PJ2401259991","PJ2401260000","PJ2401260025","PJ2401260026","PJ2401260041","PJ2401260039","PJ2401260043","PJ2401260042","PJ2401260091","PJ2401260123","PJ2401261784","PJ2401261326","PJ2401261836","PJ2401261835","PJ2407001219","PJ2401261726","PJ2401261692","PJ2401261686","PJ2401261679","PJ2401261508","PJ2401261509","PJ2401261317","PJ2401261315","PJ2401261311","PJ2401261313","PJ2401261303","PJ2401261302","PJ2401261266","PJ2401260703","PJ2401260732","PJ2401260747","PJ2401260816","PJ2401260847","PJ2401260879","PJ2401260933","PJ2401260928","PJ2401260992","PJ2401260995","PJ2401261158","PJ2401261161","PJ2401261163","PJ2401261219","PJ2401261220","PJ2401261216","PJ2401261226","PJ2401261242","PJ2401260291","PJ2401260450","PJ2401260494","PJ2401260489","PJ2401260491","PJ2401260493","PJ2401260495","PJ2401260504","PJ2401260507","PJ2401260594","PJ2401260602","PJ2401260252","PJ2401260603","PJ2401260253","PJ2401260249","PJ2401260248","PJ2401260251","PJ2407001216","PJ2407001215","PJ2401259781","PJ2401261783"]

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

    time.sleep(2)

    submit = driver.find_element(By.CLASS_NAME, "track-button")
    submit.click()

    # Locate the specific div
    try:
        div_locator = (By.CLASS_NAME ,"text-start")
        wait = WebDriverWait(driver, 20)
        div_element = wait.until(EC.visibility_of_element_located(div_locator))
        
        # Locate the third span within the div
        span_elements = div_element.find_elements(By.TAG_NAME, 'span')
        if len(span_elements) >= 3:
            third_span = span_elements[2]
            third_span_text = span_elements[2].text
            no_space_string = third_span_text.replace(" ", "")
        else:
            print('There are less than 3 span elements within the div.')

        print("invoice",element,"wayBill",no_space_string)

    except Exception as e:
        print("invoice",element,"wayBill Unable_To_load")



