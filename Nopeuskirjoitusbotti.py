from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.livechat.com/typing-speed-test/#/")

time.sleep(5)
element = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]')
for i in range(507):
    try:
        element = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]')
    except Exception:
        break
    write = ActionChains(driver)
    write.send_keys(element.text + " ")
    write.perform()