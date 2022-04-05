from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from datetime import datetime
import time

op = webdriver.ChromeOptions()
op.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(executable_path = "chromedriver.exe", options=op)

driver.get("https://www.dextools.io/app/bsc/pair-explorer/0x310ce2c28a74000904c44cbb523e3ffb0c0325a9")
driver.maximize_window()

now = datetime.now()

def start():
    btn1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/app-video-yt-modal/div[1]/button')))
    btn1.click()
    btn2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div/div[3]/app-favorites-list/div/div[1]/div/button')))
    btn2.click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, 240)")
    time.sleep(5)
    while True :

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S").replace(" ", "_").replace("/", "_").replace(":", "_")
        time.sleep(1)
        png = driver.get_screenshot_as_png()

        im = Image.open(BytesIO(png))

        left = 456
        top = 209
        right = 1842
        bottom = 842


        im = im.crop((left, top, right, bottom))
        im.save(f'{dt_string}.png')
        print("saved screenshot...")
        time.sleep(600)

start()