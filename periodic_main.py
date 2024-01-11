from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def dictionify(web_elements, headers):
    new_dict = {}

    for header, element in list(zip(headers, web_elements)):
        new_dict[header] = element.text
    return new_dict



#Init drivers
driver = webdriver.Chrome()

second_driver = webdriver.Chrome()

#Route driver 1

driver.get("https://efdsearch.senate.gov/")


driver.find_element(By.XPATH, "//input[@id='agree_statement']").click()
sleep(3)

#Route driver 2

second_driver.get("https://efdsearch.senate.gov/")
second_driver.find_element(By.XPATH, "//input[@id='agree_statement']").click()


#Driver 1 table init operations

driver.find_element(By.XPATH, "//input[@class='form-check-input senator_filer']").click()

####
driver.find_element(By.XPATH, "//label[@id='reportTypeLabelPtr']").click()
#####

driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(3)

driver.find_element(By.XPATH, "//th[@aria-label='Date Received/Filed: activate to sort column ascending']").click()
sleep(1)

driver.find_element(By.XPATH, "//th[@aria-label='Date Received/Filed: activate to sort column descending']").click()
sleep(1)




outer_heading_row = [heading_value.text for heading_value in driver.find_elements(By.XPATH, "//thead//tr//th")]




outer_data = []
inner_data = []

page = 1

done = False

while not done:
    

    outer_table_rows = driver.find_elements(By.XPATH, "//tbody//tr[@role='row']")
    for outer_table_row in outer_table_rows:    
        outer_row_values = outer_table_row.find_elements(By.XPATH, ".//td")


        
        second_driver.get(outer_row_values[3].find_element(By.XPATH, ".//a").get_attribute("href"))
        sleep(3)

        try:
            ##
            transaction_table = second_driver.find_element(By.XPATH, "//table[@class='table table-striped']")
            ##
            inner_heading_row = [heading_value.text for heading_value in transaction_table.find_elements(By.XPATH, ".//thead//tr//th")]
            ####
            inner_table_rows = transaction_table.find_elements(By.XPATH, ".//tbody//tr")   
            ####

            for inner_table_row in inner_table_rows:
                inner_row_values = inner_table_row.find_elements(By.XPATH, ".//td")


                
                inner_dict = dictionify(inner_row_values, inner_heading_row)
                if inner_dict['Ticker'] != "--":
                    ###deleted line
                    inner_data.append(inner_dict)
                    outer_data.append(dictionify(outer_row_values, outer_heading_row))

        except NoSuchElementException:
            print(outer_row_values[3].find_element(By.XPATH, ".//a").get_attribute("href"))
            pass
    try:
        driver.find_element(By.XPATH, "//a[@class='paginate_button next']").click()
        page += 1
        sleep(3)
    except NoSuchElementException:
        done = True

    
    if page == 60:
        done = True



dataset = []

for outer_row, inner_row in zip(outer_data, inner_data):
    outer_row.update(inner_row)
    dataset.append(outer_row)


with open("senator_trading_dataset2222.json", "w") as jsonfile:
    json.dump(dataset, jsonfile)
