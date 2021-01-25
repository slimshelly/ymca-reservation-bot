from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date
from time import time, sleep

# credentials to be filled in
USERNAME = ""
PASSWORD = ""

driver = webdriver.Chrome(ChromeDriverManager().install())

# clicks the session at the exact time, attempts to book it
def book(session_btn):
    session_btn.click()

    wait = WebDriverWait(driver, 2)
    book_btn = wait.until(EC.element_to_be_clickable((By.ID, 'book_btn')))
    book_btn.click()


# loops until it is time to book
def wait_until_ready(session_btn, countdown_time):
    sec = countdown_time.timestamp()
    while True:
        currtime = time()
        if currtime >= sec:
            book(session_btn)
            break
        else:
            sleep(0.25)
            driver.find_elements_by_class_name("close-popup")

# finds the next available session for that day
def find_session(two_days_from_now):
    # find index of column
    week_start = two_days_from_now - timedelta(days=two_days_from_now.weekday())
    delta = two_days_from_now - week_start
    index = delta.days
    day_list = driver.find_elements_by_css_selector("#schedule_content .cal_column");
    day_column = day_list[index]

    class_list = day_column.find_elements_by_css_selector(".c_holder")

    for item in class_list:
        class_name = item.find_element_by_class_name("classname").text
        class_time_str = item.find_element_by_class_name("time").text
        class_start_str = class_time_str.split('-')[0].strip()

        if class_name == "Lap Swim":
            # check if the time is the next closest one to now
            class_time = datetime.strptime(class_start_str, "%I:%M %p").time()
            countdown_time = datetime.combine(date.today(), class_time)
            time_now = datetime.now()
            if (time_now < countdown_time):
                session_btn = item.find_element_by_xpath('..')
                return (session_btn, countdown_time)

# loads page based on target date
def load_page():
    now = datetime.now()
    two_days_from_now = datetime.now() + timedelta(hours=48)
    target_date_string = two_days_from_now.strftime('%Y-%m-%d')
    driver.get('https://prospect-park-ymca.virtuagym.com/classes/week/'+ target_date_string +'?event_type=1201&coach=0&activity_id=0&member_id_filter=0&embedded=0&planner_type=7&show_personnel_schedule=0&in_app=0&single_club=0')
    return two_days_from_now

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

# main flow of execution
def main():
    login()
    two_days_from_now = load_page()
    session_btn, countdown_time = find_session(two_days_from_now)
    wait_until_ready(session_btn, countdown_time)

if __name__ == "__main__":
    main()
