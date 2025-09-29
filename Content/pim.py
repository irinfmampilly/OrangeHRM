from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.XPATH, "//a[text()='Add Employee']")
        self.employee_list_button = (By.XPATH, "//a[text()='Employee List']")

    def click_add_employee(self):
        self.driver.find_element(*self.add_employee_button).click()

    def click_employee_list(self):
        self.driver.find_element(*self.employee_list_button).click()
