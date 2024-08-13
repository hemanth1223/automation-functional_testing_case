# Automation Test - Functional Testing Case

This project demonstrates a functional test case using Selenium WebDriver to automate a web application. The test includes logging into the application, uploading an XLS file, validating the data, and capturing the final output. The test is designed to check the functional flow of the application and ensure that it operates as expected.

## Overview

This test case automates the following tasks:

1. **Log in** to the web application using the provided credentials.
2. **Upload an XLS file** to the application.
3. **Validate the data** on the page after the file is uploaded.
4. **Capture a video** of the entire process.
5. **Take a screenshot** of the final output page.

## Test Steps & Input

1. **Visit the Web Application:**
   - Navigate to: [https://demo.dealsdray.com/](https://demo.dealsdray.com/)

2. **Login:**
   - Use the following credentials to log in:
     - **Username:** [prexo.mis@dealsdray.com](mailto:prexo.mis@dealsdray.com)
     - **Password:** [prexo.mis@dealsdray.com](mailto:prexo.mis@dealsdray.com)

3. **Navigate to Orders Section:**
   - Go to the "Orders" section.

4. **Add a Bulk Order:**
   - Click on the "Add Bulk Orders" button.

5. **Upload XLS File:**
   - Download the file and upload it. (Refer Code)

6. **Validate Data:**
   - Click the "Validate Data" button.

7. **Capture Screenshot:**
   - Take a screenshot of the page displaying validation results.

8. **Handle Errors:**
   - Note any issues faced during the XLS file upload and data validation process.

## Output

- **Video**: A video capturing the entire login process and file upload.
- **Screenshot**: A screenshot of the final output page after the validation.
- **Script**: The Selenium script used to perform the test.

## How to Run the Test

1. Clone the Repository:
   ```bash
   git clone https://github.com/hemanth1223/automation-functional_testing_case.git
   cd automation-functional_testing_case
   
2. Set Up the Environment:
   Ensure you have Python installed.
   
   Create and activate a virtual environment & Install the required dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    
3. Run the Test:
   ```bash
   python functional_test.py

4. Review the Output:
   - The video of the process will be saved as test_video.mp4 or any name.
   - The screenshot of the final output page will be saved as final_output.png. (Here, I have used MS Excel to import the final output data instead of screenshot.)
   - The test script is provided in the repository.

## Notes
- Ensure that the web application is accessible, and the provided credentials are correct.
- The video recording of the test process can be done using screen recording tools such as OBS Studio or any other preferred tool.
- The script is written in Python and uses Selenium WebDriver with the Firefox browser.
- If any issues arise during the test, ensure that all dependencies are installed, and the browser drivers are correctly configured.
