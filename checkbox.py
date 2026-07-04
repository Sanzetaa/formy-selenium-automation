from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

checkbox_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Checkbox']"))
)
checkbox_button.click()

assert "checkbox" in driver.current_url

checkboxone_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkbox-1"))
)

if not checkboxone_button.is_selected():
    checkboxone_button.click()
assert checkboxone_button.is_selected()
print("checkboxone is selected")

checkboxtwo_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkbox-2"))
)

if not checkboxtwo_button.is_selected():
    checkboxtwo_button.click()
assert checkboxtwo_button.is_selected()
print("checkboxtwo is also selected")

checkboxthree_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkbox-3"))
)

if not checkboxthree_button.is_selected():
    checkboxthree_button.click()
assert checkboxthree_button.is_selected()
print("And lastly checkboxthree is also selected")

time.sleep(5)

driver.quit()
