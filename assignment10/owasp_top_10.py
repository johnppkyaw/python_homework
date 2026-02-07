from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

#Task 6: Scraping Structured Data
results = []

try:
    driver.get("https://owasp.org/www-project-top-ten/")
    top_ten_a = driver.find_element(By.XPATH, '//main/div/div/section/p/a')
    top_ten_url = top_ten_a.get_attribute('href')
    driver.get(top_ten_url)
    top_ten_li = driver.find_elements(By.XPATH, '//div[3]/main/div/div[3]/article/ol/li')
    for each_risk in top_ten_li:
        dict = {}
        each_risk_info = each_risk.find_element(By.XPATH, 'a')
        dict['Title'] = each_risk_info.text
        dict['URL'] = each_risk_info.get_attribute('href')
        results.append(dict)
    df = pd.DataFrame(results)
    df.to_csv('owasp_top_10.csv')


except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()
