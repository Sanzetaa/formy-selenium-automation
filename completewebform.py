from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

webform_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Complete Web Form']"))
)
webform_button.click()

assert "form" in driver.current_url

firstname_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "first-name"))
)
firstname_input.send_keys("Sanjita")

lastname_input= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "last-name"))
)
lastname_input.send_keys("Adhikari")

jobtitle_input= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "job-title"))
)
jobtitle_input.send_keys("Student")

highschool_radio = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "radio-button-1"))
)
highschool_radio.click()

female_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkbox-2"))
)
female_check.click()

experience_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "select-menu"))
)
experience_button.click()
time.sleep(5)

value = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[@value='1']"))
)
value.click()
time.sleep(5)
 

date = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='datepicker']"))
)
date.send_keys(6/25/2026)

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@role='button']"))
)
submit_button.click()

assert "thanks" in driver.current_url

time.sleep(5)

driver.quit()
