from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Setup ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    print("🔃 Opening FoSCoS homepage...")
    driver.get("https://foscos.fssai.gov.in")

    # Step 1: Apply for Tatkal
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//b[contains(text(),'Apply for Tatkal License/Registration')]"))
    )
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.XPATH, "//b[contains(text(),'Apply for Tatkal License/Registration')]"),
    )

    # Step 2: Click "Proceed" on KOB list popup
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed')]"))
    )
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]"),
    )

    print("\n➡️ Please manually complete:")
    print("  • Food Services → Petty Retailer of snacks/tea shops")
    print("  • Tick checkbox")
    print("  • Click final 'Proceed' to open Form A")
    input("✅ When Form A loads on your screen, press ENTER to start auto-fill...")

    # === Auto-fill Form A ===
    print("📝 Filling Form A...")

    # Applicant Details
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "applicantName"))
    ).send_keys("Vikash Kumar")

    driver.find_element(By.NAME, "designation").send_keys("Individual")
    driver.find_element(By.NAME, "addressPremises").send_keys("123 Tea Shop Street")
    driver.find_element(By.NAME, "stateCode").send_keys("Uttar Pradesh")
    driver.find_element(By.NAME, "districtCode").send_keys("Greater Noida")
    driver.find_element(By.NAME, "subDivisionCode").send_keys("Noida Subdivision")
    driver.find_element(By.NAME, "villageCode").send_keys("VillageName")
    driver.find_element(By.NAME, "pinCode").send_keys("201306")
    driver.find_element(By.NAME, "landmark").send_keys("Near Sector 62 metro")
    driver.find_element(By.NAME, "pan").send_keys("ABCDE1234F")

    # Correspondence Address (Same as premises)
    driver.find_element(By.NAME, "correspondenceSameAsPremises").click()

    # Contact Details
    driver.find_element(By.NAME, "mobileNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "emailId").send_keys("vikash@example.com")
    driver.find_element(By.NAME, "contactPersonName").send_keys("Vikash Kumar")
    driver.find_element(By.NAME, "contactPersonAadhar").send_keys("123412341234")

    # License duration (select dropdown)
    driver.find_element(By.NAME, "licensePeriod").send_keys("5")

    # Food Items – skip (leave empty) or handle dynamically

    # Source of Water
    driver.find_element(By.NAME, "sourceOfWaterSupply").send_keys("Public")

    # Power Usage
    driver.find_element(By.NAME, "electricPowerUsage").send_keys("Yes")

    # Declaration Checkbox
    driver.find_element(By.NAME, "declarationAccepted").click()

    print("✅ Form completed ✅")
    print("You can now manually click 'Save & Next' or proceed as needed.")

except Exception as err:
    print("❌ Error during form auto-fill:", err)

finally:
    input("👀 Press ENTER to close browser.")
    driver.quit()
