from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

nama = "Aditya"
username = "03041282025055@student.unsri.ac.id"
password = "Keluargarn1"

mata_kuliah = dict()
mata_kuliah['Matematika Teknik'] = "10261"
mata_kuliah['Medan Elektromagnetik'] = "14962"
mata_kuliah['Dasar Sistem Kendali'] = "28960"
mata_kuliah['Metode Numerik'] = "11418"
mata_kuliah['Analisis Transien Rangkaian Listrik'] = "15034"
mata_kuliah['Konversi Energi'] = "30565"
mata_kuliah['Praktikum Dasar Sistem Telekomunikasi'] = "11664"

a = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
a.get('https://elearning212.unsri.ac.id/')
a.find_element(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[2]").send_keys(username)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[3]")[0].send_keys(password)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button")[0].click()

user = '1'
status = '0'
keterangan ='None'
def absen(key, value):
    a.get('https://elearning212.unsri.ac.id/mod/attendance/view.php?id=' + value)
    textError = a.find_elements(By.XPATH,"//h1[contains(text(), 'Error')]")
    panjangerror = len(textError)
    while(panjangerror > 0) :
        a.get('https://elearning212.unsri.ac.id/mod/attendance/view.php?id=' + value)
        textError = a.find_elements(By.XPATH,"//*[contains(text(), 'Error')]")
    tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")
    panjang = len(tombol_absen)
    if panjang > 0 :
        print(key + ' => ABSEN ADA')
        a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(text(), 'Present')]")[0].click()
        a.find_elements(By.ID,'id_submitbutton')[0].click()
    else :
        print(key + ' => ABSEN TIDAK ADA')

for key, value in mata_kuliah.items():
    absen(key, value)

