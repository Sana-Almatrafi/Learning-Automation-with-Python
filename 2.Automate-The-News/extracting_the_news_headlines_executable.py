from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
# to convert it to executable use the following commandline in terminal
# pyinstaller --onefile extracting_the_news_headlines_executable.py
application_path = os.path.dirname(sys.executable)

# get date in format DDMMYYYY
now = datetime.now()
day_month_year = now.strftime("%d%m%Y")

web = 'https://www.thesun.co.uk/sport/football/'
path = '/home/sana/repos/Learning-Automation-with-Python/2.Automate-The-News/chromedriver-linux64/chromedriver'  # introduce path here


# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.command_executor.set_timeout(1000)
driver.get(web)

#//div[@class="story__copy-container"]
# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="story__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/p').text
    subtitle = container.find_element(by='xpath', value='./a/h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dictionary = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dictionary)

file_name = f'football-headlines-{day_month_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()