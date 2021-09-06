import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("http://www.willistowerswatson.com/ICT")
    explicit_wait = WebDriverWait(driver, 10)
    explicit_wait.until(EC.frame_to_be_available_and_switch_to_it(
    driver.find_element_by_xpath("/html[1]/body[1]/div[6]/div[1]/iframe[1]")))
    #Agree with cookie settings and proceed
    driver.find_element_by_link_text("Agree and Proceed").click()
    driver.switch_to.default_content()
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()