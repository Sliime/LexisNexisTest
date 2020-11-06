from selenium.webdriver import Firefox  

url = "https://selenium-python.readthedocs.io/"

driver = Firefox()

driver.get(url)

getting_Starting = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[2]/a')

getting_Starting.click()

find_title_Text = driver.find_element_by_xpath('//*[@id="getting-started"]/h1')

print("O Titulo da pagina é  " + find_title_Text.text)

originalText = find_title_Text.text #Pega o texto original da pagina
setText = set(originalText) #Pega o conjunto de caracteres com set, set não permite que o conjunto tenha caracteres iguais 

result = len(originalText) == len(setText) # Compara a quantidade de caracteres, se o tamanho for igual (True), a string não tem carateres repetidos, caso contrário(false) a string possui.

if (result == True): 
    print("Sua string não possui caracteres repetidos")

else: 
    print("Sua string possui caracteres repetidos")

driver.quit()