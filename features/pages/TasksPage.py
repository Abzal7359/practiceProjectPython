import time

from selenium.webdriver.common.by import By


class TasksPage:
    def __init__(self,driver):
        self.driver=driver

    createTask_XPATH="//button[normalize-space()='Create Task']"
    textArea_XPATH="//div[@class='angular-editor-textarea']"
    priority_XPATH="(//div[contains(@class,'sm:px-6')]//div[contains(@class,'relative')])//input[@placeholder='Medium']"
    time_XPATH="//input[@id='dueTime']"
    taskSave_XPATH="//button[normalize-space()='Save']"

    List_tasks=[]

    def clickOnCreateTask(self):
        self.driver.find_element(By.XPATH,self.createTask_XPATH).click()
        time.sleep(2)

    def enterTaskDetails(self,message,timee):
        self.driver.find_element(By.XPATH, self.textArea_XPATH).send_keys(message)
        time.sleep(2)
        priority = self.driver.find_element(By.XPATH,self.priority_XPATH)
        self.driver.execute_script("arguments[0].click()", priority)
        time.sleep(2)

        p = self.driver.find_element(By.XPATH, "//label[normalize-space()='High']")
        self.driver.execute_script("arguments[0].click()", p)

        time.sleep(1)
        self.driver.find_element(By.XPATH, self.time_XPATH).send_keys(timee)
        time.sleep(2)

    def clickOnTaskSave(self):
        self.driver.find_element(By.XPATH,self.taskSave_XPATH).click()
        time.sleep(3)

    def isTaskCreated(self):
        l = self.driver.find_elements(By.XPATH,"//div[@class='py-4 ml-4 bg-white mb-4 rounded-lg ng-star-inserted']")
        # boolean = False
        if len(l) >= 1:
            self.List_tasks.append(True)
        else:
            self.List_tasks.append(False)
        #task created or not validating in activity page
        c=self.driver.find_element(By.XPATH, "//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)
        expectedd = "Task created"
        actuall = self.driver.find_element(By.XPATH, "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if expectedd in actuall:
            self.List_tasks.append(True)
        else:
            self.List_tasks.append(False)
        # self.driver.find_element(By.XPATH, self.).click()
        time.sleep(2)
        if False not in self.List_tasks:
            return True
        else:
            return False
