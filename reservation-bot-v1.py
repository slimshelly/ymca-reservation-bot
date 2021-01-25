from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep
from datetime import datetime

# variables to be filled in
USERNAME = ""
PASSWORD = ""
BOOKING_TIME = "2021-01-25 07:30:00.00"
SESSION_ID = "544614269-5f91dac96641f3-69299650"

driver = webdriver.Chrome(ChromeDriverManager().install())

# clicks the session at the exact time, attempts to book it
def book():
    session_btn = driver.find_element_by_id(SESSION_ID)
    session_btn.click()

    wait = WebDriverWait(driver, 2)
    book_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, 'book_btn')))
    book_btn.click()

# loops until it is time to book
def wait_until_ready():
    slot_time_obj = datetime.strptime(BOOKING_TIME,'%Y-%m-%d %H:%M:%S.%f')
    sec = slot_time_obj.timestamp()
    print(sec)
    while True:
        currtime = time()
        print(currtime)
        if currtime >= sec:
            book()
            break
        else:
            print("not yet")
            sleep(0.25)
            driver.find_elements_by_class_name("close-popup")


# login to the ymca website, loads current week page
def login():
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


def main():
    login()
    wait_until_ready()


if __name__ == "__main__":
    main()
