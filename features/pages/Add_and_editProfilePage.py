import time

from selenium.webdriver.common.by import By


class AddAndEditProfilePage:
    def __init__(self,driver):
        self.driver=driver

    profile_XPATH="//a[@id='profile']"
    EditProfile_XPATH="(//button[@class='primary-button h-9 mr-1.5 ng-star-inserted'])[1]"
#----------------------------------------------------------------------------------------------
    UPLOAD_PHOTO_INPUT = (By.XPATH, "//input[@type='file']")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='button'][normalize-space()='Save'])[1]")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")
    DATE_OF_BIRTH_INPUT = (By.XPATH, "//input[@type='date']")
    GENDER_MALE_RADIO = (By.XPATH, "//input[@value='MALE']")

    #-----------------------------------------------------------------------
    secondPhonenum_XPATH="(//input[@id='phone-number'])[2]"
    secondmail_XPATH="(//input[@placeholder='Email Address'])[1]"
    AddanotherPhoneNum_XPATH="(//p[@for='status'])[1]"
    thirdPhonenum_XPATH="(//input[@id='phone-number'])[3]"
    AddanotherMail_XPATH="(//a[normalize-space()='Add Email'])[1]"
    thirdMail_XPATH="(//input[@placeholder='Email Address'])[2]"
    Address_XPATH="//input[@formcontrolname='address']"
    linkedinURL_XPATH="//input[@formcontrolname='linkdinUrl']"
    facebookURL_XPATH="//input[@formcontrolname='facebookUrl']"
    instagramURL_XPATH="//input[@formcontrolname='instagramUrl']"
    twitterURL_XPATH="//input[@formcontrolname='twitterUrl']"
#---------------------------------------------------------------------------
    ADD_COMPANY_LINK = (By.XPATH, "(//a[normalize-space()='Add Company'])[1]")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Company Name']")
    DESIGNATION_INPUT = (By.XPATH, "(//input[@placeholder='Designation'])[1]")
    START_DATE_INPUT = (By.XPATH, "(//input[@type='date'])[2]")
    END_DATE_INPUT = (By.XPATH, "(//input[@type='date'])[3]")
    COMPANY_WEBSITE_INPUT = (By.XPATH, "(//input[@placeholder='Company Website'])[1]")
    LOCATION_INPUT = (By.XPATH, "(//input[@placeholder='Location'])[1]")
    SALARY_INPUT = (By.XPATH, "(//input[@placeholder='Salary'])[1]")
#------------------------------------------------------------------------------------------------

    ADD_SCHOOL_LINK = (By.XPATH, "(//a[normalize-space()='Add School'])[1]")
    SCHOOL_NAME_INPUT = (By.XPATH, "(//input[@placeholder='School Name'])[1]")
    COURSE_NAME_INPUT = (By.XPATH, "(//input[@placeholder='Course Name'])[1]")
    SSTART_DATE_INPUT = (By.XPATH, "(//input[@type='date'])[4]")
    EEND_DATE_INPUT = (By.XPATH, "(//input[@type='date'])[5]")
    LLOCATION_INPUT = (By.XPATH, "(//input[@placeholder='Location'])[2]")

    #--------------------------------------------------------------------------------------------------------------------------

    def clikcOnProfile(self):
        c = self.driver.find_element(By.XPATH, self.profile_XPATH)
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)

    def clickOnEditProfile(self):
        self.driver.find_element(By.XPATH,self.EditProfile_XPATH).click()
        time.sleep(2)

    def enterBasicDetails(self,FIP,FN,LN,DOB):
        #FN=firstname LN=lastname
        #------------------------------------------------------------------------------
        # self.driver.find_element(*self.UPLOAD_PHOTO_INPUT).send_keys(FIP)
        # time.sleep(2)
        # self.driver.find_element(*self.SAVE_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(FN)
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(LN)
        self.driver.find_element(*self.DATE_OF_BIRTH_INPUT).send_keys(DOB)
        z =self.driver.find_element(By.XPATH, "(//div[@class='absolute w-[100%]'])[1]//button")
        self.driver.execute_script("arguments[0].click()", z)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Self'])[1]").click()
        self.driver.execute_script("arguments[0].click()", z)
        self.driver.find_element(*self.GENDER_MALE_RADIO).click()

    def enterContactDetials(self,SP,SM,TP,TM,ADDRESS,LURL,FURL,IURL,TURL):
        #sp=secondphonenum,SM=secondmail,LURL=linkedinurl,TP=thirdphonenum
        self.driver.find_element(By.XPATH, self.secondPhonenum_XPATH).send_keys(SP)
        self.driver.find_element(By.XPATH, self.secondmail_XPATH).send_keys(SM)
        self.driver.find_element(By.XPATH, self.AddanotherPhoneNum_XPATH).click()
        self.driver.find_element(By.XPATH, self.thirdPhonenum_XPATH).send_keys(TP)
        self.driver.find_element(By.XPATH, self.AddanotherMail_XPATH).click()
        self.driver.find_element(By.XPATH, self.thirdMail_XPATH).send_keys(TM)
        self.driver.find_element(By.XPATH, self.Address_XPATH).send_keys(ADDRESS)
        self.driver.find_element(By.XPATH, self.linkedinURL_XPATH).send_keys(LURL)
        self.driver.find_element(By.XPATH, self.facebookURL_XPATH).send_keys(FURL)
        self.driver.find_element(By.XPATH, self.instagramURL_XPATH).send_keys(IURL)
        self.driver.find_element(By.XPATH, self.twitterURL_XPATH).send_keys(TURL)
        time.sleep(2)

    def enterProfessionalDetails(self,name,desig,sd,ed,compwebsite,loc,salary):
        self.driver.find_element(*self.ADD_COMPANY_LINK).click()
        self.driver.find_element(*self.COMPANY_NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.DESIGNATION_INPUT).send_keys(desig)
        self.driver.find_element(*self.START_DATE_INPUT).send_keys(sd)
        self.driver.find_element(*self.END_DATE_INPUT).send_keys(ed)
        self.driver.find_element(*self.COMPANY_WEBSITE_INPUT).send_keys(compwebsite)
        self.driver.find_element(*self.LOCATION_INPUT).send_keys(loc)
        self.driver.find_element(*self.SALARY_INPUT).send_keys(salary)
        time.sleep(2)

    def enterEducationalDetails(self,name,course,sd,ed,loc):
        #sd=startdate,ed=enddate,loc=loaation
        self.driver.find_element(*self.ADD_SCHOOL_LINK).click()
        self.driver.find_element(*self.SCHOOL_NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.COURSE_NAME_INPUT).send_keys(course)
        self.driver.find_element(*self.SSTART_DATE_INPUT).send_keys(sd)
        self.driver.find_element(*self.EEND_DATE_INPUT).send_keys(ed)
        self.driver.find_element(*self.LLOCATION_INPUT).send_keys(loc)
        time.sleep(3)