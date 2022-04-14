import time
import pytest
from selenium import webdriver

def test_welcome1():
        link = "http://suninjuly.github.io/registration1.html"
        with webdriver.Chrome() as browser:
            browser.get(link)
            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("test@test.ru")
            input4 = browser.find_element_by_css_selector(".second_block .first")
            input4.send_keys("123456789")
            input4 = browser.find_element_by_css_selector(".second_block .second")
            input4.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

def test_welcome2():
        link = "http://suninjuly.github.io/registration2.html"
        with webdriver.Chrome() as browser:
            browser.get(link)
            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("test@test.ru")
            input4 = browser.find_element_by_css_selector(".second_block .first")
            input4.send_keys("123456789")
            input4 = browser.find_element_by_css_selector(".second_block .second")
            input4.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    pytest.main()
