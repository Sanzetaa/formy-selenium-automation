from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/")

autocomplete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']"))
)
autocomplete_button.click()

assert "autocomplete" in driver.current_url

address_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "autocomplete"))
)
address_input.send_keys("Kathmandu, Nepal")

streetaddress_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "street_number"))
)
streetaddress_input.send_keys("Bafal 12 78")

streetaddress2_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "route"))
)
streetaddress2_input.send_keys("Sitapaila marga 234")

city_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "locality"))
)
city_input.send_keys("Kathmandu")

state_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "administrative_area_level_1"))
)
state_input.send_keys("Bagmati")

zipcode_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "postal_code"))
)
zipcode_input.send_keys("76532")

country_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "country"))
)
country_input.send_keys("Nepal")


time.sleep(5)

driver.quit()

