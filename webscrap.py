import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)

products=[]
prices=[]
Ram_Sizes=[]

driver.get("https://www.flipkart.com/mobiles/~asus-zenfone-max-pro-m2/pr?sid=tyy,4io&fm=neo%2Fmerchandising&iid=M_d92ce8e6-893e-453c-a0aa-5a47d2b1b520_1.OVN5I9PFZ3SW&ppt=dynamic&ppn=dynamic&otracker=dynamic_omu_infinite_Top%2BSelling%2BMobiles_1_1.dealCard.OMU_INFINITE_OVN5I9PFZ3SW&cid=OVN5I9PFZ3SW")

content = driver.page_source
soup = BeautifulSoup(content,'lxml')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    ram=a.find('li', attrs={'class':'tVe95H'})
    products.append(name.text)
    prices.append(price.text)
    Ram_Sizes.append(ram.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Ram':Ram_Sizes}) 
df.to_csv('phonesproducts.csv', index=False, encoding='utf-8')
