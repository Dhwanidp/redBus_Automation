from Pages.Landing_page import landing_page
from Pages.Search_page import train_search_page
from Pages.Trains_page import trains_page
from utils.locators_utils import source_input
import pytest
@pytest.mark.usefixtures("setup")
class TestSearchTrains:
    def test_searching_trains(self, test_data ,driver):
        driver = self.driver

        landing = landing_page(driver)
        landing.open_train_booking()

        search = train_search_page(driver)
        trains = trains_page(driver)
        driver.find_element(*source_input).click()
        results_all = []

        for tc in test_data:
            search.select_location(tc["from"])
            search.select_location(tc["to"])
            search.pick_date(tc["target_month"], tc["target_day"])
            search.toggle_free_cancellation(tc.get("free_cancellation", "no"))

            search.click_search()

            trains.wait_for_results()
            trains.open_ticket_class()
            trains.select_class_row(tc.get("ticket_class_contains", "Sleeper"))

            top_n = tc.get("top_n", 2)
            top_trains = trains.get_top_trains(top_n)
            results_all.append({tc.get("test_name", "case"): top_trains})

            for idx, t in enumerate(top_trains, 1):
                print("==================================")
                print(f"Test Case : {tc.get('test_name')}")
                print(f"Train {idx}:")
                print("Train Name :", t["train_name"])
                print("Train No   :", t["train_no"])
                print("Dep Time   :", t["dep_time"])
                print("Stations   :", t["station_codes"])
                print("Duration   :", t["duration"])

