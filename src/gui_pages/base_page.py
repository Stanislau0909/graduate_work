from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
    def refresh_page(self):
        self.driver.refresh()

    def wait_for_text_in_element(self, element_xpath, expected_text, timeout=10):

        return Wait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, element_xpath), expected_text))
        # print(f"Текст '{expected_text}' найден в элементе с XPath '{element_xpath}'")


    def move_to_click(self, locator):
        """Перемещает курсор мыши к указанному элементу и кликает на него."""
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*locator)  # Распаковываем кортеж
        actions.move_to_element(element).click().perform()

    def element_is_visable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elemets_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def elemets_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elemets_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def upload_file(self, locator, file):
        self.driver.find_element(*locator).send_keys(file)

    def explicit_wait_to_be_clickable(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def explicit_wait_to_be_text_available(self, locator, text, timeout=10):
        return Wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))


    def actions_move_to_element(self):
        pass







    def wait_for(self, locator, timeout=10):
        try:
            element = Wait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not find"



    def wait_and_click(self,locator,timeout=10):
        try:
            element = Wait(self.driver,timeout).until(
                EC.element_to_be_clickable((By.XPATH,locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f'Element {locator} does not find'

