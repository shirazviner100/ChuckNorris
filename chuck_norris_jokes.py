from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from file_helper import file_helper

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
        
        try:
            driver.get(cls.jokes_url)
            driver.implicitly_wait(10)

            page_text = driver.find_element(By.XPATH, '//ol')
            jokes = page_text.text.split('\n')

            #saving the jokes to have the most update copy of the list
            if len(jokes) > 0 : file_helper.save_array_to_file(jokes, "./data/data.txt")
            return jokes
        
        except:
            #in case that webdriver.get access deny we get the jokes from file saved local in the server
            #appends only on testing ood when we send a lot of request to this website
            return file_helper.read_array_from_file("data/data.txt")
        finally:
            driver.quit()