from selenium.webdriver.common.by import By



class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    Options = (By.CSS_SELECTOR, "button[data-menu='country-selector--is-visible']")
    Country = (By.XPATH, "//span[contains(text(),'Americas')]")
    Language = (By.XPATH, "//a[@href='/en-US']")
    Search_icon = (By.CSS_SELECTOR, "button[data-menu='search-menu-is-visible']")
    Search_text = (By.CSS_SELECTOR, "input[title = 'Insert a query. Press enter to send']")
    Search_click = (By.CSS_SELECTOR, "a[class='CoveoSearchButton coveo-accessible-button']")

    def countryoptions(self):
        self.driver.find_element(*SearchPage.Options).click()
        CountryOptions = SearchPage(self.driver)
        return CountryOptions

    def countryselect(self):
        self.driver.find_element(*SearchPage.Country).click()
        CountrySel = SearchPage(self.driver)
        return CountrySel

    def languageselect(self):
        self.driver.find_element(*SearchPage.Language).click()
        LanguageSel = SearchPage(self.driver)
        return LanguageSel

    def searchoption(self):
        self.driver.find_element(*SearchPage.Search_icon).click()
        SearchOpt = SearchPage(self.driver)
        return SearchOpt

    def searchtotext(self):
        self.driver.find_element(*SearchPage.Search_text).send_keys("IFRS 17")
        Searchtotext = SearchPage(self.driver)
        return Searchtotext

    def clicksearch(self):
        self.driver.find_element(*SearchPage.Search_click).click()
        Searchtoclick = SearchPage(self.driver)
        return Searchtoclick





