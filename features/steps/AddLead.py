import time

from behave import *
from selenium.webdriver.common.by import By

from features.pages.DashboardPage import DashboardPage
from features.pages.LeadsPage import LeadsPage
from features.pages.LoginPage import LoginPage
from features.pages.NotesPage import NotesPage


@given(u'user navigates to login page')
def step_impl(context):
    pass


@when(u'user enters login details mail as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    #LOP=login page
    context.LOP=LoginPage(context.driver)
    context.LOP.enter_mail_and_password(email,password)


@when(u'click login button')
def step_impl(context):
    #DP = dashboard page
    context.DP=context.LOP.clickSignIn()


@when(u'click on sales and inside that clicks leads')
def step_impl(context):
    #LP=LeadsPage
    context.LP=context.DP.clickOnLeads()



@when(u'click Add Lead option')
def step_impl(context):
    context.LP.clickAddLead()

@when(u'enters mandatory fields in add leads page')
def step_impl(context):
    for row in context.table:
        global name
        global mail
        name=row["firstname"]
        mail=row["email"]
        context.LP.enter_Mandatory_Fields(row["firstname"],row["lastname"],row["email"],row["mobile"],row["description"])



@when(u'click on save button')
def step_impl(context):
    context.LP.clickAddLeadSave()


@then(u'the lead details should added successfully')
def step_impl(context):

    assert context.LP.isLeadCreated(name,mail)


#tasks features

@when(u'click on tasks bar')
def step_impl(context):
    #TP=tasks page
    context.LP=LeadsPage(context.driver)
    context.TP=context.LP.clickOnTasksPage()

    time.sleep(2)




@when(u'click on create task')
def step_impl(context):
    context.TP.clickOnCreateTask()



@when(u'write task and set task details')
def step_impl(context):
    for r in context.table:
        context.TP.enterTaskDetails(r["textbox"], r["time"])




@when(u'click task save')
def step_impl(context):
    context.TP.clickOnTaskSave()


@then(u'ckeck task is created or not')
def step_impl(context):

    assert context.TP.isTaskCreated()

    time.sleep(2)


#notes page feature



@when(u'clickon Notes taskbar')
def step_impl(context):
    context.NP=NotesPage(context.driver)
    context.NP.click_onNotes()


@when(u'click on create notes')
def step_impl(context):
    context.NP.click_On_CreateNotes()


@when(u'write description in notes and save')
def step_impl(context):
    for i in context.table:
        context.NP.enter_note_in_box(i["notesDescription"])

@then(u'check the note is created or not')
def step_impl(context):
    context.NP = NotesPage(context.driver)
    assert context.NP.isNoteCreate()
    # context.DP=DashboardPage(context.driver)
    # context.DP.clickSignout()

