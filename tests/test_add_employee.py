from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
import time

def test_add_employees():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    LoginPage(driver).login("Admin", "admin123")
    DashboardPage(driver).navigate_to_pim()
    pim = PIMPage(driver)

    employees = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Brown")]

    for first, last in employees:
        pim.click_add_employee()
        AddEmployeePage(driver).add_employee(first, last)
        time.sleep(2)

    driver.quit()
