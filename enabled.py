from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

enabled_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Enabled and disabled elements']"))
)
enabled_button.click()

assert "enabled" in driver.current_url

text_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "input"))
)
text_input.send_keys("hello world......!!")

time.sleep(5)

driver.quit()
