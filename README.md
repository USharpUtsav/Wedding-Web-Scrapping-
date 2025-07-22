**🏨 Wedding Venue Scraper**
This project scrapes wedding venue data from Wedding Spot using Scrapy and Selenium for JavaScript-based pagination.

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

