from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

print("🔃 Opening FoSCoS homepage...")
driver.get("https://foscos.fssai.gov.in/")

try:
    print("➡️ Waiting for Tatkal Registration text inside <b> tag...")

    # Wait for the <b> tag that contains "Apply for Tatkal License/Registration"
    b_tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//b[contains(text(), 'Apply for Tatkal License/Registration')]"))
    )

    # Use JavaScript to click on the parent <p> tag (since direct click may be blocked)
    parent_p = b_tag.find_element(By.XPATH, "./..")
    driver.execute_script("arguments[0].click();", parent_p)
    print("✅ Clicked using JS")

    # Now wait for the Proceed button to appear and click it
    proceed_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Proceed')]"))
    )
    proceed_button.click()
    print("✅ 'Proceed' button clicked")

except Exception as e:
    print(f"❌ Error occurred while clicking: {e}")

input("⏸️ Press Enter to exit and close the browser...")
driver.quit()
