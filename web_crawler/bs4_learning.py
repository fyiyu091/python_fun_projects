from bs4 import BeautifulSoup as soup
import requests

def main():
    r = requests.get("https://www.oneplus.com/")
    page = soup(r.content, "html.parser")
    print(page.findAll("a"))

if __name__ == "__main__":
    main()