from selenium import webdriver

import time


def find_all():
    url = "http://192.168.1.254/basic_-_my_devices.htm"
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)

    data = driver.find_element_by_id("wireless")
    data.click()
    data = driver.find_element_by_id("wireless_num").text # nailed it
    device_num = data
    data = driver.find_element_by_id("device_obj_box").text
    all_data = data

    driver.quit()

    return device_num, all_data

def interpret(all_data):
    data = all_data
    device_dict = {}
    data_list = data.splitlines()

    device_names = data_list[0::8]
    refined_list = []

    counter = 0
    for i in device_names:
        new_item = data_list[counter:counter+8]
        refined_list.append(new_item)
        counter += 8

    for device in refined_list:
        del device[2]
        del device[3]
        device[0] = "Name:             " + device[0]
        device[1] = "Frequency;        " + device[1]
        device[2] = "Local IP Address: " + device[2]
        device[3] = "MAC Address:      " + device[3]
        device[4] = "Uploaded Data:    " + device[4]
        device[5] = "Downloaded Data:  " + device[5]

    return refined_list

def ui(data):
    choices = ["1) List minimum information" , "2) List medium information" , "3) List maximum information", "4) Quit"]

    print("Select an option from below: \n")
    time.sleep(1)
    for i in range (len(choices)):
          print(choices[i])
    time.sleep(1)
    choice = input("\nChoice: ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        time.sleep(1)
        print("\nInvalid choice. \nPlease select again. ")
        time.sleep(1)
        choice = input("\nChoice: ")

    if choice == "1":
        minimum(data)
    if choice == "2":
        medium(data)
    if choice == "3":
        maximum(data)
    if choice == "4":
        print("\nExiting. ")

def minimum(data):
    print("")

    for device in data:
        print(device[0])
        print(device[3])
        print("")

    time.sleep(2)
    ui(data)

def medium(data):
    print("")

    for device in data:
        print(device[0])
        print(device[1])
        print(device[2])
        print(device[3])
        print("")  

    time.sleep(2)
    ui(data)

def maximum(data):
    print("")

    for device in data:
        print(device[0])
        print(device[1])
        print(device[2])
        print(device[3])
        print(device[4])
        print(device[5])
        print(device[6])
        print("")    

    time.sleep(2)
    ui(data)

def main():
    print("Scraping initiated. ")
    data = find_all()
    device_num = data[0]
    all_data = data[1]

    f = open("raw_found.txt","w")
    f.write(all_data)
    f.close()

    data = interpret(all_data)
    print("\nScraping finished. \n")
    time.sleep(1)

    ui(data)

main()
