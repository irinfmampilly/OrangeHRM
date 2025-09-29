from selenium import webdriver
from pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.login("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()
    driver.quit()
