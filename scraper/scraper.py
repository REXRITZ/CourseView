from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
cseWebsite = "https://www.cse.iitb.ac.in/"
asc = "https://asc.iitb.ac.in/acadmenu/"
driver.get(asc)
username = driver.find_element(By.NAME, "UserName")
# password = driver.find_element(By.ID, "passwd")
password = driver.find_element(By.NAME, "UserPassword")

username.send_keys("roll_number")
password.send_keys("paswword")

driver.find_element(By.NAME, "submit").click()
print(driver.text())