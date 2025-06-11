import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/VIKASH/OneDrive/Documents/Automation/AutomationMania/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://foscos.fssai.gov.in/public/fbo/open-register-tatkal/N")
time.sleep(10)  # Keep browser open for 10 seconds
driver.quit()
