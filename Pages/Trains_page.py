from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from redbus_Automation.utils.locators_utils import (
    total_trains,
    ticket_class_arrow,
    row_class_xpath,
    recommended_block,
    recommended_card,
    card_train_timing,
    card_station_codes,
    card_full_timings,
)

class trains_page:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_results(self):
        self.wait.until(EC.visibility_of_element_located(total_trains))

    def open_ticket_class(self):
        self.driver.find_element(*ticket_class_arrow).click()

    def select_class_row(self, class_text):
        xpath = row_class_xpath.format(class_text)
        locator = (By.XPATH, xpath)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_for_recommended(self):
        self.wait.until(EC.visibility_of_element_located(recommended_block))

    def get_top_trains(self, top_n=2):
        self.wait_for_recommended()
        recommended = self.driver.find_element(*recommended_block)
        cards = recommended.find_elements(By.XPATH, recommended_card)
        top_cards = cards[:top_n]

        results = []

        for card in top_cards:
            info = (card.get_attribute("aria-label") or "").strip()
            train_name = info.split("Train Name:")[1].split(",")[0].strip()
            train_no = info.split("Train Number:")[1].split(",")[0].strip()
            dep_time = card.find_element(By.XPATH, card_train_timing).text.strip()
            station_codes = card.find_element(By.XPATH, card_station_codes).text.strip()
            duration = card.find_element(By.XPATH, card_full_timings).text.strip()

            results.append({
                "train_name": train_name,
                "train_no": train_no,
                "dep_time": dep_time,
                "station_codes": station_codes,
                "duration": duration
            })

        return results

    def print_top_trains(self, top_n=2):
        trains = self.get_top_trains(top_n)
        for idx, t in enumerate(trains, 1):
            print("==================================")
            print(f"Train {idx}:")
            print("Train Name :", t["train_name"])
            print("Train No   :", t["train_no"])
            print("Dep Time   :", t["dep_time"])
            print("Stations   :", t["station_codes"])
            print("Duration   :", t["duration"])
