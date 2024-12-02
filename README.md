# Harvest Hawk
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ritesh-tiwary/harvest-hawk.svg?style=social)](https://github.com/ritesh-tiwary/harvest-hawk/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ritesh-tiwary/harvest-hawk.svg?style=social)](https://github.com/ritesh-tiwary/harvest-hawk/network/members)
[![GitHub issues](https://img.shields.io/github/issues/ritesh-tiwary/harvest-hawk.svg)](https://github.com/ritesh-tiwary/harvest-hawk/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/ritesh-tiwary/harvest-hawk.svg)](https://github.com/ritesh-tiwary/harvest-hawk/pulls)
[![Contributors](https://img.shields.io/github/contributors/ritesh-tiwary/harvest-hawk.svg)](https://github.com/ritesh-tiwary/harvest-hawk/graphs/contributors)
[![Twitter](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fritesh-tiwary%2Fharvest-hawk)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fritesh-tiwary%2Fharvest-hawk)


**Harvest Hawk** is a powerful, scalable web scraping application built with Scrapy and Scrapy-Splash to tackle JavaScript-rendered pages. Initially developed to scrape quotes from JavaScript-enabled sites, this project is evolving into a versatile tool capable of configuring and extracting data from any URL. Its modular design and robust Docker integration make it adaptable for diverse web data harvesting needs.

## Features

- **JavaScript Handling**: Integrated Scrapy-Splash enables the handling of JavaScript-rendered pages.
- **Dockerized Environment**: Runs seamlessly with Docker, simplifying setup and deployment.
- **Scalable Architecture**: Designed to grow into a comprehensive scraping tool for various websites and data formats.
- **Dynamic URL Configurations**: Allowing users to configure URLs for various scraping needs.
- **Custom Data Extraction**: Extract any data type specified by users, beyond quotes.
- **Advanced Scheduling and Proxy Management**: For large-scale scraping across multiple sources.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- **Docker**: For containerized Splash and seamless deployment.
- **Python 3.12+**: To run Scrapy and manage project dependencies.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ritesh-tiwary/harvest-hawk.git
   cd harvest-hawk
   ```
2. Pull and run Splash from Docker
   ```
   docker run -p 8050:8050 scrapinghub/splash
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a scrapy project
   ```bash
   scrapy startproject harvest_hawk_scraper
   ```

5. Navigate to the project folder
   ```bash
   cd harvest_hawk_scraper
   ```

6. Create spider 'quotes' using template 'basic' in module: harvest_hawk_scraper.spiders.quotes
   ```bash
   scrapy genspider quotes quotes.toscrape.com
   ```

### Usage
1. Start the Splash service:
   ```bash
   docker-compose up -d splash
   ```

2. Navigate to the project folder
   ```bash
   cd harvest_hawk_scraper
   ```

3. Run the Scrapy spider to scrape quotes:
   ```bash
   scrapy crawl quotes -o output/quotes.json
   ```
This initial spider is configured to scrape sample quotes from a JavaScript-enabled site.

### Configuration

- **Settings**: Customize your Scrapy settings in `settings.py`.
- **Splash Settings**: Modify Splash configurations and endpoints if needed in `docker-compose.yml`.

### Contributing

Contributions are welcome! Feel free to submit issues or pull requests to help improve Harvest Hawk.
