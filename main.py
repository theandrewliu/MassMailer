# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# email to be spammed
target_email = "syntheticmangaming@gmail.com"

# Navigate to url
driver.get('https://www.nbc26.com/account/manage-email-preferences')
time.sleep(1)

# Wait for DOM to render
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'block'))

# enter email text
input_email = driver.find_element(by=By.ID, value='id_email')
input_email.send_keys(target_email)
print("newsletters email input")

# click newsletter checkboxes
breaking_news = driver.find_element(by=By.ID, value="8dd3e567-62dc-4aca-bc0c-9650de13aad4").click()
headlines = driver.find_element(by=By.ID, value="edac06c6-aa98-4904-98db-400d1d5fae99").click()
marketing = driver.find_element(by=By.ID, value="81e98b4e-4158-4760-9031-9c2d9e50b666").click()
weather_forecast = driver.find_element(by=By.ID, value="a53cc146-456f-4b57-b0dd-d10956a79963").click()

# click submit button
submit_btn = driver.find_element(by=By.CLASS_NAME, value="btn--primary.js-suh-submit")
submit_btn.click()

# wait for confirmation
time.sleep(1)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'form__note.is-success'))
print("Newsletters subscribed")

# Go to Weather Alerts section
driver.find_element(By.CLASS_NAME, 'button--text.suh-alerts').click()

# Wait for Dom to render
time.sleep(1)
WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, 'chosen-choices'))

# enter email text
input_email = driver.find_element(by=By.ID, value='id_email')
input_email.send_keys(target_email)
print("weather alerts email input")

# Activate the dropdown menu
driver.find_element(By.ID, "id_weather_alerts_chosen").click()
print("clicked the weather alerts box")

element = driver.find_element(By.CLASS_NAME, 'chosen-results')
elements = element.find_elements(By.TAG_NAME, 'li')

choices = len(elements)
i = 0
while i < choices:
    driver.find_element(By.ID, "id_weather_alerts_chosen").click()
    element = driver.find_element(By.CLASS_NAME, 'chosen-results')
    elements = element.find_elements(By.TAG_NAME, 'li')
    elements[i].click()
    i += 1

# click submit button
submit_btn = driver.find_element(by=By.CLASS_NAME, value="btn--primary.js-suh-submit")
submit_btn.click()
    
# wait for confirmation
time.sleep(1)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'form__note.is-success'))
print("Weather Alerts subscribed")

##
# Issue with clicking on items after index 11
##

# # Go to School Closings section
# driver.find_element(By.CLASS_NAME, 'button--text.suh-closings').click()

# # Wait for Dom to render
# time.sleep(3)
# WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, 'chosen-choices'))

# # enter email text
# input_email = driver.find_element(by=By.ID, value='id_email')
# input_email.send_keys(target_email)
# print("school closings email input")

# # Activate the dropdown menu
# driver.find_element(By.ID, "id_closings_delays_chosen").click()
# print("clicked the school closings box")

# element = driver.find_element(By.CLASS_NAME, 'chosen-results')
# elements = element.find_elements(By.TAG_NAME, 'li')

# choices = len(elements)
# i = 0

# while i < choices:
#     driver.find_element(By.CLASS_NAME, "col-md-three-fourths").click()
#     element = driver.find_element(By.CLASS_NAME, 'chosen-results')
#     elements = element.find_elements(By.TAG_NAME, 'li')
#     elements[i].click()
#     print(i)
#     i += 1

# print("caught up")