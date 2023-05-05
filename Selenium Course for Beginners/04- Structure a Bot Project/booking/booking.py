import os
import booking.constants as const
from selenium import webdriver

driver = webdriver.Chrome


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/usr/local/bin", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()