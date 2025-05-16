import time
import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants.products_constants import EXPECTED_IMAGES
from pages.locators.locators import BasePageLocators, CartPageLocators, ProductsPageLocators
from pages.page_cart import CartFunctionalityPage
from pages.page_products import ProductBrowsingPage
from utils.data_loader import load_active_users_for_full_tests, load_performance_valid_users


# ------------------ HEADER COMPONENTS TESTS ------------------

# Xray: TEST-04
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_page_primary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    soft_assert.assert_equal(product_page.get_app_logo_text(), "Swag Labs", "Expected: Swag Labs")
    soft_assert.assert_true(product_page.is_cart_icon_visible(),
                            f"'{username}'Expected: product_page.is_cart_icon_visible() to be True")
    soft_assert.assert_true(product_page.is_burger_menu_button_visible(),
                            f"'{username}'Expected: product_page.is_burger_menu_button_visible() to be True")



# Xray: TEST-05
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_page_secondary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    soft_assert.assert_true(product_page.is_products_title_visible(),
                            f"'{username}'Expected: product_page.is_products_title_visible() to be True")
    soft_assert.assert_true(product_page.is_sort_dropdown_visible(),
                            f"'{username}'Expected: product_page.is_sort_dropdown_visible() to be True")




# ------------------ BURGER MENU FUNCTIONALITY TESTS ------------------

# Xray: TEST-06
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_menu_open(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.open_menu()
    soft_assert.assert_true(product_page.is_menu_open(), f"'{username}'Expected: product_page.is_menu_open() to be True")
    expected_menu_options = BasePageLocators.EXPECTED_MENU_OPTIONS
    actual_menu_options = product_page.get_menu_options()
    soft_assert.assert_equal(sorted(actual_menu_options), sorted(expected_menu_options),
                             f"'{username}'Expected: {sorted(expected_menu_options)}")




# Xray: TEST-07
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_logout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.open_menu()
    product_page.click_logout()
    soft_assert.assert_true("www.saucedemo.com" in driver.current_url, f"'{username}'Expected: 'www.saucedemo.com' in driver.current_url to be True")




# Xray: TEST-08
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_logout_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.open_menu()
    start_time = time.time()
    product_page.click_logout()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))
    end_time = time.time()
    logout_time = end_time - start_time
    soft_assert.assert_true(logout_time < 2, f"'{username}'Expected: logout_time < 2")
    soft_assert.assert_true("www.saucedemo.com" in driver.current_url,
                            f"'{username}'Expected: 'www.saucedemo.com' in driver.current_url to be True")




# Xray: TEST-09
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_navigation_to_about(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.open_menu()
    url = product_page.click_about_and_handle_redirect()
    soft_assert.assert_true(
        "saucelabs.com" in url,
        f"'{username}'Expected: 'saucelabs.com' in driver.current_url to be True"
    )
    if len(driver.window_handles) > 1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



# Xray: TEST-10
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_reset_app_state_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.open_menu()
    start_time = time.time()
    product_page.click_reset_app_state()
    end_time = time.time()
    reset_time = end_time - start_time
    soft_assert.assert_true(reset_time < 2, f"'{username}'Expected: reset_time < 2")




# Xray: TEST-11
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_reset_app_state_cart_badge_disappearance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.open_menu()
    product_page.click_reset_app_state()
    cart_badge_gone = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(CartPageLocators.CART_BADGE))
    soft_assert.assert_true(cart_badge_gone, f"'{username}'Expected: cart_badge_gone to be True")



# Xray: TEST-12
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_reset_app_state_remove_button_disappearance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.open_menu()
    product_page.click_reset_app_state()
    try:
        remove_button_gone = WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(BasePageLocators.REMOVE_BUTTONS)
        )
    except TimeoutException:
        remove_button_gone = False
    expected_message = f"'{username}'Expected: Remove button to disappear after resetting app state"
    soft_assert.assert_true(remove_button_gone, expected_message)



# Xray: TEST-13
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_product_titles_visibility(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_titles = product_page.get_product_titles_from_list()
    expected_titles = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]
    soft_assert.assert_equal(sorted(product_titles), sorted(expected_titles), f"'{username}'Expected: {sorted(expected_titles)}")




# Xray: TEST-14
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_product_detail_navigation(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_name = product_page.get_first_product_name()
    product_page.click_first_product()
    WebDriverWait(driver, 5).until(EC.url_contains("inventory-item.html"))
    product_title_on_detail = product_page.get_product_title_from_detail_page()
    soft_assert.assert_true(
        "inventory-item.html" in driver.current_url,
        f"Expected: 'inventory-item.html' in driver.current_url to be True for '{username}'"
    )
    if username == "problem_user":
        soft_assert.assert_info(
            product_title_on_detail != product_name,
            f"Known issue for '{username}': Expected mismatched product title — got '{product_title_on_detail}', expected '{product_name}'"
        )
    else:
        soft_assert.assert_equal(
            product_title_on_detail,
            product_name,
            f"Expected: product title '{product_title_on_detail}' to equal '{product_name}' for user '{username}'"
        )




# Xray: TEST-15
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_expected_images_per_product(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    products = product_page.get_all_product_info()
    for product in products:
        name = product["name"]
        img_src = product["img_src"]
        expected_img_path = EXPECTED_IMAGES.get(name)
        if expected_img_path:
            if not img_src.endswith(expected_img_path):
                message = (
                    f"Image mismatch for product '{name}' — Expected: '{expected_img_path}', Got: '{img_src}'"
                )
                if username in ["problem_user", "visual_user"]:
                    soft_assert.assert_info(True, f"[{username}] Known defect: {message}")
                else:
                    soft_assert.assert_true(False, message)
            else:
                soft_assert.assert_true(True, f"'{username}'Image for '{name}' matches expected URL")
        else:
            soft_assert.assert_warn(
                False,
                f"Unexpected product '{name}' not found in EXPECTED_IMAGES mapping"
            )




# Xray: TEST-16
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_ui_layout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    layout_issues = product_page.get_ui_layout_issues()
    def handle_assert(issue_key, message):
        if issue_key in layout_issues:
            if username == "visual_user" and issue_key == "cart_overlap":
                soft_assert.assert_info(
                    True,
                    f"'{username}' Known layout defect: '{issue_key}' is present in layout_issues (expected for this user)"
                )

            else:
                soft_assert.assert_true(False, f"{issue_key} found in layout_issues — {message}")
        else:
            soft_assert.assert_true(True, message)
    handle_assert("cart_overlap", f"'{username}'Expected: 'cart_overlap' not in layout_issues")
    handle_assert("burger_menu_missing", f"'{username}'Expected: 'burger_menu_missing' not in layout_issues")
    handle_assert("title_not_centered", f"'{username}'Expected: 'title_not_centered' not in layout_issues")
    handle_assert("inventory_not_visible", f"'{username}'Expected: 'inventory_not_visible' not in layout_issues")
    handle_assert("sort_dropdown_issue", f"'{username}'Expected: 'sort_dropdown_issue' not in layout_issues")





# Xray: TEST-17
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_add_remove_buttons_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    buttons_working = product_page.are_buttons_functional()
    if username in ["problem_user", "error_user"]:
        if not buttons_working:
            soft_assert.assert_info(f"Expected: buttons to be broken for user '{username}'")
        else:
            soft_assert.assert_info(f"'UNEXPECTED: buttons are functional for user '{username}'")
    else:
        soft_assert.assert_true(
            buttons_working,
            f"Expected: functional add/remove buttons for user '{username}'"
        )




# Xray: TEST-18
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_add_all_to_cart(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    total_products = product_page.get_total_products_count()
    product_page.add_all_products_to_cart()
    try:
        cart_badge = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProductsPageLocators.CART_BADGE)
        )
        actual_count = int(cart_badge.text)
    except (TimeoutException, NoSuchElementException):
        actual_count = 0
    except ValueError:
        actual_count = -1
    if username in ["problem_user", "error_user"]:
        soft_assert.assert_info(
            actual_count != total_products,
            f"'{username}'Expected: not all products added for user '{username}' due to broken buttons"
        )
    else:
        soft_assert.assert_equal(
            actual_count,
            total_products,
            f"'{username}'Expected: {total_products} products in cart for user '{username}'."
        )




# Xray: TEST-19
@pytest.mark.products
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_navigation_to_cart_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    start_time = time.time()
    product_page.go_to_cart()
    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))
    end_time = time.time()
    cart_transition_time = end_time - start_time
    soft_assert.assert_true("cart.html" in driver.current_url, f"'{username}'Expected: 'cart.html' in driver.current_url to be True")
    soft_assert.assert_true(cart_transition_time < 2, f"'{username}'Expected: cart_transition_time < 2")




# Xray: TEST-20
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_add_and_remove_from_cart(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    cart_badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProductsPageLocators.CART_BADGE))
    soft_assert.assert_equal(cart_badge.text, "1", "Expected: 1")
    product_page.go_to_cart()
    WebDriverWait(driver, 5).until(
        EC.url_contains("cart.html"))
    cart_page = CartFunctionalityPage(driver)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(CartPageLocators.CART_ITEMS))
    soft_assert.assert_false(cart_page.is_cart_empty(), f"'{username}'Expected: cart_page.is_cart_empty() to be False")
    cart_page.click_remove_button()
    cart_badge_gone = WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(ProductsPageLocators.CART_BADGE))
    soft_assert.assert_true(cart_badge_gone, f"'{username}'Expected: cart_badge_gone to be True")
    soft_assert.assert_true(cart_page.is_cart_empty(), f"'{username}'Expected: cart_page.is_cart_empty() to be True")




# Xray: TEST-21
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_sort_dropdown_name_az_selection(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    expects_sorting_broken = username in ["problem_user", "error_user"]
    try:
        try:
            product_page.sort_by_name_az()
        except NoSuchElementException:
            if username == "problem_user":
                soft_assert.assert_info(
                    True,
                    f"'{username}': Known defect – Sorting dropdown missing."
                )
                return
            else:
                raise
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        soft_assert.assert_true(
            False,
            f"'{username}': Unexpected sorting alert appeared during A-Z: '{alert_text}'."
        )
        return
    except TimeoutException:
        if username == "error_user":
            soft_assert.assert_info(
                False,
                f"'{username}': Alert not shown during A-Z because it's default and broken sorting was never triggered. Known limitation."
            )
    names = product_page.get_product_names()
    expected = sorted(names)
    if expects_sorting_broken:
        soft_assert.assert_info(
            names != expected,
            f"'{username}': Expected sorting to be broken (known defect)."
        )
    else:
        soft_assert.assert_equal(
            names,
            expected,
            f"'{username}': Expected products to be sorted A-Z correctly."
        )




# Xray: TEST-22
@pytest.mark.products
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_performance_valid_users())
def test_products_sort_name_az_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    start_time = time.time()
    product_page.sort_by_name_za()
    product_page.sort_by_name_az()
    end_time = time.time()
    sorting_time = end_time - start_time
    if username == "performance_glitch_user":
        soft_assert.assert_info(
            sorting_time > 10,
            f"'{username}' Expected delay met — sorting took {sorting_time:.2f}s"
        )
    else:
        soft_assert.assert_true(
            sorting_time < 2,
            f"'{username}' Sorting duration: {sorting_time:.2f}s"
        )



# Xray: TEST-23
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_sort_dropdown_name_za_selection(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    expects_sorting_broken = username in ["problem_user", "error_user"]
    expects_popup_alert = username == "error_user"
    try:
        try:
            product_page.sort_by_name_za()
        except NoSuchElementException:
            if username == "problem_user":
                soft_assert.assert_info(
                    True,
                    f"'{username}': Known defect - Sorting dropdown missing."
                )
                return
            else:
                raise
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        if expects_popup_alert:
            soft_assert.assert_info(
                True,
                f"'{username}': Expected sorting alert: '{alert_text}'."
            )
        else:
            soft_assert.assert_true(
                False,
                f"'{username}': Unexpected sorting alert appeared: '{alert_text}'."
            )
        return
    except TimeoutException:
        if expects_popup_alert:
            soft_assert.assert_info(
                False,
                f"'{username}': Expected sorting alert, but none appeared."
            )
            return
    names = product_page.get_product_names()
    expected = sorted(names, reverse=True)
    if expects_sorting_broken:
        soft_assert.assert_info(
            names != expected,
            f"'{username}': Expected sorting to be broken (known defect)."
        )
    else:
        soft_assert.assert_equal(
            names,
            expected,
            f"'{username}': Expected products to be sorted Z-A correctly."
        )




# Xray: TEST-24
@pytest.mark.products
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_performance_valid_users())
def test_products_sort_name_za_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    start_time = time.time()
    product_page.sort_by_name_za()
    end_time = time.time()
    sorting_time = end_time - start_time
    if username == "performance_glitch_user":
        soft_assert.assert_info(
            sorting_time > 5,
            f"'{username}' Expected delay met — sorting took {sorting_time:.2f}s"
        )
    else:
        soft_assert.assert_true(
            sorting_time < 2,
            f"'{username}' Sorting duration: {sorting_time:.2f}s"
        )



# Xray: TEST-25
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_sort_dropdown_low_to_high_selection(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    expects_sorting_broken = username in ["problem_user", "visual_user", "error_user"]
    expects_popup_alert = username == "error_user"
    try:
        product_page.sort_by_price_low_to_high()
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        if expects_popup_alert:
            soft_assert.assert_info(
                True,
                f"'{username}': Expected sorting alert: '{alert_text}'."
            )
        else:
            soft_assert.assert_true(
                False,
                f"'{username}': Unexpected sorting alert appeared: '{alert_text}'."
            )
        return
    except TimeoutException:
        if expects_popup_alert:
            soft_assert.assert_info(
                False,
                f"'{username}': Expected sorting alert, but none appeared."
            )
            return
    prices = product_page.get_product_prices()
    expected = sorted(prices)
    if expects_sorting_broken:
        soft_assert.assert_info(
            prices != expected,
            f"'{username}': Expected sorting to be broken (known defect)."
        )
    else:
        soft_assert.assert_equal(
            prices,
            expected,
            f"'{username}': Expected prices to be sorted Low to High correctly. {expected}"
        )



# Xray: TEST-26
@pytest.mark.products
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_performance_valid_users())
def test_products_sort_low_to_high_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    start_time = time.time()
    product_page.sort_by_price_low_to_high()
    end_time = time.time()
    sorting_time = end_time - start_time
    if username == "performance_glitch_user":
        soft_assert.assert_info(
            sorting_time > 5,
            f"'{username}' Expected delay met — sorting took {sorting_time:.2f}s"
        )
    else:
        soft_assert.assert_true(
            sorting_time < 2,
            f"'{username}' Sorting duration: {sorting_time:.2f}s"
        )


# Xray: TEST-27
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_sort_dropdown_high_to_low_selection(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    expects_sorting_broken = username in ["problem_user", "visual_user", "error_user"]
    expects_popup_alert = username == "error_user"
    try:
        product_page.sort_by_price_high_to_low()
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        if expects_popup_alert:
            soft_assert.assert_info(
                True,
                f"'{username}': Expected sorting alert: '{alert_text}'."
            )
        else:
            soft_assert.assert_true(
                False,
                f"'{username}': Unexpected sorting alert appeared: '{alert_text}'."
            )
        return
    except TimeoutException:
        if expects_popup_alert:
            soft_assert.assert_info(
                False,
                f"'{username}': Expected sorting alert, but none appeared."
            )
            return
    prices = product_page.get_product_prices()
    expected = sorted(prices, reverse=True)
    if expects_sorting_broken:
        soft_assert.assert_info(
            prices != expected,
            f"'{username}' Expected sorting to be broken (Known Issue)."
        )
    else:
        soft_assert.assert_equal(
            prices,
            expected,
            f"'{username}': Expected sorted prices (High to Low): {expected}"
        )



# Xray: TEST-28
@pytest.mark.products
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_performance_valid_users())
def test_products_sort_high_to_low_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    start_time = time.time()
    product_page.sort_by_price_high_to_low()
    end_time = time.time()
    sorting_time = end_time - start_time
    if username == "performance_glitch_user":
        soft_assert.assert_info(
            sorting_time > 5,
            f"'{username}' Expected delay met — sorting took {sorting_time:.2f}s"
        )
    else:
        soft_assert.assert_true(
            sorting_time < 2,
            f"[{username}] Sorting duration: {sorting_time:.2f}s"
        )






# ------------------ FOOTER COMPONENTS AND SOCIAL LINKS TESTS ------------------

# Xray: TEST-29
@pytest.mark.products
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_page_footer_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    soft_assert.assert_true(product_page.is_footer_social_link_present("Twitter"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('Twitter') to be True")
    soft_assert.assert_true(product_page.is_footer_social_link_present("Facebook"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('Facebook') to be True")
    soft_assert.assert_true(product_page.is_footer_social_link_present("LinkedIn"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('LinkedIn') to be True")
    expected_copy = "© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    actual_copy = product_page.get_footer_legal_text()
    soft_assert.assert_equal(actual_copy, expected_copy, f"'{username}'Expected: {expected_copy}")




# Xray: TEST-30
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_twitter_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.scroll_to_footer()
    original_window = driver.current_window_handle
    product_page.click_footer_social_link("Twitter")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://x.com/saucelabs"))
    soft_assert.assert_true(
        "https://x.com/saucelabs" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://x.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



# Xray: TEST-31
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_facebook_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.scroll_to_footer()
    original_window = driver.current_window_handle
    product_page.click_footer_social_link("Facebook")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.facebook.com/saucelabs"))
    soft_assert.assert_true(
        "https://www.facebook.com/saucelabs" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://www.facebook.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)


# Xray: TEST-32
@pytest.mark.products
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_products
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_products_linkedin_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.scroll_to_footer()
    original_window = driver.current_window_handle
    product_page.click_footer_social_link("LinkedIn")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.linkedin.com/company/sauce-labs/"))
    soft_assert.assert_true(
        "https://www.linkedin.com/company/sauce-labs/" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://www.linkedin.com/company/sauce-labs/' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)







