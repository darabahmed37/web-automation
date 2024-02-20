from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from json import load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import uniform


def open_file():
    with open("pending_follow_requests.json", "r") as file:
        data = load(file)
        data = [
            x["string_list_data"][0]["href"]
            for x in data["relationships_follow_requests_sent"]
        ]
        return list(reversed(data))


def get_element(path: str, driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))


def automate():
    options = Options()

    options.add_argument(r"--profile-directory=Profile 1")
    options.add_argument(r"--user-data-dir=/home/dev/.config/google-chrome/")
    driver = webdriver.Chrome(options=options)
    follow_requests = open_file()
    for request in follow_requests:
        driver.get(request)
        driver.implicitly_wait(10)
        element = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button",
        )
        print(element)
        element.click()
        element.find_element(
            By.XPATH,
            "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]",
        ).click()
        print(f"unfollowed {driver.title}")

        sleep(uniform(1, 3))


if __name__ == "__main__":
    automate()
