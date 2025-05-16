import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators import CartPageLocators, BasePageLocators
from utils.base_page import BasePage


class CartFunctionalityPage(BasePage):

    def is_element_displayed(self, by, value):
        try:
            return self.driver.find_element(by, value).is_displayed()
        except NoSuchElementException:
            return False

    def get_app_logo_text(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "app_logo").text
        except NoSuchElementException:
            return ""

    def is_cart_icon_visible(self):
        return self.is_element_displayed(By.CLASS_NAME, "shopping_cart_link")

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
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bm-item-list"))
            )
            menu_items = self.driver.find_elements(By.XPATH, "//nav[contains(@class,'bm-item-list')]//a")
            return [self.driver.execute_script("return arguments[0].textContent;", item).strip() for item in menu_items]
        except NoSuchElementException:
            return []

    def click_all_items(self):
        all_items = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
        )
        all_items.click()


    def click_about(self):
        about_link = WebDriverWait(self.driver, 10).until(
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
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(BasePageLocators.RESET_APP_STATE)
        )
        self.driver.execute_script("arguments[0].click();", reset_button)


    def click_logout(self):
        logout_button = self.driver.find_element(*BasePageLocators.LOGOUT)
        self.driver.execute_script("arguments[0].click();", logout_button)


    def is_products_title_visible(self):
        return self.is_element_displayed(By.CLASS_NAME, "title")


    def is_continue_shopping_button_present(self):
        return self.is_element_displayed(By.ID, "continue-shopping")


    def get_product_name(self):
        try:
            return self.driver.find_element(*CartPageLocators.PRODUCT_NAMES).text
        except NoSuchElementException:
            raise AssertionError("Product name not found in cart!")


    def get_product_description(self):
        try:
            return self.driver.find_element(*CartPageLocators.PRODUCT_DESCRIPTION).text.strip()
        except NoSuchElementException:
            raise AssertionError("Product description not found in cart!")


    def get_product_price_in_cart(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [price.text for price in prices]


    def get_qty_header_text(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "cart_quantity_label").text
        except NoSuchElementException:
            return None


    def get_description_header_text(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "cart_desc_label").text
        except NoSuchElementException:
            return None


    def is_remove_button_present(self):
        return self.is_element_displayed(By.CLASS_NAME, "cart_button")


    def click_remove_button(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "cart_button").click()
        except NoSuchElementException:
            raise AssertionError("Remove button not found!")


    def remove_all_items_from_cart(self):
        remove_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Remove']")
        for button in remove_buttons:
            button.click()


    def is_cart_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item")) == 0


    def get_ui_layout_issues(self):
        issues = []
        def is_fully_inside(inner, outer):
            return (
                inner['x'] >= outer['x'] and
                inner['x'] + inner['width'] <= outer['x'] + outer['width'] and
                inner['y'] >= outer['y'] and
                inner['y'] + inner['height'] <= outer['y'] + outer['height']
            )
        try:
            cart_rect = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").rect
            primary_header_rect = self.driver.find_element(By.CLASS_NAME, "primary_header").rect
            if not is_fully_inside(cart_rect, primary_header_rect):
                issues.append("cart_icon_overlap")
        except NoSuchElementException:
            issues.append("cart_icon_overlap")
        try:
            qty_header = self.driver.find_element(*CartPageLocators.QTY_HEADER)
            desc_header = self.driver.find_element(*CartPageLocators.DESCRIPTION_HEADER)
            if qty_header.location['x'] >= desc_header.location['x']:
                issues.append("qty_column_not_left_of_description")
        except NoSuchElementException:
            issues.append("qty_column_not_left_of_description")
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
            checkout_button = self.driver.find_element(By.ID, "checkout")
            container = self.driver.find_element(By.CLASS_NAME, "cart_footer")
            button_y = checkout_button.location['y']
            container_y = container.location['y']
            container_height = container.size['height']
            if not (container_y <= button_y <= container_y + container_height):
                issues.append("checkout_button_issue")
        except NoSuchElementException:
            issues.append("checkout_button_issue")
        return issues


    def go_to_cart(self):
        self.driver.find_element(*CartPageLocators.CART_ICON).click()


    def click_continue_shopping_button(self):
        try:
            self.driver.find_element(By.ID, "continue-shopping").click()
        except NoSuchElementException:
            raise AssertionError("Continue Shopping button not found!")


    def is_on_inventory_page(self):
        return "inventory" in self.driver.current_url


    def is_checkout_button_present(self):
        return self.is_element_displayed(By.ID, "checkout")


    def click_checkout_button(self):
        try:
            self.driver.find_element(By.ID, "checkout").click()
        except NoSuchElementException:
            raise AssertionError("Checkout button not found!")


    def is_on_checkout_page(self):
        return "checkout-step-one" in self.driver.current_url


    def scroll_to_footer(self):
        footer = self.driver.find_element(By.CLASS_NAME, "footer")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)


    def click_footer_social_link(self, platform):
        selectors = {
            "Twitter": "footer a[href*='twitter.com']",
            "Facebook": "footer a[href*='facebook.com']",
            "LinkedIn": "footer a[href*='linkedin.com']"
        }
        selector = selectors.get(platform)
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
