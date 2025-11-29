from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import (
    suggestion_wrapper,
    search_category,
    suggestion_list_header,
    month_label,
    day_xpath,
    free_cancel_switch,
    search_trains_button,
)

class train_search_page:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def number_of_elements_to_be_more_than(self, locator, count):
        def _predicate(driver):
            elements = driver.find_elements(*locator)
            return elements if len(elements) > count else False
        return _predicate

    def select_location(self, location_text):
        self.wait.until(EC.visibility_of_element_located(suggestion_wrapper))

        active_input = self.driver.switch_to.active_element
        active_input.send_keys(location_text)

        search_list = self.wait.until(
            self.number_of_elements_to_be_more_than(search_category, 1)
        )

        location_search_result = search_list[0]
        location_list = location_search_result.find_elements(By.XPATH, suggestion_list_header)

        for location in location_list:
            full_text = (location.text or "").strip().lower()
            main_word = full_text.split(",")[0].split()[0]

            if main_word == location_text.lower():
                location.click()
                break

    def pick_date(self, target_month, target_day):
        month_xpath = "//p[contains(@class,'monthYear')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, month_xpath)))

        current_month = self.driver.find_element(By.XPATH, month_xpath).text

        while current_month != target_month:
            active_input = self.driver.switch_to.active_element
            active_input.click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, month_xpath)))
            current_month = self.driver.find_element(By.XPATH, month_xpath).text

        self.driver.find_element(By.XPATH, day_xpath.format(target_day)).click()

    def toggle_free_cancellation(self, flag):
        if str(flag).lower() == "yes":
            self.driver.find_element(*free_cancel_switch).click()

    def click_search(self):
        self.driver.find_element(*search_trains_button).click()
