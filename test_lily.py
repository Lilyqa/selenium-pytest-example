browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/")
assert browser.title == expected_title

added
