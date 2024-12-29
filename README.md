# extendEwayBill Automation

This Python script automates the process of extending E-way bills on the Indian GST E-way bill system. It uses Selenium WebDriver to interact with the website's interface programmatically.

## Features

- **Automated Login**: The script automatically logs into the E-way bill system using provided credentials.
- **E-way Bill Extension**: The script reads E-way bill numbers and expiry dates from a CSV file, and then extends each E-way bill on the website.
- **Form Filling**: The script automatically fills in necessary details on the extension form, such as vehicle number, transhipment details, and adjusted distance.
- **Submission**: After filling in the details, the script submits the form to complete the extension process.

## Usage

To use this script, you need to have Python and Selenium WebDriver installed on your machine. You also need to have two files:

1. **user.json**: A JSON file that stores your E-way bill portal credentials.

   Example `user.json`:
   ```json
   {
     "user_name": "your_username",
     "password": "your_password"
   }
   Place the eway.csv file containing the E-way bill details in the same directory as the script.
2. The script will detect the E-way bills that are about to expire based on the "Valid Untill" column.
3. The browser will open, and the script will wait for the user to fill in the CAPTCHA and log in.
4. Once logged in, the script will fetch all necessary data from the E-way bill portal.
The script will then proceed to extend the E-way bills.
Please note that this script is configured to use Firefox as the web browser. If you want to use a different browser, you will need to modify the WebDriver initialization in the script.


## Disclaimer

This script is intended for educational purposes and automating personal tasks. Please ensure you have the necessary permissions to automate interactions with the E-way bill system. The author is not responsible for any misuse or any issues arising from the use of this script.

## Tags

- **Python**
- **Automation**
- **Selenium**
- **E-way Bill**
- **GST**
- **Web Scraping**
- **Logistics**
- **Billing**
- **India**
- **Taxation**
- **Ewaybill**
- **Ewaybill Automation**
- **Ewaybill Auto EXtend**
