import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ResultPage import ResultPage
from pageObjects.SearchPage import SearchPage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_wtw(self):
        log = self.getLogger()
        explicit_wait = WebDriverWait(self.driver, 10)
        searchPage = SearchPage(self.driver)
        resultPage = ResultPage(self.driver)
        searchPage.countryoptions()
        searchPage.countryselect()
        time.sleep(1)
        log.info("Select US English Language")
        searchPage.languageselect()
        searchPage.searchoption()
        log.info("Search for text IFRS 17")
        searchPage.searchtotext()
        explicit_wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@class='CoveoSearchButton coveo-accessible-button']")))
        searchPage.clicksearch()
        explicit_wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//span[@aria-label='Sort results by Relevancy']")))
        try:
            resultPage.val_arriveresultpage()
            log.info("Arrived on Results Page")
        except NoSuchElementException:
            log.debug("Not able to reach results page")

        sort_by = self.driver.find_element_by_css_selector("span[aria-checked='true")
        log.info(sort_by.text)
        if not (sort_by.text)== "Date":
            log.info("Results need to be sorted by Date")
            resultPage.datesort()
            log.info("Results are sorted by Date now")
        explicit_wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[@aria-label='Inclusion filter on Article; 13 results']")))
        resultPage.filtercontent()
        log.info("Filter content by Article")
        explicit_wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//span[@class='coveo-facet-breadcrumb-caption']")))
        list_article=[]
        next_icon = self.driver.find_element_by_css_selector("span[class='coveo-pager-next-icon']")
        log.info(next_icon.is_displayed())
        while True:
            try:
                log.info("Taking out the string to be validated in each article")
                article = self.driver.find_elements_by_css_selector("div[class='CoveoFieldValue wtw-listing-result-uri'] span")
                for i in article:
                    log.info(i.text)
                    list_article.append(i.text)
                log.info(list_article)
                resultPage.nextpageclick()
                time.sleep(1)
            except:
                break

        str_compare= "https://www.willistowerswatson.com/en-US"
        for i in list_article:
            assert str_compare in i
            log.info("String compare is Passed")