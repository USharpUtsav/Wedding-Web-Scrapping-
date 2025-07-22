### Submission Checklist:
- [x] **1. A complete set of code files for the scraping task (either a zip file or a GitHub link)**
    - The zip file containing all the necessary code files has been submitted via email.
  
- [x] **2. Match the structure of the sample data and ensure accuracy**
    - The structure and format of the scraped data match the provided sample. All relevant fields are included and formatted as per the requirement.
  
- [x] **3. A Readme file with instructions on setting up the project, running it and viewing the data**
    - A Readme file instruction is provided below for setup, execution, and viewing the data.
  
- [x] **4. A sample of the scraped data (JSON, CSV, or Excel file). Try to scrape up to 4 or 5 listing pages.**
    - A `weddingvenues_sorted_forsubmission.csv` file has been created, containing the extracted venue details from up to 6 listing pages.



# Wedding Venue Scraper Intern Assignment for Parsedom

This project scrapes wedding venue data from https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1 using Scrapy and Selenium for pagination


From the given website HTML, the "Next Page" button doesn't directly contain any link or URL, but it does have an aria-label="Next Page" attribute. The next page is likely triggered dynamically by clicking this button, but the URL is not be explicitly provided in the button itself.

So to handle the next page button i am using integrating selenium with scrapy,Handling the "Next Page" Button with Selenium
The next page is loaded through JavaScript, i am going to use Scrapy-Selenium to simulate the button click and handle JavaScript-driven pagination.

## Requirements

- Python 3.10 or higher
- Scrapy
- Selenium
- ChromeDriver

## Installation
Install Dependencies:Install the required Python packages using pip
scrapy: For web scraping.

selenium: For handling JavaScript-driven pagination.

pandas: For data cleaning and manipulation (used in my data cleaning script).

webdriver_manager: For managing the ChromeDriver installation.

re: For regular expressions (used for cleaning phone numbers).

##Running the Project
1.Open a terminal or command prompt.

2.Navigate to the wedvenue folder inside the extracted intern_parsedom folder:

3.Run the command :-scrapy crawl venue_spider -o weddingvenues.csv

4.Clean and Sort the Data:After scraping, run the data cleaning script to clean and sort the data according to given sample:order_arranged.py

5.Open the  weddingvenues.csv to view the extracted data from the web
