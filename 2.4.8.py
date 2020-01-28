from selenium import webdriver
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return log(abs(12*sin(x)))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

button = browser.find_element_by_id("book")
button.click()

x = int(browser.find_element_by_id("input_value").text)
result = str(calc(x))
input1 = browser.find_element_by_id("answer")
input1.send_keys(result)

button2 = browser.find_element_by_id("solve")
button2.click()

