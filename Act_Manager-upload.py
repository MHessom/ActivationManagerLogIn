from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from tkinter import *



def Edge_driver():

    # Login information for the activation manager
    Username = "UserName"
    Password = "Password"
    #Serial number as entered in UI by user
    global serial

    #Get the serial as a string
    Serial = serial.get()

    #Load up an instance of Microsoft Edge and Open Activation Manager
    driver = Edge()
    driver.get("URL")

    #Login using credentials
    User_Element = driver.find_element_by_name("Login2:txtName")
    User_Element.send_keys(Username)

    Password_Element = driver.find_element_by_name("Login2:txtPassword")
    Password_Element.send_keys(Password)

    Login_Element = driver.find_element_by_name("Login2:cmdLogin")
    Login_Element.submit()

    #Enter Serial input from user
    Serial_Element = driver.find_element_by_name("txtSearch")
    Serial_Element.send_keys(Serial)

    #Submit form
    ### NOTE: sumbit() did not work, click() does. Need to understand difference.
    Submit_Element = driver.find_element_by_name("cmdLookup")
    Submit_Element.click()

#Using TKinter initialise window for user to paster serial number

root = Tk()

#Title and size of window, minsize doesnt allow for the window to be smaller than pixels entered.
root.title('Activation Manager')
root.minsize(300,50)


serial = Entry(root)
serial.pack()
serial.focus_set()

b = Button(root,text='okay',command=Edge_driver)
b.pack(side='bottom')
root.mainloop()
   


