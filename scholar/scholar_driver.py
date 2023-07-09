from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class ScholarDriver(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super().__init__(options=chrome_options)
        self.get("https://scholar.google.com")

    def search(self, query):
        wait = WebDriverWait(self, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "q")))

        search_box = self.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

    def search_author(self, query):
        self.search(query)
        wait = WebDriverWait(self, 10)
        wait.until(EC.presence_of_element_located((By.ID, "gs_hdr_mnu")))
        self.find_element(By.ID, "gs_hdr_mnu").click()

        # click on Profils
        items = self.find_elements(By.CSS_SELECTOR, "#gs_hdr_drw_in a span")
        for item in items:
            print(item.text)
            if item.text == "Profils":
                item.click()
                break

        # click on the first result
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gsc_sa_ccl a")))
        self.find_element(By.CSS_SELECTOR, "#gsc_sa_ccl a").click()

    def get_all_publications(self, URL=None):
        if URL:
            self.get(URL)
        show_more = self.find_element(By.ID, "gsc_bpf_more")
        wait = WebDriverWait(self, 10)
        while show_more.is_enabled():
            show_more.click()
            show_more = self.find_element(By.ID, "gsc_bpf_more")
            try:
                wait.until(EC.element_to_be_clickable((By.ID, "gsc_bpf_more")), "show more button is not clickable")
            except Exception as e:
                print(str(e))
                if "show more button is not clickable" in str(e):
                    print("show more button is not clickable more")
                    break
                else:
                    raise e

        # get all publications
        publications = self.find_elements(By.CSS_SELECTOR, ".gsc_a_tr")
        for publication in publications:
            captcha_flag = False
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gsc_a_at")), "no such element")
            except Exception as e:
                print(str(e))
                if "no such element" in str(e):
                    print("no such element")
                    if "https://www.google.com/sorry" in self.current_url:
                        input("please do the captcha and press enter")
                        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gsc_a_at")),
                                   "no such element")
                else:
                    raise e

            publication.find_element(By.CSS_SELECTOR, ".gsc_a_at").click()
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gsc_oci_title")), "no such element")
            except Exception as e:
                print(str(e))
                if "no such element" in str(e):
                    print("no such element")
                    if "https://www.google.com/sorry" in self.current_url:
                        input("please do the captcha and press enter")
                        captcha_flag = True
                        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gsc_oci_title")),
                                   "no such element")

                else:
                    raise e
            title = self.find_element(By.CSS_SELECTOR, "#gsc_oci_title").text
            authors = self.find_element(By.CSS_SELECTOR, ".gsc_oci_value").text

            try:
                summary = self.find_element(By.CSS_SELECTOR, "#gsc_oci_descr").text
            except Exception as e:
                summary = ""

            elem = self.find_elements(By.CSS_SELECTOR, ".gs_scl")[1]
            year = elem.find_element(By.CSS_SELECTOR, ".gsc_oci_value").text
            year = year.split('/')[0].strip()
            try:
                year = int(year)
            except Exception as e:
                year = None

            print("title")
            print(title)
            print("authors")
            print(authors)
            print("summary")
            print(summary)
            print(year)
            print()
            self.back()
            if captcha_flag:
                self.back()
