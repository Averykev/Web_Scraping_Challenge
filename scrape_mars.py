from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape():

    ## NASA MARS NEWS ##

    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)

    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('li', class_='slide').find('div', class_="content_title").text

    news_paragraph = soup.find('li', class_='slide').find('div', class_='article_teaser_body').text



    ##  JPL MARS SPACE IMAGES - FEATURED IMAGE  ##

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(image_url)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(1)

    browser.click_link_by_partial_text('more info')

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_image = soup.find('figure', class_='lede')

    mars_image = mars_image.a['href']

    jpl_base_url = 'https://www.jpl.nasa.gov'

    featured_image_url = jpl_base_url + mars_image



    ##  MARS FACTS TABLE  ##

    mars_facts_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(mars_facts_url)

    mars_df = tables[0]

    mars_df.columns=['Measurement', 'Value']

    mars_df.set_index('Measurement', inplace = True)

    mars_table = mars_df.to_html(classes="table table-striped")



    ##  MARS HEMISPHERES  ##

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemi_url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div', class_='collapsible results')

    unique_hemispheres = results.find_all('div', class_='item')

    hemisphere_names = []

    hemi_base_url = 'https://astrogeology.usgs.gov'

    for hemi in unique_hemispheres:
        title = hemi.find('h3').text
    
        partial_url = hemi.find('a', class_='itemLink product-item')['href']
    
        full_url = hemi_base_url + partial_url
    
        browser.visit(full_url)

        time.sleep(1)
    
        html = browser.html
    
        soup = BeautifulSoup(html, 'html.parser')
    
        image_url = soup.find('img', class_='wide-image')['src']
    
        full_image_url = hemi_base_url + image_url
    
        hemisphere_names.append({'title': title, 
                                'img_url': full_image_url})



    ##  STORE DATA  ##

    mars_info = {

        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "jpl_featured_image": featured_image_url,
        "mars_table": mars_table,
        "hemisphere_info": hemisphere_names
    }

    browser.quit()

    return mars_info

