import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def decorator(d):
    for i in d:
        print(f'{i} , {d[i]}')

url="https://oas.iitmandi.ac.in/instituteprocess/common/login.aspx"

user = input("Enter your username: ")
pswd = input("Enter your password: ")
date = input("Enter date in DDMMYYYY Format: ")

user_route = int(input('''
Enter 1 for North campus to Mandi,\n
Enter 2 for Mandi to North campus,\n
Enter 7 for North campus to mandi direct,\n
'''))

browser = webdriver.Chrome()

# browser = webdriver.Remote(
#     command_executor="http://43.204.110.52:4445/wd/hub",
#     options=webdriver.ChromeOptions(),
# )

info={}
try:


    browser.get(url)
    username = browser.find_element(By.ID,'txtLoginId')
    password = browser.find_element(By.ID,'txtPassword')
    submit = browser.find_element(By.ID,'btnLogin')
    username.send_keys(user)
    password.send_keys(pswd)
    submit.send_keys(Keys.RETURN)

    time.sleep(2)

    browser.get('https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx')
    time.sleep(2)

    dat = browser.find_element(By.ID,'txtFromDate')
    time.sleep(1)
    for i in range(10):
        dat.send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    for i in date:
        dat.send_keys(i)
    time.sleep(1)
    dat.send_keys(Keys.RETURN)
    time.sleep(1)

    route = browser.find_element(By.ID,'ddlRoute')
    route_options = route.find_elements(By.TAG_NAME,'option')
    for option in route_options:
        try:
            if(int(option.get_attribute('value'))==user_route):
                option.click()
                break
        except:
            continue

    time.sleep(1)
    schedule = browser.find_element(By.ID,'ddlTiming')
    time_options = schedule.find_elements(By.TAG_NAME,'option')
    n=len(time_options)
    for i in range(1,n):
        schedule = browser.find_element(By.ID,'ddlTiming')
        time_options = schedule.find_elements(By.TAG_NAME,'option')
        t = time_options[i]
        time_txt = t.text
        t.click()
        time.sleep(2)
        bus = browser.find_element(By.ID,'ddlBus')
        bus_options = bus.find_elements(By.TAG_NAME,'option')
        for j in range(1,len(bus_options)):
            bus = browser.find_element(By.ID,'ddlBus')
            bus_options = bus.find_elements(By.TAG_NAME,'option') 
            b = bus_options[j]
            bus_text = b.text
            b.click()
            time.sleep(2)
            available=browser.find_element(By.ID,'lblAvilable')
            info[f"{time_txt} , {bus_text}"] = int(available.text)
            time.sleep(1)
    decorator(info)
    browser.quit()

except:
    print('Some error occured, dont blame my script, The script runs on a 1gb ram and a shared 1vcpu server so it has its limitations')
    try:
        decorator(info)
    except:
        pass
    browser.quit()



