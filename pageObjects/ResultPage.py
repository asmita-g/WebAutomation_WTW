from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    arrive = (By.CSS_SELECTOR, "span[aria-label='Sort results by Relevancy']")
    validate_datesort = (By.CSS_SELECTOR, "span[aria-checked='true']")
    date_sort = (By.CSS_SELECTOR, "span[aria-label='Sort by Date in descending order']")
    filter_by = (By.CSS_SELECTOR, "div[aria-label='Inclusion filter on Article; 13 results']")
    next_page_icon = (By.CSS_SELECTOR, "span[class='coveo-pager-next-icon']")
    article_str = (By.CSS_SELECTOR, "div[class='CoveoFieldValue wtw-listing-result-uri'] span")

    def val_arriveresultpage(self):
        self.driver.find_element(*ResultPage.arrive)
        Val_arriveresultpage = ResultPage(self.driver)
        return Val_arriveresultpage

    def val_sortdate(self):
        self.driver.find_element(*ResultPage.validate_datesort)
        Val_sortdate = ResultPage(self.driver)
        return Val_sortdate

    def datesort(self):
        self.driver.find_element(*ResultPage.validate_datesort).click()
        Date_sort = ResultPage(self.driver)
        return Date_sort

    def filtercontent(self):
        self.driver.find_element(*ResultPage.filter_by).click()
        Filtercontent = ResultPage(self.driver)
        return Filtercontent

    def stringtocompare(self):
        self.driver.find_element(*ResultPage.article_str)
        Stringcompare = ResultPage(self.driver)
        return Stringcompare

    def nextpageclick(self):
        self.driver.find_element(*ResultPage.next_page_icon).click()
        Nextpageclick = ResultPage(self.driver)
        return Nextpageclick

    def nextpageicon(self):
        self.driver.find_element(*ResultPage.next_page_icon)
        Nextpageicon = ResultPage(self.driver)
        return Nextpageicon


