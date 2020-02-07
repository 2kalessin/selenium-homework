from selenium import webdriver
import time
import os

with open("file.txt", "w") as file:
    content = file.write("automationbypython")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Pashka")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Kakashka")
input3 = browser.find_element_by_name("email")
input3.send_keys("cool@xakep.bro")

upload = browser.find_element_by_name("file")
upload.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(15)
browser.quit()
