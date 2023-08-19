import time

from selenium.webdriver.common.by import By


class LeadsProfile:
    def __init__(self,driver):

        self.driver=driver

    name=""

    leadsProfile_XPATH="(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]"
    assignedPerson_XPATH="(//button[contains(@class,' pr-3')])[1]"
    labelButton_XPATH="(//button[contains(@class,' pr-3')])[2]"
    sourceTypeButton_XPATH="(//button[contains(@class,' pr-3')])[3]"
    sourceButton_XPATH="(//button[contains(@class,' pr-3')])[4]"
    campaignButton_XPATH="(//button[contains(@class,' pr-3')])[5]"

    l=[]

    def getleadsProfiletext(self):
        return self.driver.find_element(By.XPATH,self.leadsProfile_XPATH).text

    def clickOnLeadsProfile(self):

        self.name=self.getleadsProfiletext()
        self.driver.find_element(By.XPATH,self.leadsProfile_XPATH).click()
        time.sleep(3)



    def clickToChangeAssignedPerson(self):
        self.driver.find_element(By.XPATH, self.assignedPerson_XPATH).click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Venkatesh Iyer'])[1]").click()
        time.sleep(3)
        actuall=self.driver.find_element(By.XPATH,"(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])[1]").text
        if "assigned" in actuall:
            self.l.append(True)
        else:
            self.l.append(False)

    def clickTo_Add_label(self):
        self.driver.find_element(By.XPATH, self.labelButton_XPATH).click()
        self.driver.find_element(By.XPATH, "(//input[@id='selectedItem-0'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.labelButton_XPATH).click()
        actuall = self.driver.find_element(By.XPATH,"(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])[1]").text
        if "label" in actuall:
            self.l.append(True)
        else:
            self.l.append(False)

    def clickTo_Change_source(self):
        self.driver.find_element(By.XPATH, self.sourceTypeButton_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Digital'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.sourceButton_XPATH).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Facebook'])[1]").click()
        time.sleep(2)
        actuall = self.driver.find_element(By.XPATH,"(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])[1]").text
        if "source" in actuall:
            self.l.append(True)
        else:
            self.l.append(False)
    def clickToChange_CampaignType(self):
        self.driver.find_element(By.XPATH, self.campaignButton_XPATH).click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Referral'])[1]").click()
        time.sleep(2)
        actuall = self.driver.find_element(By.XPATH,"(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])[1]").text
        if "campaign" in actuall:
            self.l.append(True)
        else:
            self.l.append(False)
    def isLeadProfile_Modified(self):
        if False not in self.l:
            return True
        else:
            return False