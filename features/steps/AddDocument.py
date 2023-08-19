import time

from behave import *
from selenium.webdriver.common.by import By

from features.pages.AddDocumentPage import AddDocumentPage


@when(u'user clicks on Document option')
def step_impl(context):
    #ADCP=adddocumentpage
    context.ADCP=AddDocumentPage(context.driver)
    context.ADCP.click_document_option()
    # d=context.driver.find_element(By.XPATH,"//a[@id='document']")
    # context.driver.execute_script("arguments[0].click()",d)
    # time.sleep(2)

@when(u'in that page he clicks Add Documents')
def step_impl(context):
    context.ADCP.click_add_documents_button()
    # context.driver.find_element(By.XPATH,"//button[normalize-space()='Add Documents']").click()
    # time.sleep(2)


@when(u'user upload file here')
def step_impl(context):
    context.ADCP.upload_file("C://Users/abzalhussain/Desktop/download.jpeg")
    # context.driver.find_element(By.XPATH,"//input[@id='file-upload - ']").send_keys("C://Users/abzalhussain/Desktop/download.jpeg")
    # time.sleep(5)
@when(u'clicks save')
def step_impl(context):
    context.ADCP.click_save_button()
    # context.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    # time.sleep(3)


@then(u'check wheather the file is uploaded or not')
def step_impl(context):
    assert context.ADCP.check_uploaded_files()
    # l=context.driver.find_elements(By.XPATH,"//div[@class='flex flex-col ng-star-inserted']")
    # if len(l)>=1:
    #     assert True
    # else:
    #     assert False

