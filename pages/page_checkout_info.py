import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage
from pages.locators.locators import CheckoutPageLocators, BasePageLocators


class CheckoutProcessPage(BasePage):

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
            WebDriverWait(self.driver, 10).until(
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

    def is_error_message_displayed(self):
        return self.is_element_displayed(*CheckoutPageLocators.ERROR_MESSAGE)

    def go_to_cart(self):
        self.driver.find_element(*CheckoutPageLocators.CART_ICON).click()

    def enter_first_name(self, first_name):
        self.enter_text(CheckoutPageLocators.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(CheckoutPageLocators.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.enter_text(CheckoutPageLocators.POSTAL_CODE_INPUT, postal_code)

    def complete_checkout(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def click_continue(self):
        self.driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()

    def cancel_checkout(self):
        self.click(CheckoutPageLocators.CANCEL_BUTTON)

    def is_first_name_field_present(self):
        return self.is_element_displayed(*CheckoutPageLocators.FIRST_NAME)

    def is_last_name_field_present(self):
        return self.is_element_displayed(*CheckoutPageLocators.LAST_NAME)

    def is_postal_code_field_present(self):
        return self.is_element_displayed(*CheckoutPageLocators.POSTAL_CODE)

    def is_cancel_button_present(self):
        return self.is_element_displayed(By.ID, "cancel")

    def is_continue_button_present(self):
        return self.is_element_displayed(By.ID, "continue")

    def is_checkout_title_present(self):
        return self.is_element_displayed(*CheckoutPageLocators.PAGE_TITLE)

    def is_products_title_visible(self):
        return self.is_element_displayed(By.CLASS_NAME, "title")

    def get_ui_layout_issues(self):
        issues = []

        def is_fully_inside(inner, outer):
            return (
                inner['x'] >= outer['x'] and
                inner['x'] + inner['width'] <= outer['x'] + outer['width'] and
                inner['y'] >= outer['y'] and
                inner['y'] + inner['height'] <= outer['y'] + outer['height']
            )

        if "checkout-step-one" not in self.driver.current_url:
            print(f"Warning: get_ui_layout_issues() called outside Checkout Info Page. URL: {self.driver.current_url}")

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

        for key, field_id in [
            ("first_name_field_misaligned", "first-name"),
            ("last_name_field_misaligned", "last-name"),
            ("postal_code_field_misaligned", "postal-code")
        ]:
            if not self.is_element_displayed(By.ID, field_id):
                issues.append(key)

        try:
            continue_btn = self.driver.find_element(By.ID, "continue")
            cancel_btn = self.driver.find_element(By.ID, "cancel")
            if abs(continue_btn.location['y'] - cancel_btn.location['y']) > 5:
                issues.append("continue_button_misaligned")
                issues.append("cancel_button_misaligned")
        except NoSuchElementException:
            issues.append("continue_button_misaligned")
            issues.append("cancel_button_misaligned")

        try:
            footer = self.driver.find_element(By.CLASS_NAME, "footer")
            window_height = self.driver.execute_script("return window.innerHeight")
            footer_bottom = footer.location['y'] + footer.size['height']
            if footer_bottom < window_height - 50:
                issues.append("footer_misaligned")
        except NoSuchElementException:
            issues.append("footer_misaligned")

        return issues

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
