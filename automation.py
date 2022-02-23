import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://cleancode-stg.prospark.co/')
    # driver.maximize_window()
    yield driver

def test_add(driver):
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[1]/input').send_keys('ihsantrainer')
    driver.find_element_(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[2]/input').send_keys('P@ssword123' + Keys.ENTER)
    time.sleep(7)

    trainingbtn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/ul/li[3]/a')
    ActionChains(driver).move_to_element(trainingbtn).perform()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/ul/li[3]/div/div/a[2]').click()

    driver.find_element(By.XPATH,'//*[@id="btn-add-course"]').click()

    driver.find_element(By.XPATH,'//*[@id="course-name"]').send_keys('TestAutomation')
    select = Select(driver.find_element_by_id('category-select'))
    select.select_by_value('5')
    driver.find_element(By.XPATH,'//*[@id="course-description"]').send_keys('TestAutomation')

    driver.find_element(By.XPATH,'//*[@id="start_date"]').click()
    driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/table/tfoot/tr[1]/th').click()


    driver.find_element(By.XPATH,'//*[@id="end_date"]').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/table/tfoot/tr[1]/th').click()
    
    driver.find_element(By.XPATH,'//*[@id="number_of_failed_attempts"]').send_keys('10')

    driver.find_element_by_xpath('//*[@id="save-course-button"]').click()

def test_assign(driver):
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[1]/input').send_keys('ihsantrainer')
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[2]/input').send_keys('P@ssword123' + Keys.ENTER)
    time.sleep(10)

    trainingbtn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/ul/li[3]/a')
    ActionChains(driver).move_to_element(trainingbtn).perform()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/ul/li[3]/div/div/a[2]').click()
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="m_datatable"]')))
        print('data muncul')

    except TimeoutException:
        print("data tidak muncul")
        pass

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[2]/td[3]/span/div/button'))).click()
        print('data muncul')

    except TimeoutException:
        print("data tidak muncul")
        pass

    driver.find_element(By.XPATH, '//*[@id="users-tab-link"]').click()
    driver.find_element(By.XPATH, '//*[@id="search2"]').send_keys('ihsan')
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/input'))).click()
    driver.find_element(By.XPATH, '//*[@id="add-to-course"]').click()

def test_learner(driver):
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[1]/input').send_keys('ihsanlearner')
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div[2]/div/div[1]/form/div[2]/input').send_keys('P@ssword123' + Keys.ENTER)
    time.sleep(7)

    driver.find_element(By.XPATH,'//*[@id="m_topbar_notification_icon"]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div/div[2]/div/div/ul/li[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/span[2]/b/a').click()
    time.sleep(7)

    

    

    