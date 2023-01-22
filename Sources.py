# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

class NBC26:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        # email to be spammed
        target_email = email
        
        # Navigate to url
        driver.get('https://www.nbc26.com/account/manage-email-preferences')
        time.sleep(1)

        # Wait for DOM to render
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'block'))

        # enter email text
        driver.find_element(by=By.ID, value='id_email').send_keys(target_email)

        # click newsletter checkboxes
        # breaking_news
        driver.find_element(by=By.ID, value="8dd3e567-62dc-4aca-bc0c-9650de13aad4").click()
        # headlines
        driver.find_element(by=By.ID, value="edac06c6-aa98-4904-98db-400d1d5fae99").click()
        # marketing
        driver.find_element(by=By.ID, value="81e98b4e-4158-4760-9031-9c2d9e50b666").click()
        # weather_forecast
        driver.find_element(by=By.ID, value="a53cc146-456f-4b57-b0dd-d10956a79963").click()

        # click submit button
        driver.find_element(by=By.CLASS_NAME, value="btn--primary.js-suh-submit").click()

        # wait for confirmation
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'form__note.is-success'))


        # Go to Weather Alerts section
        driver.find_element(By.CLASS_NAME, 'button--text.suh-alerts').click()

        # Wait for Dom to render
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, 'chosen-choices'))

        # enter email text
        driver.find_element(by=By.ID, value='id_email').send_keys(target_email)

        # Activate the dropdown menu
        driver.find_element(By.ID, "id_weather_alerts_chosen").click()

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
        driver.find_element(by=By.CLASS_NAME, value="btn--primary.js-suh-submit").click()
            
        # wait for confirmation
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'form__note.is-success'))
        driver.quit()
        print("Successfully subscribed to NBC26")

        
        # Issue with clicking on items after index 11
        

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

class CrossWalk:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        driver.get('https://www.crosswalk.com/newsletters/#for-men')
        time.sleep(1)

        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'NewsletterPage.group'))

        driver.find_element(By.CLASS_NAME, "emailAddress").send_keys(email)

        group = driver.find_element(By.CLASS_NAME, "NewsletterPage.group")
        columns = group.find_elements(By.CLASS_NAME, 'NewsletterColumn')
        for column in columns:
            for category in column.find_elements(By.CLASS_NAME, 'NewsletterCategory'):
                item = category.find_elements(By.CLASS_NAME, 'Item.group')
                for i in item:
                    i.find_element(By.CSS_SELECTOR, 'input').click()
        
        driver.find_element(By.CLASS_NAME, 'SubmitButton').click()
        driver.quit()
        print("Successfully subscribed to Crosswalk")

class HealthLine:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        driver.get('https://www.healthline.com/newsletter-signup')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'css-1q447m2'))

        driver.find_element(By.CLASS_NAME, "css-kljuul.hl-id-class").send_keys(email)

        unit = driver.find_elements(By.CLASS_NAME, "css-1q447m2")
        
        for box in unit:
            box.find_element(By.CLASS_NAME, "icon-hl-check.css-1dyq2cu").click()

        driver.find_element(By.CLASS_NAME, "hl-id-class.css-c6f4e9").click()
        driver.quit()
        print("Successfully subscribed to Healthline")

class NBCSanDiego:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcsandiego.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC SanDiego")

class NBCPhilly:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcphiladelphia.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Philadelphia")

class NBCWashington:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcwashington.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Washington")

class NBCBayArea:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcbayarea.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Bay Area")

class NBCChicago:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcchicago.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Chicago")
    
class NBCBoston:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcboston.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Boston")

class NBCDFW:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcdfw.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC DFW")
    
class NBCConnecticut:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcconnecticut.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Connecticut")

class NBCLosAngeles:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbclosangeles.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Los Angeles")

class NBCMiami:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcmiami.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC Miami")

class NBCNewYork:
    def __init__(self, email):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.nbcnewyork.com/newsletters/')
        time.sleep(1)
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'email'))

        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        time.sleep(3)
        try:
            if driver.find_element(By.ID, "fname").is_displayed():
                time.sleep(2)
                driver.find_element(By.ID, "fname").send_keys("ima")
                driver.find_element(By.ID, "lname").send_keys("loser")
                driver.find_element(By.ID, "zip").send_keys("12345")
                driver.find_element(By.CSS_SELECTOR, "label[for='gender-1']").click()
                driver.find_element(By.CLASS_NAME, "newsletters__button").click()
                time.sleep(2)
        except NoSuchElementException:
            pass

        elements = driver.find_elements(By.CLASS_NAME, "checkbox")
        for element in elements:
            element.find_element(By.CSS_SELECTOR, "label").click()
            continue
        
        driver.find_element(By.CLASS_NAME, "newsletters__button").click()
        driver.quit()
        print("Successfully subscribed to NBC New York")