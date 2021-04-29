from selenium import webdriver

driver=webdriver.Chrome()



driver.get("https://the-internet.herokuapp.com/login")

korisnickoIme=driver.find_element_by_css_selector("#username")
korisnickiSifra=driver.find_element_by_css_selector("#password")

dugme=driver.find_element_by_css_selector("div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example form:nth-child(3) button.radius:nth-child(3) > i.fa.fa-2x.fa-sign-in")

pravoIme="tomsmith"
pravaSifra="SuperSecretPassword!"

korisnickoIme.send_keys(pravoIme)
korisnickiSifra.send_keys(pravaSifra)

dugme.click()