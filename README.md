#  SCT_SD_Task4 – E-commerce Scraper 

This repository contains **Task 4** for my **Software Development Internship** at **SkillCraft Technology**.

---

##  Task Objective

Create a program that extracts **product information** such as **names, prices, and ratings** from an online e-commerce website  
and stores the data in a structured format (**CSV file**).  
The goal is to demonstrate web scraping, data parsing, and file export using Python with a **user-friendly GUI**.

---

##  Key Features

- User-friendly **Tkinter GUI** to enter the URL of the e-commerce page.
- Uses **`requests`** to fetch the page content.
- Parses the page with **`BeautifulSoup`** to extract product details.
- Supports extracting:
  - Product **Name**
  - Product **Price**
  - Product **Rating**
- Saves the scraped data in **`products.csv`**.
- Displays success or error popups for clear feedback.

---

##  Tools & Libraries Used

- **Python 3**
- **Tkinter** (GUI library)
- **requests** (HTTP requests)
- **BeautifulSoup** (HTML parsing)
- **pandas** (CSV export)

---

##  Requirements

Install the required libraries before running and Run
```bash
pip install requests beautifulsoup4 pandas
python Task_4.py
