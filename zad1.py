from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

korisnickoIme=driver.find_element_by_xpath("//input[@id='username']")
korisnickiSifra=driver.find_element_by_xpath("//input[@id='password']")

dugme=driver.find_element_by_xpath("//i[contains(text(),'Login')]")

pravoIme="tomsmith"
pravaSifra="SuperSecretPassword!"

korisnickoIme.send_keys(pravoIme)
korisnickiSifra.send_keys(pravaSifra)

dugme.click()
