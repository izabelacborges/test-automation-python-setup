from helper import wait_until

class BaseElement():

    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        print "Typing: '%s' - '%s' => '%s'" % (locator[0], locator[1], value)
        try:
            for letter in value:
                wait_until.presence_of_element_located(self.driver, locator).send_keys(letter)
        except:
            self.driver.quit()
            raise

    def click(self, locator):
        print "Clicking: '%s' - '%s'" % (locator[0], locator[1])
        try:
            wait_until.element_to_be_clickable(self.driver, locator).click()
        except:
            self.driver.quit()
            raise

    def assert_this(self, locator, message):
        print "Asserting: '%s' on %s - %s" % (message, locator[0], locator[1])
        try:
            return wait_until.presence_of_element_located(self.driver, locator)
        except:
            self.driver.quit()
            raise

    def get_element(self, locator):
        print "Getting: '%s' - '%s' " % (locator[0], locator[1])
        try:
            return wait_until.visibility_of_element_located(self.driver, locator)
        except:
            self.driver.quit()
            raise
