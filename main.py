import time
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_winner(driver):
    driver.maximize_window()
    driver.get("https://www.winner.co.il")


def winner_login(driver, username, password):
    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR, 'button[id="top-login-btn"]').click()

    time.sleep(5)
    username_field = driver.find_element(By.ID, 'userName')
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    input("Press any key to exit...")


    def main():
        load_dotenv()
        driver = webdriver.Chrome("D:\WinnerAutoBetResources\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        open_winner(driver)
        winner_login(driver, os.getenv("WINNER_USERNAME"), os.getenv("WINNER_PASSWORD"))


    if __name__ == "__main__":
        main()
