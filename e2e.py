from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_score_service():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://127.0.0.1:5000/")

    score = driver.find_element(By.ID, 'score').text

    if score in range(1, 1000):
        return True
    else:
        return False


def main_function():
    if test_score_service():
        return 0
    else:
        return -1


