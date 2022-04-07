from PageObject.HomePage import HomePage
from tests.test_basetest import BaseTest


class TestHomePage(BaseTest):

    def test_calculate_Monthly_Discretionary_Income(self):
        homePage = HomePage(self.driver)
        homePage.submitCustomerDetails('1960-01-01', 60000, 30000)
        assert homePage.calculate_Monthly_Discretionary_Income() == 2500
        assert homePage.calculate_Monthly_Discretionary_Income() > 0


