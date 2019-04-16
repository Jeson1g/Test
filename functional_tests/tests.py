from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from django.test import LiveServerTestCase

# 最大等待时长
MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            if time.time() - start_time > MAX_WAIT:
                raise TimeoutError
            else:
                try:
                    table = self.browser.find_element_by_id('id_list_table')
                    rows = table.find_elements_by_tag_name('tr')
                    if row_text in [row.text for row in rows]:
                        return
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)

    # def test_start_and_retrieve(self):
    #     self.browser.get(self.live_server_url)
    #
    #     # 应用邀请她输入一个待办事项
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Use peacock feathers to make a fly')
    #     # 她按回车键后，页面更新了
    #     # 待办事项表格中显示了“1: Buy peacock feathers”
    #     inputbox.send_keys(Keys.ENTER)
    #
    #     self.wait_for_row_in_list_table('1: Use peacock feathers to make a fly')
    #
    # def test_multiple_users_can_start_lists_at_different_urls(self):
    #
    #     # 伊迪丝新建一个待办事项清单
    #     self.browser.get(self.live_server_url)
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Buy peacock feathers')
    #     inputbox.send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Buy peacock feathers')
    #     # 她注意到清单有个唯一的URL
    #     edith_list_url = self.browser.current_url
    #     self.assertRegex(edith_list_url, '/lists/.+')
    #
    #     # Use new browser
    #     self.browser.quit()
    #     self.browser = webdriver.Firefox()
    #     self.browser.get(self.live_server_url)
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Buy milk')
    #     inputbox.send_keys(Keys.ENTER)
    #
    #     self.wait_for_row_in_list_table('1: Buy milk')

    def test_layout_and_styling(self):

        self.browser.get(self.live_server_url)

        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: testing')

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

