import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.set_capability('unhandledPromptBehavior', 'accept')

answers = {'Yes':1, 'No':2, 'Dunno':3}
executable_path = 'C:/Users/Компьютер/Desktop/chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path, options=option)

for _ in range(100):
    question1 = random.randint(1,5)
    question2 = random.randint(1,4)
    question3 = random.randint(1,4)
    question4 = random.choice(list(answers))

    url = (
        f'https://docs.google.com/forms/d/e/1FAIpQLSfchqVHQ1I89K3MBv081j9gJJfA7zZ6fyTpua3K6Hk5FUFH-w/viewform?usp=pp_url'
        f'&entry.824939393={question1}'
        f'&entry.1148448411=Option+{question2}'
        f'&entry.1093979098=Option+{question3}'
        f'&entry.539828997={question4}'
    )
    
    driver.get(url)
    button = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
    button.click()
