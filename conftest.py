import pytest
from selenium import webdriver
@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window() # макс окно
    browser.implicitly_wait(3) #время ожидания пока страница прогрузится для поиска элементов
    yield browser
