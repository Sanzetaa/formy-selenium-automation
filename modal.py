from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

modal_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Modal']"))
)
modal_button.click()

assert "modal" in driver.current_url

openmodal_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "modal-button"))
)
openmodal_button.click()

close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "close-button"))
)
close_button.click()

time.sleep(5)

driver.quit()
