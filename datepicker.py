from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

datepicker_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Datepicker']"))
)
datepicker_button.click()

assert "datepicker" in driver.current_url

date_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "datepicker"))
)
date_input.send_keys("06/24/2026")

time.sleep(5)

driver.quit()
