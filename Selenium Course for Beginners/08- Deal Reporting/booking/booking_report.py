from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.deal_boxes = boxes_section_element

    def pull_deal_box_attributes(self):

        collection = []
        for deal_box in self.deal_boxes:
            # Pegando o nome dos hoteis
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            # Pegando o preço dos hoteis
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip()

            # Pegando o score
            try:
                hotel_score = deal_box.find_element(
                    By.CSS_SELECTOR, 'div[data-testid="review-score"]'
                )
                hotel_score = hotel_score.find_element(
                    By.CLASS_NAME, 'b5cd09854e'
                ).get_attribute('innerHTML').strip()
            except:
                hotel_score = None
                
            collection.append(
                [hotel_name, hotel_price,hotel_score]
            )
        return collection
            