import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.locators import BasePageLocators, ProductsPageLocators
from utils.base_page import BasePage


class ProductBrowsingPage(BasePage):

    def get_app_logo_text(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "app_logo").text
        except NoSuchElementException:
            return ""

    def is_cart_icon_visible(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
        except NoSuchElementException:
            return False

    def is_products_title_visible(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "title").is_displayed()
        except NoSuchElementException:
            return False

    def is_sort_dropdown_visible(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
        except NoSuchElementException:
            return False

    def sort_by_name_az(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, ".//option[@value='az']").click()

    def sort_by_name_za(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, ".//option[@value='za']").click()

    def sort_by_price_low_to_high(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, ".//option[@value='lohi']").click()

    def sort_by_price_high_to_low(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, ".//option[@value='hilo']").click()

    def is_sorting_broken(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            if "Sorting is broken!" in alert.text:
                alert.accept()
                return True
        except NoSuchElementException:
            return False
        return False


    def is_burger_menu_button_visible(self):
        try:
            return self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        except NoSuchElementException:
            return False


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
                EC.visibility_of_all_elements_located((By.XPATH, "//nav[contains(@class,'bm-item-list')]//a"))
            )
            menu_items = self.driver.find_elements(By.XPATH, "//nav[contains(@class,'bm-item-list')]//a")
            return [self.driver.execute_script("return arguments[0].innerText;", item).strip() for item in menu_items]
        except NoSuchElementException as e:
            print(f"Menu option error: {e}")
            self.driver.save_screenshot("menu_debug.png")
            return []


    def click_about(self):
        about_link = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(BasePageLocators.ABOUT))
        self.driver.execute_script("arguments[0].click();", about_link)

    def click_about_and_handle_redirect(self):
        self.click_about()
        time.sleep(3)
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[-1])
        return self.driver.current_url

    def click_logout(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BasePageLocators.LOGOUT))

    def click_reset_app_state(self):
        reset_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(BasePageLocators.RESET_APP_STATE))
        self.driver.execute_script("arguments[0].click();", reset_btn)


    def get_total_products_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "inventory_item"))

    def add_all_products_to_cart(self):
        for button in self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']"):
            button.click()

    def get_product_names(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
        )
        return [e.text for e in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def get_product_prices(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
        )
        prices = []
        for e in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price"):
            try:
                prices.append(float(e.text.strip().replace("$", "")))
            except ValueError:
                continue
        return prices

    def are_buttons_functional(self):
        try:
            buttons = self.driver.find_elements(By.XPATH,
                                                "//button[contains(text(), 'Add to cart') or contains(text(), 'Remove')]")
            if not buttons:
                return False
            for i in range(len(buttons)):
                current_buttons = self.driver.find_elements(By.XPATH,
                                                            "//button[contains(text(), 'Add to cart') or contains(text(), 'Remove')]")
                if i >= len(current_buttons):
                    return False
                button = current_buttons[i]
                original_text = button.text.strip()
                button.click()
                try:
                    WebDriverWait(self.driver, 3).until(
                        lambda d: d.find_elements(By.XPATH,
                                                  "//button[contains(text(), 'Add to cart') or contains(text(), 'Remove')]")[
                                      i].text.strip() != original_text
                    )
                except TimeoutException:
                    return False
                updated_text = self.driver.find_elements(By.XPATH,
                                                         "//button[contains(text(), 'Add to cart') or contains(text(), 'Remove')]")[
                    i].text.strip()
                if (original_text == "Add to cart" and updated_text != "Remove") or \
                        (original_text == "Remove" and updated_text != "Add to cart"):
                    return False
            return True
        except NoSuchElementException:
            return False


    def click_first_product(self):
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()

    def get_product_titles_from_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
        )
        return [elem.text for elem in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def get_product_title_from_detail_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))
        )
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text

    def add_first_product_to_cart(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
            )
            first = self.driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
            first.find_element(By.TAG_NAME, "button").click()
        except TimeoutException:
            raise Exception("Product list did not load in time.")

    def get_first_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text


    def get_ui_layout_issues(self):
        issues = []
        tolerance = 5
        try:
            cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            header = self.driver.find_element(By.CLASS_NAME, "primary_header")
            cart_rect = cart.rect
            header_rect = header.rect
            cart_top = cart_rect['y']
            cart_bottom = cart_rect['y'] + cart_rect['height']
            header_top = header_rect['y']
            header_bottom = header_rect['y'] + header_rect['height']
            vertically_aligned = (
                    cart_top >= header_top - tolerance and
                    cart_bottom <= header_bottom + tolerance
            )
            cart_left = cart_rect['x']
            cart_right = cart_rect['x'] + cart_rect['width']
            header_left = header_rect['x']
            header_right = header_rect['x'] + header_rect['width']
            horizontally_aligned = (
                    cart_left >= header_left - tolerance and
                    cart_right <= header_right + tolerance
            )
            if not (vertically_aligned and horizontally_aligned):
                issues.append("cart_overlap")
        except NoSuchElementException as e:
            print("Cart/Header check failed:", e)
            issues.append("cart_overlap")
        try:
            if not self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed():
                issues.append("burger_menu_missing")
        except NoSuchElementException:
            issues.append("burger_menu_missing")
        try:
            if not self.driver.find_element(By.CLASS_NAME, "title").is_displayed():
                issues.append("title_not_centered")
        except NoSuchElementException:
            issues.append("title_not_centered")
        try:
            if not self.driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed():
                issues.append("inventory_not_visible")
        except NoSuchElementException:
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
        try:
            if not self.driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed():
                issues.append("sort_dropdown_issue")
        except NoSuchElementException:
            issues.append("sort_dropdown_issue")
        return issues


    def go_to_cart(self):
        self.driver.find_element(*ProductsPageLocators.CART_ICON).click()

    def remove_all_items_from_cart(self):
        for button in self.driver.find_elements(By.XPATH, "//button[text()='Remove']"):
            button.click()

    def get_all_product_info(self):
        product_info_list = []
        for product in self.driver.find_elements(By.CLASS_NAME, "inventory_item"):
            try:
                name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
                img = product.find_element(By.CLASS_NAME, "inventory_item_img").find_element(By.TAG_NAME, "img")
                product_info_list.append({
                    "name": name,
                    "img_src": img.get_attribute("src"),
                    "alt": img.get_attribute("alt")
                })
            except NoSuchElementException as e:
                print(f"[ERROR] Could not extract product info: {e}")
                continue
        return product_info_list


    def scroll_to_footer(self):
        footer = self.driver.find_element(By.CLASS_NAME, "footer")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)

    def is_footer_social_link_present(self, platform):
        selectors = {
            "Twitter": "footer a[href*='twitter.com']",
            "Facebook": "footer a[href*='facebook.com']",
            "LinkedIn": "footer a[href*='linkedin.com']"
        }
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, selectors[platform])
            return element.is_displayed()
        except Exception as e:
            print(f"[DEBUG] {platform} link not found: {e}")
            return False

    def click_footer_social_link(self, platform):
        selectors = {
            "Twitter": "footer a[href*='twitter.com']",
            "Facebook": "footer a[href*='facebook.com']",
            "LinkedIn": "footer a[href*='linkedin.com']"
        }
        self.driver.find_element(By.CSS_SELECTOR, selectors[platform]).click()

    def get_footer_legal_text(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "footer_copy").text.strip()
        except NoSuchElementException:
            return ""

