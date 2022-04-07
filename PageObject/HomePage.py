from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    DOB = (By.XPATH, "DOB")
    YEARLY_NET_SALARY = (By.XPATH, "YEARLY_NET_SALARY")
    YEARLY_EXPENDITURE = (By.XPATH, "YEARLY_EXPENDITURE")
    SUBMIT = (By.XPATH, "SUBMIT")
    yearlyNetIncome = 0
    yearlyExpenditure = 0

    def submitCustomerDetails(self, dob, yearly_net_income, yearly_expenditure):
        self.enter_text(self.DOB, dob)
        self.enter_text(self.YEARLY_NET_SALARY, yearly_net_income)
        self.enter_text(self.YEARLY_EXPENDITURE, yearly_expenditure)
        self.click_element(self.SUBMIT)
        self.yearlyNetIncome = yearly_net_income
        self.yearlyExpenditure = yearly_expenditure

    def calculate_Monthly_Discretionary_Income(self):
        return round((self.yearlyNetIncome / 12) - (self.yearlyExpenditure / 12), 2)
