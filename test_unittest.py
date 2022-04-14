import pytest
from selenium import webdriver
import time


def test_reg_page_1():
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("third")
        input3.send_keys("aa@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text  # add assertion here
        browser.quit()


def test_reg_page_2():
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("third")
        input3.send_keys("aa@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.quit()

if __name__ == '__main__':
    pytest.main()
