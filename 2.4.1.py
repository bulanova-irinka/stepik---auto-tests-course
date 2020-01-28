from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

z = browser.find_element_by_id("answer")
z.send_keys(y)

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[for='robotsRule']")
option2.click()

button = browser.find_element_by_tag_name("button")
button.click()
