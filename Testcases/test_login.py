import allure

from pages.loginpage import LoginPage

def test_login(setup):
    driver, user, passw = setup
    lpage = LoginPage(driver)
    lpage.login(user,passw)
    #assert "Dashboard" in setup.title
    print("successful")