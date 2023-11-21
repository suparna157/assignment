from selenium import webdriver 
driver = webdriver.chrome(path="C:\chromedriver.exe")
driver.maximise_window()
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

