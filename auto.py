from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# PARAMETERS
FIREFOX_BINARY_PATH = '/CHANGE-ME/firefox'
#FILE_DOWNLOAD_PATH = '/tmp'
LOGIN = 'CHANGE-ME'
PASSWORD = 'CHANGE-ME'

# prep firefox binary
binary = FirefoxBinary(FIREFOX_BINARY_PATH)

# prep profile for disabling download dalog
profile = FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", FILE_DOWNLOAD_PATH)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream");
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.showWhenStarting", False);

driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)

# LOGIC
driver.get("https://www.packtpub.com/packt/offers/free-learning");
driver.find_element_by_css_selector("div.book-claim-token-inner > input.form-submit").click()
driver.find_element_by_css_selector("#packt-user-login-form > div > #login-form > #login-form-email > #email-wrapper > #email").clear()
driver.find_element_by_css_selector("#packt-user-login-form > div > #login-form > #login-form-email > #email-wrapper > #email").send_keys(LOGIN)
driver.find_element_by_css_selector("#packt-user-login-form > div > #login-form > #login-form-pass > #password-wrapper > #password").clear()
driver.find_element_by_css_selector("#packt-user-login-form > div > #login-form > #login-form-pass > #password-wrapper > #password").send_keys(PASSWORD)
driver.find_element_by_css_selector("#packt-user-login-form > div > #login-form > #login-form-submit > #edit-submit-1").click()
driver.find_element_by_css_selector("div.book-claim-token-inner > input.form-submit").click()

browser.close()
