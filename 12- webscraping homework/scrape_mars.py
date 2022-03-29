import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager



class ScrapingHelper():
    def __init__(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)

        sites = [
            url = "https://redplanetscience.com/",
            url2 = "https://spaceimages-mars.com/",
            url3 ="https://galaxyfacts-mars.com/",
            url4 = "https://marshemispheres.com/"
        ]

    def getData(self):
        for site1 in sites:
            browser.visit(self.url)
            html = browser.html
            soup= BeautifulSoup(html, "html.parser")

            news_title = soup.find_all("div", {"class": "content_title"})[0].text
            news_p = soup.find_all("div", {"class": "article_teaser_body"})[0].text

            browser.quit()

        for site2 in sites:
            browser.visit(self.url2)
            browser.links.find_by_partial_text('FULL IMAGE').click()
            html = browser.html
            soup= BeautifulSoup(html, "html.parser")
            featured_image_url = soup.find("img", {"class":"fancybox-image"})['src']
            featured_image_url = url2+featured_image_url

            browser.quit()


        for site3 in sites:
            df = pd.read_html(self.url3)[0]
            df.columns = ["Description", "Mars", "Earth"]
            df.set_index('Description', inplace= True)
            facts = df.to_html()

            browser.quit()


        for site4 in sites:
            browser.visit(self.url4)
            hemisphere_image_urls = []
            links = browser.find_by_css("a.product-item img")

            for x in range(len(links)):
                hemisphere = {}
                browser.find_by_css("a.product-item img")[x].click()
                element = browser.links.find_by_text('Sample').first
                hemisphere["img_url"] = element['href']
                hemisphere["title"] = browser.find_by_css("h2.title").text
                hemisphere_image_urls.append(hemisphere)
                browser.back()

            browser.quit()

        data = {
            "news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "facts": facts,
            "hemisphere_image_urls": hemisphere_image_urls
        }

        return(data)




