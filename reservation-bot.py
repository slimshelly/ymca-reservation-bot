from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import time, ctime
from datetime import datetime

USERNAME = ""
PASSWORD = ""


def main():
    login()
    wait_until_ready()

# login to the ymca website, loads current week page


def login():
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    driver.get('https://prospect-park-ymca.virtuagym.com/signin')
    username_field = driver.find_element_by_id("username")
    username_field.click()
    username_field.send_keys(USERNAME)
    password_field = driver.find_element_by_id("password")
    password_field.click()
    password_field.send_keys(PASSWORD)
    login_btn = driver.find_element_by_id("login_btn")
    login_btn.click()
    driver.get('https://prospect-park-ymca.virtuagym.com/classes/week/2021-01-26?event_type=1201&coach=0&activity_id=0&member_id_filter=0&embedded=0&planner_type=7&show_personnel_schedule=0&in_app=0&single_club=0')

# loops until it is time to book


def wait_until_ready():
    swimtime = '2021-01-23 17:00:00.00'
    while True:
        currtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if currtime >= swimtime:
                book()
                break
            else:
                print("not yet")
                time.sleep(0.5)

# clicks the session at the exact time, attempts to book it

def book():
    session_btn = driver.find_element_by_id(
        "1313502331-5f89f04bca4484-64368299")
    session_btn.click()

    wait = WebDriverWait(driver, 1)
    book_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, 'book_btn')))
    book_btn.click()
