from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

keypress_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Key and Mouse Press']"))
)
keypress_button.click()

assert "keypress" in driver.current_url

fullname_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "name"))
)
fullname_input.send_keys("Sanjita Adhikari")

button_item = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='button']"))
)
button_item.click()

time.sleep(5)

driver.quit()
