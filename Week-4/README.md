# 🕸️ Web Scraper (News Headlines Extractor)

This project is a simple Python-based **web scraper** that fetches and parses the latest news headlines from a webpage like **BBC News** using the `requests` and `BeautifulSoup` libraries.

---

## 📌 Features

- Fetches live HTML content from the web  
- Extracts news headlines from `<h1>`, `<h2>`, and `<h3>` tags  
- Filters out irrelevant or short headlines  
- Displays up to 10 clean, readable headlines  
- Uses a user-agent header to avoid bot blocking  

---

## 🧠 Project Architecture

1. **Design the web scraper architecture** and identify the key features  
2. **Implement methods** for fetching and parsing web pages  
3. Use **Python's built-in libraries** like `BeautifulSoup` or `Scrapy`  
4. **Test the web scraper** with sample data and validate output  

---

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/web_scraper.git
cd web_scraper

````

### Step 2: Install Dependencies

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Run

```bash
python web_scraper.py
```

The program will:

* Fetch data from `https://www.bbc.com/news`
* Parse the HTML content
* Display the top 10 headlines

---

## 🧪 Sample Output

```text
✅ Page fetched successfully.

📰 Headlines Found:
1. UK advises against all travel to Israel as Iran-Israel conflict rages
2. Satellite imagery reveals damage to key Iran nuclear sites
3. Footage captures exchange of attacks between Iran and Israel
4. What are the worst-case scenarios?
5. Israel-Iran conflict set to dominate G7 summit
6. 'It's heavy on the heart': Israelis survey damage in city hit by Iranian missile
7. More top stories
8. Air India plane crash death toll rises to 270
9. Manhunt after two Minnesota state politicians targeted, one of them killed
10. Race to mine metals for EV batteries threatens marine paradise    
...
```

---

## 📂 File Structure

```
web-scraper/
│
├── web_scraper.py           # Main Python script
├── README.md                # Project documentation
```

---

## 🔍 Customization Tips

* Try with different URLs like:

  * `https://edition.cnn.com/`
  * `https://www.reuters.com/`
* Customize the parser to extract specific content (articles, images, links, etc.)

---

## 📄 License

This project is licensed under the MIT License.

---
