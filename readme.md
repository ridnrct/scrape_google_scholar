# Google Scholar Scraper

Google Scholar Scraper is a Python program used to search for and retrieve article data from Google Scholar based on keywords, year range, and the desired number of articles. The search results will be displayed in the console and saved in an Excel file.

## Requirements
Ensure you have installed Python and the following libraries before running the program:

- Selenium  
- BeautifulSoup4  
- Pandas  
- Webdriver-Manager  
- OpenPyxl  

### Installing Libraries

1. Manually install the required libraries using the following command:
   ```bash
   pip install selenium beautifulsoup4 pandas webdriver-manager openpyxl
   ```

2. Alternatively, install all required libraries from the `requirements.txt` file using:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Program

1. Run the program using the command:
   ```bash
   python google_scholar_scraper.py
   ```

2. The program will prompt you to enter the following details:

   - **Keyword**: Enter the search keyword for the desired articles.  
   - **Start Year**: Enter the starting year of the search range.  
   - **End Year**: Enter the ending year of the search range.  
   - **Number of Articles**: Enter the number of articles to retrieve.  

3. After entering the details, the program will process the article search on Google Scholar.

## Results

- The retrieved articles will be displayed in the console.  
- The article data will also be saved in an Excel file, named according to the search keyword.

## Output File
The resulting Excel file will contain the following columns:

- **Journal Title**: The title of the retrieved article.  
- **Authors**: The names of the article's authors.  
- **Publication Year**: The year the article was published.  
- **Abstract**: A description or summary of the article.  
- **DOI/URL**: A link to the article.  
- **Citation Count**: The number of citations.
