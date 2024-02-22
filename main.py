from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import csv
import random


def read_data_csv(data):
    pass

def fill_google_form():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()


    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdDCs4PawrJaQ-RscLJYeEUSxLOdpf4v5iU8BYTtbHNZtaBLA/viewform?usp=sf_link'
    driver.get(form_url)
    
    # submit questions
    time.sleep(2)
    #/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div
    submit_button = driver.find_element(By.XPATH,'//*[@id="i5"]/div[3]/div')
    submit_button.click()

    # random number
    array_number = [24, 21, 18, 15]
    random.shuffle(array_number)
    random_number = array_number[0]
    print(random_number)

    # choose the role
    role_button = driver.find_element(By.XPATH,'//*[@id="i{random_number}"]/div[3]/div'.format(random_number=random_number)).click()
    
    # next buttons 
    next_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    
    #driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{rows}]/span/div[{column}]/div/div/div[3]/div'.format(rows= 2, column=2)).click()

    # page 1 
    fill_form_6_rows(driver)
    # next_button 
    next_button_con(driver)
    # page 2    
    fill_form_6_rows(driver)
    # next_button 
    next_button_con(driver)
    
    # pagge 3 
    fill_form_2_rows(driver)
    # next_button 
    next_button_con(driver)

    # pagge 4
    fill_form_2_rows(driver)
    # next_button 
    next_button_con(driver)

    # pagge 5
    fill_form_2_rows(driver)
    # next_button 
    next_button_con(driver)

     # page 6 
    fill_form_6_rows(driver)
    # next_button 
    next_button_con(driver)
    time.sleep(8)


        
    # Close the browser window
    driver.quit()


def next_button_con(driver):
    # //*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span 
    next_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    next_button.click()


def fill_form_6_rows(driver):


    column = [x for x in range(2, 8)]
    
    for rows in range(2,13,2):
        random_column = random.choice(column)   
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{rows}]/span/div[{column}]/div/div/div[3]/div'.format(rows= rows, column=random_column)).click()

    print(column, rows)



def fill_form_2_rows(driver):
    column = [x for x in range(2, 8)]
    rows = [x for x in range(2, 5, 2)]
    
    for rows in range(2,5,2):
        random_column = random.choice(column)   
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{rows}]/span/div[{column}]/div/div/div[3]/div'.format(rows= rows, column=random_column)).click()


    
fill_google_form()
