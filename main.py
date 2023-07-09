from scholar import ScholarDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = ScholarDriver()
driver.search_author("Hamid D. Taghirad")
# driver.search_author("Mohammad sina Allahkaram")
# driver.get_all_publications('https://scholar.google.com/citations?hl=fr&user=ejhATTMAAAAJ')
driver.get_all_publications()
print("done")


