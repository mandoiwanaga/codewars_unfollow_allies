def sign_in(email_address, password, browser):
    #insert email_address
    xpath_email = '//*[@id="user_email"]'
    find_xpath_email = browser.find_element_by_xpath(xpath_email)
    find_xpath_email.send_keys(email_address)
    
    #insert password
    xpath_password = '//*[@id="user_password"]'
    find_xpath_password = browser.find_element_by_xpath(xpath_password)
    find_xpath_password.send_keys(password)
    
    #submit to login
    xpath_login = '//*[@id="new_user"]/button'
    login = browser.find_element_by_xpath(xpath_login)
    login.submit()