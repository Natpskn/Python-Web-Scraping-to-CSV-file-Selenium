from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time
import csv

header_list= ["Lot_number", "Order", "Case_Number", "Asset_Type", "Rai", "Ngan", "Wa_Square", "Estimate_Price", "District", "Sub_District", "State"]

with open('../Asset.csv', 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(header_list)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("http://asset.led.go.th/newbidreg/")

driver.maximize_window()
time.sleep(1)

capcha_element = driver.find_element(By.XPATH, '//*[@id="pass"]')
capcha = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/table/tbody/tr[1]/td[1]/strong/font/font")
capcha = capcha.text
capcha_element.send_keys(capcha)

State_element =  driver.find_element(By.XPATH, '//*[@id="data"]')
State = "กรุงเทพ"
State_element.send_keys(State)

Asst_type_dropdown = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div/div/div[4]/div/div[1]/table/tbody/tr/td[2]/div/select')
Asst_type_DD = Select(Asst_type_dropdown)
Asst_type_DD.select_by_index(10)

Search = driver.find_element(By.XPATH, '//*[@id="GFG_Button"]')
Search.click()


Total_Page = driver.find_elements(By.XPATH, '//*[contains(@width,"37%")]')
Total_Page = str(Total_Page[1].text)
Total_Page = Total_Page[7:]
Total_Page = Total_Page.replace(" ","")
Total_Page = Total_Page.split("/")
Current_page = int(Total_Page[0])
Last_page = int(Total_Page[1])
print('Current_page', Current_page)
print('Last_page',Last_page)

for j in range(Last_page):
    Lot_Number = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[1]')  #Lot_Number
    Order = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[2]')  #Order
    Case_Number = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[3]')  #Case_Number
    Asset_Type = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[4]')  #Asset_Type
    Size_01 = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[5]')  #Size_01(Rai)
    Size_02 = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[6]')  #Size_02(Ngan)
    Size_03 = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[7]')  #Size_03(Wa-square)
    Estimate_Price = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[8]')  #Estimate_Price
    District = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[9]')  #District
    Sub_District = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[10]')  #Sub_District
    State = driver.find_elements(By.XPATH, '//*[@id="box-table-a"]/table/tbody/tr/td[11]')  #State

    start_time = time.perf_counter()
    
    with open('../Asset.csv', 'a', encoding='utf-8-sig') as file:
        for i in range(len(Lot_Number)):
            iLot_Number = Lot_Number[i].text
            iOrder= Order[i].text
            iCase_Number = Case_Number[i].text
            iAsset_Type = Asset_Type[i].text
            iRai = Size_01[i].text
            iNgan = Size_02[i].text
            iWa_Square = Size_03[i].text
            iEstimate_Price = str(Estimate_Price[i].text)
            iEstimate_Price = iEstimate_Price.replace(",","")
            iDistrict = District[i].text
            iSub_District = Sub_District[i].text
            iState = State[i].text

            file.write(f'{iLot_Number},{iOrder},{iCase_Number},{iAsset_Type},{iRai},{iNgan},{iWa_Square},{iEstimate_Price},{iDistrict},{iSub_District},{iState}\n')
        next = driver.find_element_by_xpath('//*[contains(text(),"[Next]")]')
        print(next)
        next.click()
    end_time = time.perf_counter()
    print(f"Time take {end_time-start_time:0.4f} seconds")
    On_page = j+1
    print("On_page: ", On_page)
    file.close()
driver.close()
