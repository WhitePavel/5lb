import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait            # import for wait
from selenium.webdriver.support import expected_conditions as EC   # import for wait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--******")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
wait = WebDriverWait(driver,20,poll_frequency=15)                   # время ожидания и интервал запросов

driver.get('https://www.moysklad.ru/login/')

login_field= ("xpath","//input[@name='j_username']")
password_field = ("xpath","//input[@name='j_password']")
entry_button = ("xpath","//button[@type='submit']")
element_for_wait_workers = ("//div[text()='Возвраты']")
workers = ("xpath","//span[text()='По сотрудникам']")
title = ("xpath","//a[@title]")

wait.until(EC.element_to_be_clickable(login_field)).send_keys("*******")
wait.until(EC.element_to_be_clickable(password_field)).send_keys("*****")
wait.until(EC.element_to_be_clickable(entry_button)).click()
driver.get("https://online.moysklad.ru/app/#pnl?periodFilter=07.11.2024%2000:00:00,07.11.2024%2023:59:00,inside_period")
wait.until(EC.element_to_be_clickable(workers)).click()
time.sleep(10)


# src = driver.page_source
# with open("index.html","w") as file:
#     file.write(src)
