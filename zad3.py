from selenium import webdriver
import time

ime = {
    "vuk":"prozor",
    "dusan":"laptop",
    "comtrade":"qa",
    "tomsmith":"SuperSecretPassword!"
}

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
# find_element_by_css_selector

#ime.items je vuk:prozor itd... element recnika

for key,value in ime.items():
    korsnickoime=driver.find_element_by_css_selector("#username")
    korsnickasifra=driver.find_element_by_css_selector("#password")
    dugme=driver.find_element_by_css_selector("div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example form:nth-child(3) button.radius:nth-child(3) > i.fa.fa-2x.fa-sign-in")
    korsnickoime.send_keys(key)
    korsnickasifra.send_keys(value)
    dugme.click()
    if driver.current_url=='https://the-internet.herokuapp.com/secure': #tacan log in link
        print(key,value,'Prosao Test')
    else:
        print(key,value,'Nije Prosao Test') #ako se ne loguje
    time.sleep(2)
    driver.refresh()
