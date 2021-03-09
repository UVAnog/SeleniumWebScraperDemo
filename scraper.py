from selenium import webdriver

######## configuring the webdriver ########

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

######## begin the scraping part ########

from selenium.webdriver.common.keys import Keys
import requests as rq
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

######## importing the driver ########
wd = webdriver.Chrome('the path to your chromedriver',options=options)
wd.get("the url of the webpage you want to scrape")

######## this is a delay on performing the scrape in order for the page to load before we scrape it ########

a = WebDriverWait(wd, 10).until(
             EC.presence_of_element_located((By.XPATH, '//*[the class of the item you want to scrape]')))
#print(a.text)
# or:
for i in a:
    available = a.text

print(available)


######## sending the email ########
import smtplib as smtplib

# replace x with the particular word the site uses i.e "Out of Stock", "Not Available", "Sold Out" if the item is sold out
if (available != "x"):
  sender = "your email to send from"
  receiver = ["the email you want to send updates to"]
  subject = "The subject of the email" #feel free to change this and the message
  text = "The message of the email"
  message = 'Subject: {}\n\n{}'.format(subject, text)
  
  try:
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,'the password to your sender email')
    session.sendmail(sender,receiver,message)
    session.quit()
  except smtplib.SMTPException:
    print('Error')
else:
  print("The item you want is not available.")

