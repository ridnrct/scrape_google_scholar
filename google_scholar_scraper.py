from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

def scrape_google_scholar(keyword, start_year, end_year, num_results):
    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    keyword = keyword.replace(" ", "+")
    base_url = f'https://scholar.google.com/scholar?q={keyword}&as_ylo={start_year}&as_yhi={end_year}'
    
    article_list = []
    start = 0  
    while len(article_list) < num_results:
        url = f"{base_url}&start={start}"  
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.find_all('div', {'class': 'gs_r gs_or gs_scl'})
        if not articles: 
            break
        for article in articles:
            if len(article_list) >= num_results:
                break
            try:
                title = article.find('h3', {'class': 'gs_rt'}).text
            except:
                title = "No title"
            try:
                link = article.find('h3', {'class': 'gs_rt'}).find('a')['href']
            except:
                link = "Link not available"
            try:
                citation = "Citation not available"
                citation_elements = article.find_all('a', href=True)
                for elem in citation_elements:
                    if 'cites=' in elem['href']:
                        citation = elem.text.strip()
                        break
                if citation == "Citation not available":
                    citation = "Citation not found"
            except Exception as e:
                citation = f"Error in fetching citation: {str(e)}"
            try:
                snippet = article.find('div', {'class': 'gs_rs'}).text
            except:
                snippet = "Description not available"
            try:
                authors_year = article.find('div', {'class': 'gs_a'}).text
                authors = re.split(' - ', authors_year)[0]
                year = re.search(r'\d{4}', authors_year).group()
            except:
                authors = "Authors not available"
                year = "Year not available"
            
            article_data = {
                'Journal Title': title,
                'Authors': authors,
                'Publication Year': year,
                'Abstract': snippet,
                'DOI/URL': link,
                'Citation Count': citation
            }
            article_list.append(article_data)
        start += 10  
    driver.quit()
    return article_list


def save_to_excel(data, keyword):
    df = pd.DataFrame(data)
    filename = f"{keyword}.xlsx"
    df.to_excel(filename, index=False, engine='openpyxl')

def main():
    keyword = input("Enter search keyword for articles: ")
    start_year = int(input("Enter start year (e.g., 2020): "))
    end_year = int(input("Enter end year (e.g., 2025): "))
    num_results = int(input("Enter number of articles: "))
    articles = scrape_google_scholar(keyword, start_year, end_year, num_results)
    if articles:
        print("\nList of Articles:")
        for i, article in enumerate(articles, start=1):
            print(f"\nArticle {i}:")
            print(f"Title: {article['Journal Title']}")
            print(f"Authors: {article['Authors']}")
            print(f"Publication Year: {article['Publication Year']}")
            print(f"DOI/URL: {article['DOI/URL']}")
            print(f"Citation Count: {article['Citation Count']}")
            print(f"Abstract: {article['Abstract']}")
        save_to_excel(articles, keyword)
        print(f"\nData successfully saved to the file {keyword}.xlsx.")
    else:
        print("No articles found.")

if __name__ == '__main__':
    main()
