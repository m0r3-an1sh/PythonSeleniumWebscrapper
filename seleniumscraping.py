from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv

class scrapper:

    def __init__(self):
        self.tags = input("Enter the tags that you want to search ")
        self.n = int(input("Enter the no of images you want "))
        self.path = "C:\Program Files (x86)\chromedriver.exe" #mention the path of your webdriver

# this method is defined to access the pinterest and search the tags that are needed
    def accessingpinterest(self):
        try:
            driver = webdriver.Chrome(self.path)
            driver.get("https://in.pinterest.com/ideas")
            search = driver.find_element(By.NAME, 'q')
            search.send_keys(str(self.tags))
            search.send_keys(Keys.RETURN)
            actions = ActionChains(driver)
            allimages = set()
            return driver,actions,allimages
        except Exception as e:
            print("error occured"+type(e).__name__)

# based on the above results this method will fetch the images according to the reqiurement
    def fetchingimages(self):
        try:
            driver,actions,allimages = scrapper.accessingpinterest(self)
            try:
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME,'img')))
                
                while (len(allimages)<self.n):
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(6)
                    images = driver.find_elements(By.TAG_NAME,'img')
                    for image in images:
                        if (len(allimages)<self.n):
                            allimages.add(image.get_attribute('src'))
                        else:
                            driver.close()
                            break

                time.sleep(2)
                print(len(allimages))
                for i in allimages:
                    print(i)

                with open('Scrappeddata.csv','a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for i in allimages:
                        writer.writerow([i])
                print("Data appended successfully to the CSV file.")
            finally:
                driver.quit()
        except Exception as e:
            print("error occured"+type(e).__name__)

s = scrapper()
s.fetchingimages()

# this program can fetch any amount of images you want without any problem
# this scrapping program is made with the help of selenium because the contents of the website are dynamic
# in nature which makes it not possible to use a normal static scrapper library like bs4 beautifulsoup
# I have not implemented the login of pinterest functionality as it was not needed to access the website
# Just input the tag names and how many images that are needed and the program will scrape it for you
# for testing i have scrapped about 80 images urls and the program as worked fine just get it some time to run
# as the contents loaded are dynamic in nature...






















