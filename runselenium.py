from selenium import webdriver                  #BASIS FOR SELENIUM
from selenium.webdriver.common.by import By     #SEARCH WEBPAGE
from selenium.webdriver.common.keys import Keys #TYPE UTILIZE KEYBOARD I

browserEdge = webdriver.Edge()
browserEdge.get('file:///C://Users//jayso//Documents//Code//Selenium//seleniumsite.html')


print(browserEdge.title)                                #GETS PAGE'S TITLE
print()

web_elem1 = browserEdge.find_element(By.TAG_NAME, "h1") #FINDS AN ELEMENT(USING TAG(h1))
print(web_elem1.text)                                   #PRINTS CONTENT OF ELEMENT1

my_html_link = browserEdge.find_element(By.ID, 'my_html_link')
print(my_html_link.text)                                #USES .TEXT TO PRINT TEXT CONTENT
print()
my_html_link.click()                                    #GOES TO PERPETUAL MOODLE

web_elem2 = browserEdge.find_element(By.CLASS_NAME, "aalink")
web_elem2.click()                                       #GO TO LOGIN PAGE

web_elem3 = browserEdge.find_element(By.ID, "loginguestbtn")
web_elem3.click()                                       #LOGIN AS GUEST

web_elem_alamp = browserEdge.find_element(By.XPATH, "//*[@id='module-2']/div/div[1]/div/div[1]/div/div[2]/div[2]/a")
web_elem_alamp.click()   #XPATH IS COMPLICATED, IT IS THE BRANCH OF THE DOCTREE TO ACCESS THIS ELEMENT, SIMILAR TO DIRECTORY TRE
#//* MEANS START AT THIS UNIQUE SPOT morestepsup/[@criteria=name]/morestepsdown
#web_elem_lamp = browserEdge.find_element(By.XPATH, "//*[@id='module-3']/div/div[1]/div/div[1]/div/div[2]/div[2]/a")
#web_elem_lamp.click()



#web_elem = browserEdge.find_element(By.ID,'ybar-sbq') #ONLY USEFUL ON YAHOO.COM, IS THE UID FOR A SEARCH BOX
#FINDING BY ID IS THE BEST WAY
#web_elem.send_keys('Selenium download')               #SENDS KEYSTROKES TO THE ELEMENT
#web_elem.submit()                                     #SUBMIT/ENTER




input("Press any key to exit.")
browserEdge.quit()