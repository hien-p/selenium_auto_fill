from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import csv
import random
import pandas as pd
from tqdm import tqdm
def read_data_csv(data):

    # Read the CSV file
    df = pd.read_csv(data,sep=";", engine="python", skipfooter=1)

    return df



def fill_google_form():
   
    

    # page 1 
    datasets = read_data_csv("TAM-data.csv")
    for i in tqdm(range(0, len(datasets.values))):
        chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless=new") # for Chrome >= 109
        # chrome_options.add_argument("--headless")
        # chrome_options.headless = True # also works
        driver = webdriver.Chrome(options=chrome_options)
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdDCs4PawrJaQ-RscLJYeEUSxLOdpf4v5iU8BYTtbHNZtaBLA/viewform?usp=sf_link'

        driver.get(form_url)
        
        # submit questions
        time.sleep(2)
        #/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div
        submit_button = driver.find_element(By.XPATH,'//*[@id="i5"]/div[3]/div')
        submit_button.click()

        # random number
    
        random_number = random.choice([24, 21, 18, 15])
        # choose the role
        role_button = driver.find_element(By.XPATH,'//*[@id="i{random_number}"]/div[3]/div'.format(random_number=random_number)).click()
        
        # next buttons 
        next_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
        

        datavalues = datasets.values[i].tolist()
        # First 
        first = datavalues[:6]
        second_half = datavalues[6:12] # next 6 elements
        thirhd_half = datavalues[11:18] # next 6 elements
        fourth_half = datavalues[18:24] # next 6 elements

       
        # print all 
        fill_form_6_rows(driver,first)

        # next_button
        next_button_con(driver)

        # page 2
        fill_form_6_rows(driver, second_half)
        next_button_con(driver)

        # page 3    
        fill_form_2_rows(driver, thirhd_half[:2])
        next_button_con(driver)

        # page 4 
        fill_form_2_rows(driver, thirhd_half[2:4])
        next_button_con(driver)

        # page 5
        fill_form_2_rows(driver, thirhd_half[4:6])
        next_button_con(driver)
        
        # page 6 
        fill_form_6_rows(driver, fourth_half)
        next_button_con(driver)
        # Close the browser window
        driver.quit()
        time.sleep(10)
        

 
    


        
    



def next_button_con(driver):
    # //*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span 
    next_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    next_button.click()


def fill_form_6_rows(driver, list_input):


    # column = [x for x in range(2, 8)] # 2 3 4 5 6 7 
    

    # make all elment in list input + 1
    list_input = [x + 1 for x in list_input]
    
    # data thi 1 2 3 4 5 6 
        
    for rows in range(2,13,2):
        choice = list_input[0]
        #random_column = random.choice(column)   
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{rows}]/span/div[{column}]/div/div/div[3]/div'.format(rows= rows, column=choice)).click()
        list_input.pop(0)



def fill_form_2_rows(driver, list_input):
   
    
    list_input = [x + 1 for x in list_input]
    
    for rows in range(2,5,2):
        choice = list_input[0]
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[{rows}]/span/div[{column}]/div/div/div[3]/div'.format(rows= rows, column=choice)).click()
        list_input.pop(0)

    
# fill_google_form()


fill_google_form()