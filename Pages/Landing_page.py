from utils.locators_utils import train_icon

class landing_page:
    def __init__(self, driver):
        self.driver = driver

    def open_train_booking(self):
        self.driver.find_element(*train_icon).click()
