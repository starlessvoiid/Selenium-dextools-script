from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path = "chromedriver.exe")

driver.get("https://www.dextools.io/app/bsc/pair-explorer/0x310ce2c28a74000904c44cbb523e3ffb0c0325a9")

def start():

    try :
        time.sleep(10)
        btn1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/div[1]/span/div/i')))
        btn1.click()
        time.sleep(10)
        b2 =

    except :
        print("Oups, something went wrong...")