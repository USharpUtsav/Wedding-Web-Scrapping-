**🏨 Wedding Venue Scraper**
This project scrapes wedding venue data from [Wedding Spot](https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1) using Scrapy and Selenium for JavaScript-based pagination.

**🚀 Project Overview**
The target website uses JavaScript to dynamically load content. The "Next Page" button does not contain a direct link but is rendered using:
aria-label="Next Page"
As a result, Selenium is integrated with Scrapy to simulate button clicks and handle dynamic page transitions.

**🧰 Requirements**
Python ≥ 3.10

* Scrapy

* Selenium

* ChromeDriver

* pandas

* re (Python built-in)

* webdriver_manager

**⚙️ Installation**
Clone the repository or download the source files.
Install the dependencies:
pip install scrapy selenium pandas webdriver-manager
Make sure ChromeDriver is installed and compatible with your Chrome browser.
The webdriver_manager package handles this automatically.

