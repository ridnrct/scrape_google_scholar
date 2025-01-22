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
                title = "Tidak ada judul"
            try:
                link = article.find('h3', {'class': 'gs_rt'}).find('a')['href']
            except:
                link = "Link tidak tersedia"
            try:
                citation = "Sitasi tidak tersedia"
                citation_elements = article.find_all('a', href=True)
                for elem in citation_elements:
                    if 'cites=' in elem['href']:
                        citation = elem.text.strip()
                        break
                if citation == "Sitasi tidak tersedia":
                    citation = "Sitasi tidak ditemukan"
            except Exception as e:
                citation = f"Error dalam pengambilan sitasi: {str(e)}"
            try:
                snippet = article.find('div', {'class': 'gs_rs'}).text
            except:
                snippet = "Deskripsi tidak tersedia"
            try:
                authors_year = article.find('div', {'class': 'gs_a'}).text
                authors = re.split(' - ', authors_year)[0]
                year = re.search(r'\d{4}', authors_year).group()
            except:
                authors = "Penulis tidak tersedia"
                year = "Tahun tidak tersedia"
            
            article_data = {
                'Judul Jurnal': title,
                'Penulis': authors,
                'Tahun Publikasi': year,
                'Abstrak': snippet,
                'DOI/URL': link,
                'Jumlah Sitasi': citation
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
    keyword = input("Masukkan Kata Kunci Pencarian Artikel: ")
    start_year = int(input("Masukkan Tahun Awal (cth. 2020): "))
    end_year = int(input("Masukkan Tahun Akhir (cth. 2025): "))
    num_results = int(input("Masukkan Jumlah Artikel: "))
    articles = scrape_google_scholar(keyword, start_year, end_year, num_results)
    if articles:
        print("\nDaftar Artikel:")
        for i, article in enumerate(articles, start=1):
            print(f"\nArtikel {i}:")
            print(f"Judul: {article['Judul Jurnal']}")
            print(f"Penulis: {article['Penulis']}")
            print(f"Tahun Publikasi: {article['Tahun Publikasi']}")
            print(f"DOI/URL: {article['DOI/URL']}")
            print(f"Jumlah Sitasi: {article['Jumlah Sitasi']}")
            print(f"Abstrak: {article['Abstrak']}")
        save_to_excel(articles, keyword)
        print(f"\nData berhasil disimpan ke dalam file {keyword}.xlsx.")
    else:
        print("Tidak ada artikel yang ditemukan.")

if __name__ == '__main__':
    main()
