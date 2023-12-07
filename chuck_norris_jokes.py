from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class chuck_norris_jokes:
    """
    This class connect to Chuck Norris jokes website and returning an aray with all the page jokes
    """

    jokes_url = 'https://parade.com/968666/parade/chuck-norris-jokes/'


    @classmethod
    def get_chuck_norris_jokes(cls):

        options = webdriver.ChromeOptions()

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(executable_path="./chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(cls.jokes_url)
        driver.implicitly_wait(10)

        page_text = driver.find_element(By.XPATH, '//ol')

        jokes = page_text.text.split('\n')
        driver.quit()
        return jokes