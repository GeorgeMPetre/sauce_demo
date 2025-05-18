import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage
from pages.locators.locators import CheckoutOverviewPageLocators, BasePageLocators


class CheckoutOverviewPage(BasePage):

    def is_element_displayed(self, by, value):
        try:
            return self.driver.find_element(by, value).is_displayed()
        except NoSuchElementException:
            return False

    def get_app_logo_text(self):
        return self.driver.find_element(By.CLASS_NAME, "app_logo").text

    def is_cart_icon_visible(self):
        return self.is_element_displayed(By.CLASS_NAME, "shopping_cart_link")

    def go_to_cart(self):
        self.driver.find_element(*CheckoutOverviewPageLocators.CART_ICON).click()

    def is_products_title_visible(self):
        return self.is_element_displayed(By.CLASS_NAME, "title")

    def is_burger_menu_button_visible(self):
        return self.is_element_displayed(By.ID, "react-burger-menu-btn")

    def open_menu(self):
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BasePageLocators.MENU_PANEL)
        )
        menu_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bm-menu-wrap"))
        )
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap"))
        )


    def is_menu_open(self):
        try:
            element = self.driver.find_element(By.CLASS_NAME, "bm-menu-wrap")
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def get_menu_options(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bm-item-list"))
            )
            menu_items = self.driver.find_elements(By.XPATH, "//nav[contains(@class,'bm-item-list')]//a")
            return [self.driver.execute_script("return arguments[0].textContent;", item).strip() for item in menu_items]
        except NoSuchElementException:
            return []

    def click_all_items(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BasePageLocators.ALL_ITEMS)
        ).click()

    def click_about(self):
        about_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(BasePageLocators.ABOUT)
        )
        self.driver.execute_script("arguments[0].click();", about_link)

    def click_about_and_handle_redirect(self):
        self.click_about()
        time.sleep(2)
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[-1])
        return self.driver.current_url


    def click_reset_app_state(self):
        reset_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(BasePageLocators.RESET_APP_STATE)
        )
        self.driver.execute_script("arguments[0].click();", reset_button)

    def click_logout(self):
        logout_button = self.driver.find_element(*BasePageLocators.LOGOUT)
        self.driver.execute_script("arguments[0].click();", logout_button)

    def is_product_present(self, product_name):
        products = self.driver.find_elements(*CheckoutOverviewPageLocators.PRODUCT_NAME)
        return any(product.text.strip() == product_name for product in products)

    def get_product_description(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.PRODUCT_DESCRIPTION).text

    def get_product_price(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.PRODUCT_PRICE).text

    def get_payment_info(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.PAYMENT_INFO).text

    def get_shipping_info(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.SHIPPING_INFO).text

    def get_item_total(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.ITEM_TOTAL).text

    def get_tax(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.TAX).text

    def get_total(self):
        return self.driver.find_element(*CheckoutOverviewPageLocators.TOTAL).text

    def get_qty_header_text(self):
        return self.driver.find_element(By.CLASS_NAME, "cart_quantity_label").text

    def get_description_header_text(self):
        return self.driver.find_element(By.CLASS_NAME, "cart_desc_label").text

    def get_ui_layout_issues(self, username):
        issues = []

        def is_fully_inside(inner, outer):
            return (
                inner['x'] >= outer['x'] and
                inner['x'] + inner['width'] <= outer['x'] + outer['width'] and
                inner['y'] >= outer['y'] and
                inner['y'] + inner['height'] <= outer['y'] + outer['height']
            )

        def is_overlapping(r1, r2):
            return not (
                r1['x'] + r1['width'] <= r2['x'] or
                r1['x'] >= r2['x'] + r2['width'] or
                r1['y'] + r1['height'] <= r2['y'] or
                r1['y'] >= r2['y'] + r2['height']
            )

        try:
            cart_rect = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").rect
            header_rect = self.driver.find_element(By.CLASS_NAME, "primary_header").rect
            if not is_fully_inside(cart_rect, header_rect):
                issues.append("cart_icon_overlap")
        except NoSuchElementException:
            issues.append("cart_icon_overlap")

        if not self.is_burger_menu_button_visible():
            issues.append("burger_menu_missing")
        if not self.is_products_title_visible():
            issues.append("title_not_centered")
        if not self.is_element_displayed(By.CLASS_NAME, "inventory_list"):
            issues.append("inventory_not_visible")

        try:
            for product in self.driver.find_elements(By.CLASS_NAME, "inventory_item"):
                if not all([
                    product.find_element(By.CLASS_NAME, "inventory_item_name").is_displayed(),
                    product.find_element(By.TAG_NAME, "img").is_displayed(),
                    product.find_element(By.CLASS_NAME, "inventory_item_price").is_displayed()
                ]):
                    issues.append("product_element_missing")
                    break
        except NoSuchElementException:
            issues.append("product_element_missing")

        if not self.is_element_displayed(By.CLASS_NAME, "product_sort_container"):
            issues.append("sort_dropdown_issue")

        try:
            finish_button = self.driver.find_element(By.ID, "finish")
            container = self.driver.find_element(By.CLASS_NAME, "cart_footer")
            button_y = finish_button.location['y']
            container_y = container.location['y']
            container_height = container.size['height']
            if not (container_y <= button_y <= container_y + container_height):
                issues.append("checkout_button_issue")
        except NoSuchElementException:
            issues.append("checkout_button_issue")

        if username == "visual_user":
            try:
                cart_rect = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").rect
                header_rect = self.driver.find_element(By.CLASS_NAME, "primary_header").rect
                if not is_fully_inside(cart_rect, header_rect) or is_overlapping(cart_rect, header_rect):
                    issues.append("cart_icon_overlap")
            except NoSuchElementException:
                issues.append("cart_icon_overlap")

        return issues

    def is_finish_button_present(self):
        return self.is_element_displayed(*CheckoutOverviewPageLocators.FINISH_BUTTON)

    def is_cancel_button_present(self):
        return self.is_element_displayed(*CheckoutOverviewPageLocators.CANCEL_BUTTON)

    def click_cancel_button(self):
        self.driver.find_element(*CheckoutOverviewPageLocators.CANCEL_BUTTON).click()

    def click_finish(self):
        self.click(CheckoutOverviewPageLocators.FINISH_BUTTON)

    def is_order_successful(self):
        try:
            return "Thank you for your order!" in self.get_text(CheckoutOverviewPageLocators.ORDER_CONFIRMATION_TEXT)
        except TimeoutException:
            return False

    def is_error_displayed(self):
        return self.is_element_displayed(By.CLASS_NAME, "error-message-container")

    def scroll_to_footer(self):
        try:
            footer = self.driver.find_element(By.CLASS_NAME, "footer")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        except NoSuchElementException:
            pass

    def click_footer_social_link(self, platform):
        selectors = {
            "Twitter": "footer a[href*='twitter.com']",
            "Facebook": "footer a[href*='facebook.com']",
            "LinkedIn": "footer a[href*='linkedin.com']"
        }
        selector = selectors.get(platform)
        if selector:
            self.driver.find_element(By.CSS_SELECTOR, selector).click()

    def is_footer_social_link_present(self, platform):
        selectors = {
            "Twitter": "footer a[href*='twitter.com']",
            "Facebook": "footer a[href*='facebook.com']",
            "LinkedIn": "footer a[href*='linkedin.com']"
        }
        selector = selectors.get(platform)
        return self.is_element_displayed(By.CSS_SELECTOR, selector)

    def get_footer_legal_text(self):
        try:
            footer = self.driver.find_element(By.CLASS_NAME, "footer_copy")
            return footer.text.strip()
        except NoSuchElementException:
            return ""
