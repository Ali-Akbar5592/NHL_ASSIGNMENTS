# Assignment & Motivation letter

# Quotes Scraper Project

A simple Python project using Scrapy, Pandas, NumPy, and MySQL to scrape and analyze quotes from http://quotes.toscrape.com

## Features 
- Scrapes quotes, authors, and tags using Scrapy 
- Filters and processes data with Pandas and NumPy 
- Stores data in a MySQL database 

## Setup 

### 1. Install Requirements 
```bash 
pip install -r requirements.txt 

### 2. Run the Scraper

scrapy runspider quotes_scraper.py -o quotes.json 

### 3. MySQL Setup

Login to MySQL and run:

CREATE DATABASE your_database;
CREATE USER 'your_user'@'localhost' IDENTIFIED BY 'your_password'; 
GRANT ALL PRIVILEGES ON your_database.* TO 'your_user'@'localhost'; 
FLUSH PRIVILEGES;

### 4. Process and Store Data 

python process_and_store.py 