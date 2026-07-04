from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

buttons_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Buttons")
    )
)
buttons_link.click()

primary_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Primary']"))
)
primary_button.click()

success_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Success']"))
)
success_button.click()

info_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Info']"))
)
info_button.click()

warning_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Warning']"))
)
warning_button.click()

danger_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Danger']"))
)
danger_button.click()

link_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Link']"))
)
link_button.click()

left_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Left']"))
)
left_button.click()

middle_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Middle']"))
)
middle_button.click()

right_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Right']"))
)
right_button.click()

one_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1']"))
)
one_button.click()

two_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='2']"))
)
two_button.click()

dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
)
dropdown_button.click()

dropdownlinkone_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 1']"))
)
dropdownlinkone_button.click()

assert "buttons#" in driver.current_url

driver.get("https://formy-project.herokuapp.com/buttons")

dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
)
dropdown_button.click()


dropdownlinktwo_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 2']"))
)
dropdownlinktwo_button.click()


time.sleep(5)

driver.quit()




