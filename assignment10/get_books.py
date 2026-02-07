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

#Task 2 element and class notes
    #each search result: li "row cp-search-result-item"
    #title: "title-content"
    #authors: a, "author-link"
    #format and year:  span, "display-info-primary"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

#Task 3: Write a Program to Extract this Data
results = []

try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    body = driver.find_element(By.CSS_SELECTOR,'body')

    if body:
        search_results = body.find_elements(By.CSS_SELECTOR, 'li[class="row cp-search-result-item"]')

        for search_result in search_results:
          dict = {}
          #title
          title = search_result.find_element(By.CLASS_NAME, 'title-content').text

          #authors
          author_list = [(auth.text) for auth in search_result.find_elements(By.CSS_SELECTOR, 'a[class="author-link"]')]
          if author_list:
              authors = "; ".join(author_list)
          else:
              authors = ""
            
          #type and year
          type_and_year = search_result.find_element(By.CSS_SELECTOR, 'span[class="display-info-primary"]').text

          dict["Title"] = title
          dict["Author"] = authors
          dict["Format-Year"] = type_and_year
          results.append(dict)
    df = pd.DataFrame(results)
    print(df)

    #Task 4: Write out the Data
    df.to_csv('get_books.csv')
    df.to_json('get_books.json')

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()
