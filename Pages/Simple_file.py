from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# python -m pytest redbus_Automation/Tests/test_search_trains.py --browser_name=edge --html=reports/report.html --self-contained-html -q -vv
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in")
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)
driver.find_element(By.XPATH, "(//img[@title='Online Train Tickets Booking'])").click()
driver.find_element(By.ID, "rails-search-widget-source").click()

def number_of_elements_to_be_more_than(locator, count):
    def _predicate(driver):
        elements = driver.find_elements(*locator)
        return elements if len(elements) > count else False
    return _predicate


def select_location(driver, wait, location_data):
    wrapper_locator = (By.XPATH, "//div[contains(@class,'suggestionInputWrapper')]")
    wait.until(EC.visibility_of_element_located(wrapper_locator))

    active_input = driver.switch_to.active_element
    active_input.send_keys(location_data)

    search_category_locator = (By.XPATH, "//div[contains(@class,'searchCategory')]")
    search_list = wait.until(number_of_elements_to_be_more_than(search_category_locator, 1))

    location_search_result = search_list[0]
    location_name_locator = ".//div[contains(@class,'listHeader')]"
    location_list = location_search_result.find_elements(By.XPATH, location_name_locator)

    for location in location_list:
        full_text = (location.text or "").strip().lower()
        main_word = full_text.split(",")[0].split()[0]

        if main_word == location_data.lower():
            location.click()
            break


select_location(driver, wait, "Delhi")

wrapper_locator = (By.XPATH, "//div[contains(@class,'suggestionInputWrapper')]")
wait.until(EC.visibility_of_element_located(wrapper_locator))

select_location(driver, wait, "Mumbai")


target_month = "January 2026"
target_day = "15"

month_xpath = "//p[contains(@class,'monthYear')]"
wait.until(EC.visibility_of_element_located((By.XPATH, month_xpath)))

current_month = driver.find_element(By.XPATH, month_xpath).text

while current_month != target_month:
    active_input = driver.switch_to.active_element
    active_input.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, month_xpath)))
    current_month = driver.find_element(By.XPATH, month_xpath).text

driver.find_element(By.XPATH, f"//span[text()='{target_day}']").click()

free_cancellation = "yes"
if free_cancellation == "yes":
    driver.find_element(By.ID, "switch").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Search Trains']").click()

# listed trains page=========================================

wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'totalTrain')]")))


Ticket_class_arw = driver.find_element(By.XPATH, "(//i[contains(@class,'trailingIcon___f3b32a icon icon-expand_more')])[2]")
Ticket_class_arw.click()

row_xpath = "//div[contains(@class,'listItem')][.//div[contains(@class,'listHeader') and contains(normalize-space(.), 'Sleeper')]]"
row = wait.until(EC.element_to_be_clickable((By.XPATH, row_xpath)))
row.click()

recommended_locator = (By.XPATH,"//div[contains(@class,'recommendedTrains')]")
wait.until(EC.visibility_of_element_located(recommended_locator))

recommended_locator = (By.XPATH, "//div[contains(@class,'recommendedTrains')]")
wait.until(EC.visibility_of_element_located(recommended_locator))
recommended = driver.find_element(*recommended_locator)

train_cards = recommended.find_elements(By.XPATH, ".//li[contains(@class,'srpCard')]")
top_two = train_cards[:2]

for card in top_two:

    info = card.get_attribute("aria-label").strip()
    train_name = info.split("Train Name:")[1].split(",")[0].strip()
    train_no = info.split("Train Number:")[1].split(",")[0].strip()
    dep_time = card.find_element(By.XPATH, ".//div[contains(@class,'trainTiming')]").text.strip()
    station_codes = card.find_element(By.XPATH, ".//div[contains(@class,'stationCodes')]").text.strip()
    full_timing_text = card.find_element(By.XPATH, ".//div[contains(@class,'timings')]").text.strip()

    print("==================================")
    print("Train Name :", train_name)
    print("Train No   :", train_no)
    print("Dep Time   :", dep_time)
    print("Stations   :", station_codes)
    print("Duration   :", full_timing_text)

