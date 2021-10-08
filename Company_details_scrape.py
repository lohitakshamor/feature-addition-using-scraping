#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import requests
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
#import time
import numpy as np
from joblib import Parallel, delayed


# In[6]:


class company_scraping():
    def __init__(self):
        self.username = 'email_hidden'
        self.password = 'xyz'
        self.pg=[64,214,90,13,316,521,41,20,44,23,60,43,71,107,1118,87,46]
        self.sectors=['https://www.glassdoor.co.in/Explore/Top-Construction-Repair-and-Maintenance-Companies_IS.4,39_ISEC10007.htm',
             'https://www.glassdoor.co.in/Explore/Top-Education-Companies_IS.4,13_ISEC10009.htm',
             'https://www.glassdoor.co.in/Explore/Top-Accounting-and-Legal-Companies_IS.4,24_ISEC10001.htm',
             'https://www.glassdoor.co.in/Explore/Top-Aerospace-and-Defense-Companies_IS.4,25_ISEC10002.htm',
             'https://www.glassdoor.co.in/Explore/Top-Manufacturing-Companies_IS.4,17_ISEC10015.htm',
             'https://www.glassdoor.co.in/Explore/Top-Business-Services-Companies_IS.4,21_ISEC10006.htm',
             'https://www.glassdoor.co.in/Explore/Top-Biotech-and-Pharmaceuticals-Companies_IS.4,31_ISEC10005.htm',
             'https://www.glassdoor.co.in/Explore/Top-Consumer-Services-Companies_IS.4,21_ISEC10008.htm',
             'https://www.glassdoor.co.in/Explore/Top-Government-Companies_IS.4,14_ISEC10011.htm',
             'https://www.glassdoor.co.in/Explore/Top-Arts-Entertainment-and-Recreation-Companies_IS.4,37_ISEC10004.htm',
             'https://www.glassdoor.co.in/Explore/Top-Media-Companies_IS.4,9_ISEC10016.htm',
             'https://www.glassdoor.co.in/Explore/Top-Telecommunications-Companies_IS.4,22_ISEC10023.htm',
             'https://www.glassdoor.co.in/Explore/Top-Health-Care-Companies_IS.4,15_ISEC10012.htm',
             'https://www.glassdoor.co.in/Explore/Top-Finance-Companies_IS.4,11_ISEC10010.htm',
             'https://www.glassdoor.co.in/Explore/Top-Information-Technology-Companies_IS.4,26_ISEC10013.htm',
             'https://www.glassdoor.co.in/Explore/Top-Retail-Companies_IS.4,10_ISEC10022.htm',
             'https://www.glassdoor.co.in/Explore/Top-Transportation-and-Logistics-Companies_IS.4,32_ISEC10024.htm']
    
    def login(self):
        self.driver =webdriver.Chrome('/home/lohitaksha/chromedriver')
        self.driver.get("https://www.site_hidden.co.in/index.htm")
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/article/header/nav/div/div/div[4]/div[1]').click()
            time.sleep(1)
            self.driver.find_element_by_id('userEmail').send_keys(self.username)
            time.sleep(1)
            self.driver.find_element_by_id('userPassword').send_keys(self.password)
            self.driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]").click()
        except NoSuchElementException:
            pass
    
    def extract_company_details(self,company_page_url):
        self.driver.get(company_page_url)
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[1]/div/div/article[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/span/span[2]').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div[1]/article[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/a[1]/span[2]').click()
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div/article[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/span/div/div/a[1]").click()
        except NoSuchElementException:
            pass
        try:
            company=self.driver.find_element_by_xpath("//span[contains(@class, 'd-inline-flex align-items-center')]").text
        except NoSuchElementException:
            company=-1
        try:
            headquarters = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
        except NoSuchElementException:
            headquarters = -1
        try:
            website=self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Website"]//following-sibling::*').text
        except NoSuchElementException:
            website=-1
        try:
            size = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
        except NoSuchElementException:
            size = -1
        try:
            founded = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
        except NoSuchElementException:
            founded = -1
        try:
            type_of_ownership = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
        except NoSuchElementException:
            type_of_ownership = -1
        try:
            industry = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
        except NoSuchElementException:
            industry = -1
        try:
            sector = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
        except NoSuchElementException:
            sector = -1
        try:
            revenue = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
        except NoSuchElementException:
            revenue = -1
        try:
            competitors = self.driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
        except NoSuchElementException:
            competitors = -1
        return [company,headquarters,website,size,founded,type_of_ownership,industry,sector,revenue,competitors]
    
    def get_company_urls(self):
        com_links=[]
        for i in range(len(self.sectors)):
            self.driver.get(sectors[i])
            time.sleep(2)
            j=1
            while j<=self.pg[i]-1:
                j+=1
                lnks=self.driver.find_elements_by_tag_name("a")
                Links2=[x.get_attribute('href') for x in lnks if '/Reviews' in x.get_attribute('href') and x.get_attribute('href') !='https://www.site_hidden/Reviews/index.htm']
                com_links.append(Links2)
                self.driver.find_element_by_xpath('/html/body/article/div/div/div/div/div/div[3]/div/ul/li[7]/button/span').click()
                time.sleep(1.5)
            return com_links


# In[ ]:


if __name__ == '__main__':
    scraping = company_scraping()
    scraping.login()
    company_urls = scraping.get_company_urls(self)
    #company_details_array=Parallel(n_jobs=4)(delayed(extract_company_details)(company_url for company_url in company_urls)
    #companydetailsdf = pd.DataFrame.from_records(company_details_array)
    #companydetailsdf.columns = companydetailsdf.columns = ['company name','headquarters','website','size','founded','type_of_ownership','industry','sector','revenue','competitors']
    #for company_url in company_urls:
        #company_details_array = extract_company_details(company_url)
    

