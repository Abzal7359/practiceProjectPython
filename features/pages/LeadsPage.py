import time

from selenium.webdriver.common.by import By

from features.pages.TasksPage import TasksPage


class LeadsPage:
    def __init__(self,driver):
        self.driver=driver

    AddLead_XPATH="//div[@class='flex justify-between px-2' and text()=' Add Lead ']"

    #mandatory fields
    firstname_XPATH="//input[@id='first-name ']"
    lastname_XPATH="//input[@id='last-name']"
    email_XPATH="//input[@id='email']"
    mobileNumber_XPATH="//input[@id='phone-number']"
    AssignedTo_XPATH="(//button[contains(@class,'pr-3')])[3]"
    assigningPerson_XPATH="(//label[normalize-space()='kishor kharade'])[1]"
    campaign_XPATH="(//button[contains(@class,'pr-3')])[4]"
    campaignSelect_XPATH="(//label[normalize-space()='bajaj'])[1]"
    Labels_XPATH="(//button[contains(@class,'p-0')])[2]"
    warmerLabel_XPATH="(//input[@id='selectedItem-1'])[1]"
    Description_XPATH="//textarea[@id='descriptionInfo']"


    save_XPATH="(//button[normalize-space()='Save'])[1]"
    Activity_text_area_XPATH="(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])"
    mail_validation_XPATH="//div[@class='mt-2']//p[@class='ng-star-inserted']"

    Tasks_XPATH="//a[@id='task']"


    def clickAddLead(self):
        self.driver.find_element(By.XPATH,self.AddLead_XPATH).click()

    def enter_Mandatory_Fields(self,firstName,lastname,email,mobile,description):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.firstname_XPATH).clear()
        self.driver.find_element(By.XPATH, self.firstname_XPATH).send_keys(firstName)
        self.driver.find_element(By.XPATH,self.lastname_XPATH).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(email)
        self.driver.find_element(By.XPATH, self.mobileNumber_XPATH).send_keys(mobile)
        self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Manual']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Word of mouth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.AssignedTo_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.assigningPerson_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.campaign_XPATH).click()

        self.driver.find_element(By.XPATH,self.campaignSelect_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.Labels_XPATH).click()
        self.driver.find_element(By.XPATH,self.warmerLabel_XPATH).click()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click()",self.driver.find_element(By.XPATH, self.Labels_XPATH))
        # self.driver.find_element(By.XPATH, self.Labels_XPATH).click()
        self.driver.find_element(By.XPATH,self.Description_XPATH).send_keys(description)
        time.sleep(2)


    def clickAddLeadSave(self):
        self.driver.find_element(By.XPATH,self.save_XPATH).click()
        time.sleep(2)

    def isLeadCreated(self,expect,expectmail):
        boolean = False
        l=self.driver.find_elements(By.XPATH, self.Activity_text_area_XPATH)
        for i in l:
            actuall = i.text
            Expected = expect
            if Expected in actuall:
                boolean = True
                break


        boolean_mail=False

        actuall_mail = self.driver.find_element(By.XPATH, self.mail_validation_XPATH).text
        Expected_mail = expectmail
        if Expected_mail in actuall_mail:
            boolean_mail=True

        l=[boolean,boolean_mail]
        if False not in l:
            return True
        else:
            return False


    def clickOnTasksPage(self):
        self.driver.find_element(By.XPATH, self.Tasks_XPATH).click()

        return TasksPage(self.driver)


