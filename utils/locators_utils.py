from selenium.webdriver.common.by import By

train_icon = (By.XPATH, "(//img[@title='Online Train Tickets Booking'])")

source_input = (By.ID, "rails-search-widget-source")
dest_input = (By.ID, "rails-search-widget-destination")

suggestion_wrapper = (By.XPATH, "//div[contains(@class,'suggestionInputWrapper')]")
search_category = (By.XPATH, "//div[contains(@class,'searchCategory')]")
suggestion_list_header = ".//div[contains(@class,'listHeader')]"

month_label = (By.XPATH, "//p[contains(@class,'monthYear')]")
day_xpath = "//span[text()='{}']"

free_cancel_switch = (By.ID, "switch")
search_trains_button = (By.XPATH, "//button[normalize-space()='Search Trains']")

total_trains = (By.XPATH, "//span[contains(@class,'totalTrain')]")

ticket_class_arrow = (By.XPATH, "(//i[contains(@class,'trailingIcon___f3b32a icon icon-expand_more')])[2]")

row_class_xpath = ("//div[contains(@class,'listItem')][.//div[contains(@class,'listHeader') "
                   "and contains(normalize-space(.), '{}')]]")

recommended_block = (By.XPATH, "//div[contains(@class,'recommendedTrains')]")
recommended_card = ".//li[contains(@class,'srpCard')]"

card_train_timing = ".//div[contains(@class,'trainTiming')]"
card_station_codes = ".//div[contains(@class,'stationCodes')]"
card_full_timings = ".//div[contains(@class,'timings')]"
