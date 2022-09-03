from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='/Users/gunther/Downloads/chrome/chromedriver', chrome_options=option)
browser.get("https://account.t-mobile.com/signin/v2/")
try:
    WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='text_box_group text_box_group_height']")))
except:
    print("Timed out waiting for page to laod")
    browser.quit()
browser.find_element(By.ID, "usernameTextBox").send_keys("6087720364" + Keys.ENTER)
browser.find_element(By.ID, "passwordTextBox").send_keys("jMJeAKubieZy52" + Keys.ENTER)

#Click View bill
browser.find_element(By.LINK_TEXT, "View bill").click()

#select historical overview
browser.find_element(By.ID, "history-tab").click()


#select latest bill value 
latest_amt=browser.find_element(By.CLASS_NAME, "bb-past-bills-amount").text

#select the month of the latest bill
latest_month=browser.find_element(By.CLASS_NAME, "bb-past-bills-cycle").text

#go to the month
browser.find_element(By.CLASS_NAME, "bill-details").click()



#select view by line
browser.find_element(By.ID, "line-tab").click()

#Account total 
account_bill = browser.find_element(locate_with(By.CLASS_NAME, "bb-charge-amount").to_right_of({By.CLASS_NAME: "bb-charge-title"})).text

#Get Customer Name
browser.find_element(By.ID, "cust_name0").text

#Get Customer Number
browser.find_element(By.ID, "cust_msisdn0").text

#Get Customer bill 
browser.find_element(locate_with(By.CLASS_NAME, "bb-charge-amount").to_right_of({By.ID: "cust_msisdn0"})).text

for i in range(12):
    cust_name="cust_name"+str(i)
    cust_number="cust_msisdn"+str(i)
    print("cust_name: ", browser.find_element(By.ID, cust_name).text + "\t" + browser.find_element(By.ID, cust_number).text + "\t" + 
         browser.find_element(locate_with(By.CLASS_NAME, "bb-charge-amount").to_right_of({By.ID: cust_number})).text)


#graph historical data
first_graph=browser.find_elements(By.XPATH, "//*[@id='historicalChartG']")
