from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")

    def navigate_to_pim(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*self.pim_menu)
        ).click().perform()
