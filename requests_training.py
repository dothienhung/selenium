from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://45.79.43.178/source_carts/wordpress/wp-admin"
driver = webdriver.Chrome('D:/chromenium/chromedriver')
driver.get(url)

username = driver.find_element_by_name('log')
username.send_keys('admin')
password = driver.find_element_by_name('pwd')
password.send_keys('123456aA')
password.send_keys(Keys.RETURN)

get_userName =driver.find_element_by_class_name("display-name").text
print(get_userName)