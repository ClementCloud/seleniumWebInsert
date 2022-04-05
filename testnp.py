from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print driver.title
print friver.current_url

# driver.quit()