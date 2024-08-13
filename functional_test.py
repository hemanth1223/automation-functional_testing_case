from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Path to your GeckoDriver
gecko_driver_path = r'C:\\webdrivers\\geckodriver-v0.35.0-win64\\geckodriver.exe'

firefox_options = Options()
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

def extract_table_to_excel(driver):
    try:
        table = driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-9177x2']")
        
        headers = [th.text for th in table.find_elements(By.XPATH, ".//thead//th")]
        print(f"Headers found: {headers}")

        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        
        data = []
        for row in rows:
            cols = row.find_elements(By.XPATH, ".//td")
            row_data = [col.text for col in cols]
            data.append(row_data)
        
        num_headers = len(headers)
        column_lengths = [len(row) for row in data]
        
        if any(length != num_headers for length in column_lengths):
            print("Mismatch between header columns and data columns.")
            print(f"Number of columns in headers: {num_headers}")
            print(f"Number of columns in data rows: {column_lengths}")

        if len(headers) < len(data[0]):
            headers.append('Extra Column') 

        # Create DataFrame and save to Excel
        try:
            df = pd.DataFrame(data, columns=headers[:len(data[0])])
            df.to_excel("Output_data.xlsx", index=False)
            print("Table data extracted to Excel")
        except Exception as e:
            print(f"Error creating DataFrame or saving to Excel: {e}")
    except Exception as e:
        print(f"Error extracting table data: {e}")

try:
    # Open the web application
    driver.get("https://demo.dealsdray.com/")
    print("Opened the application")

    # Log in with provided credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("prexo.mis@dealsdray.com")
    driver.find_element(By.NAME, "password").send_keys("prexo.mis@dealsdray.com", Keys.RETURN)
    print("Logged in")

    # Wait for and handle any alert that might appear
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Handled login alert")
    except Exception as e:
        print(f"No alert present or error handling login alert: {e}")

    # Navigate to the Orders section
    try:
        orders_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/mis/orders']/button//span[text()='Orders']"))
        )
        orders_link.click()
        print("Clicked on Orders link")
    except Exception as e:
        print("Error finding or clicking Orders link:", e)

    # Click on "Add Bulk Orders" button
    try:
        add_bulk_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Bulk Orders')]"))
        )
        add_bulk_order_button.click()
        print("Clicked on Add Bulk Orders button")
    except Exception as e:
        print("Error finding or clicking Add a Bulk Order button:", e)

    # Upload XLS file
    try:
        file_upload_path = r"C:\\Users\\DELL\\Downloads\\Automation - Functional Testing Case\\demo-data.xlsx"
        upload_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_element.send_keys(file_upload_path)
        print("File uploaded")
    except Exception as e:
        print("Error uploading file:", e)

    # Validate Data
    try:
        validate_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Validate Data']"))
        )
        validate_button.click()
        print("Clicked on Validate Data button")

        # Handle any alert that might appear after validation
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print(f"Alert Text: {alert.text}")
            alert.accept()
            print("Handled validation alert")
        except Exception as e:
            print(f"No alert present or error handling validation alert: {e}")

        time.sleep(5) 

        extract_table_to_excel(driver)
        
    except Exception as e:
        print("Error finding or clicking Validate Data button:", e)

finally:
    driver.quit()
