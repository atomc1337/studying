import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() # макс окно
    browser.implicitly_wait(3) #время ожидания пока страница прогрузится для поиска элементов
    yield browser
