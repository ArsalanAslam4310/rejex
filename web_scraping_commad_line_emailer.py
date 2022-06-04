from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://login.yahoo.com/')
email_field = browser.find_element_by_id('login-username')
email_field.send_keys('zeeshan04956@yahoo.com')
next_button = browser.find_element_by_id('login-signin')
next_button.click()
sleep(2)
password_field = browser.find_element_by_id('login-passwd')
password_field.send_keys('Zee@03406003774')
next_button = browser.find_element_by_id('login-signin')
next_button.click()
browser.get('https://mail.yahoo.com/')
compose_button = browser.find_element_by_css_selector(
    'a[data-test-id="compose-button"]')
compose_button.click()
msgto_field = browser.find_element_by_id('message-to-field')
msgto_field.send_keys('zeeshan04956@gmail.com')
subject_field = browser.find_element_by_css_selector(
    'input[data-test-id="compose-subject"]')
subject_field.send_keys('Automate Email With PYTHON')
body = browser.find_element_by_css_selector('div[data-test-id="rte"]')
body.send_keys('Write a program that takes an email address and string of text on the command line and then, using selenium, logs in to your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.')
send_button = browser.find_element_by_css_selector(
    'button[data-test-id="compose-send-button"]')
send_button.click()
