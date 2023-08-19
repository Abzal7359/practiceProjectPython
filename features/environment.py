from selenium import webdriver

from features.pages.DashboardPage import DashboardPage

url ="https://bento.uat.propflo.in/auth/sign-in"
browser="e"

def before_all(context):

    if browser=="edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        context.driver = webdriver.Edge(options=options)
    else:
        options=webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach",True)
        context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(url)


def after_all(context):
    context.DP=DashboardPage(context.driver)
    context.DP.clickSignout()
    context.driver.quit()
