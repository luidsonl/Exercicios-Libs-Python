import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_report import BookingReport
from prettytable import PrettyTable

driver = webdriver.Chrome


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/usr/local/bin", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        #os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL + const.QUERY_STRING)
        #fecha popup se, aparecer
        #Encontra popup em portugues
        #self.close_popup(css_selector='button[aria-label="Ignorar informações de login."]')
        #Encontra popup em ingles
        self.close_popup(css_selector='button[aria-label="Dismiss sign-in info."]')



    def close_popup(self, css_selector):
        try:
            popup = self.find_element(By.CSS_SELECTOR, css_selector)
            popup.click()
            return True
        except:
            return False
        

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        
    def select_checkin_checkout(self, checkin = None, checkout = None):
        calendar = self.find_element(By.CSS_SELECTOR, 'div[data-testid="searchbox-dates-container"]')
        calendar.click()
        
        checkin_date = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkin}"]')
        checkin_date.click()

        checkout_date = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkout}"]')
        checkout_date.click()


    def search(self):
        search_button = self.find_element(By.XPATH, "//button[.//span[text()='Search']]")
        search_button.click()

    def report_results(self):
        hotel_cards = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        report = BookingReport(hotel_cards)
        table =PrettyTable(
            field_names=['Hotel Name', 'Hotel Price', 'Hotel Score']
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()