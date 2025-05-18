import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.locators import BasePageLocators, CartPageLocators
from pages.page_cart import CartFunctionalityPage
from pages.page_checkout_info import CheckoutProcessPage
from pages.page_products import ProductBrowsingPage
from utils.data_loader import load_active_users_for_full_tests




# ------------------ HEADER COMPONENTS TESTS ------------------

# Xray: TEST-59
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_primary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_equal(checkout_page.get_app_logo_text(), "Swag Labs", "Expected: Swag Labs")
    soft_assert.assert_true(checkout_page.is_cart_icon_visible(),
                            f"'{username}' Expected: checkout_page.is_cart_icon_visible() to be True")
    soft_assert.assert_true(checkout_page.is_burger_menu_button_visible(),
                            f"'{username}' Expected: checkout_page.is_burger_menu_button_visible() to be True")




# Xray: TEST-60
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_secondary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(checkout_page.is_products_title_visible(), f"'{username}' Expected: checkout_page.is_products_title_visible() to be True")




# ------------------ BURGER MENU FUNCTIONALITY TESTS ------------------

# Xray: TEST-61
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_page_menu_open(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    expected_menu_options = BasePageLocators.EXPECTED_MENU_OPTIONS
    actual_menu_options = checkout_page.get_menu_options()
    soft_assert.assert_true(checkout_page.is_menu_open(), f"'{username}' Expected: checkout_page.is_menu_open() to be True")
    soft_assert.assert_equal(sorted(actual_menu_options), sorted(expected_menu_options),
                             f"Expected: {sorted(expected_menu_options)}")




# Xray: TEST-62
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_checkout_logout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    checkout_page.click_logout()
    soft_assert.assert_true("saucedemo.com" in driver.current_url,
                            f"'{username}' Expected: 'saucedemo.com' in driver.current_url to be True")




# Xray: TEST-63
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_checkout_logout_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    start_time = time.time()
    checkout_page.click_logout()
    end_time = time.time()
    logout_time = end_time - start_time
    soft_assert.assert_true("saucedemo.com" in driver.current_url,
                            f"'{username}' Expected: 'saucedemo.com' in driver.current_url to be True")
    soft_assert.assert_true(logout_time < 2, f"'{username}' Expected: logout_time < 2")




# Xray: TEST-64
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_navigation_to_all_items(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    checkout_page.click_all_items()
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}' Expected: 'inventory.html' in driver.current_url to be True")




# Xray: TEST-65
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_navigation_to_all_items_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    start_time = time.time()
    checkout_page.click_all_items()
    end_time = time.time()
    navigation_time = end_time - start_time
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}' Expected: 'inventory.html' in current URL after clicking All Items")
    if username == "performance_glitch_user":
        if navigation_time > 5:
            soft_assert.assert_info(
                f"'{username}' Expected: navigation time exceeded 5 seconds (expected for known defect). Actual: {navigation_time:.2f}s")
        else:
            soft_assert.assert_info(
                f"UNEXPECTED: '{username}' navigation time was {navigation_time:.2f}s (expected > 5s for known defect)")
    else:
        soft_assert.assert_true(navigation_time < 2,
                                f"'{username}' Expected: navigation time to be under 2 seconds.")




# Xray: TEST-66
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_navigation_to_about(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    soft_assert.assert_true(
        checkout_page.is_menu_open(),
        f"'{username}'Expected: cart_page.is_menu_open() to be True"
    )
    url = checkout_page.click_about_and_handle_redirect()
    soft_assert.assert_true(
        "saucelabs.com" in url,
        f"'{username}'Expected: 'saucelabs.com' in driver.current_url to be True"
    )
    if len(driver.window_handles) > 1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])





# Xray: TEST-67
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_reset_app_state_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    start_time = time.time()
    cart_page.click_reset_app_state()
    end_time = time.time()
    reset_time = end_time - start_time
    soft_assert.assert_true(reset_time < 2, f"'{username}' Expected: reset_time < 2")





# Xray: TEST-68
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_reset_app_state_cart_badge_disappearance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.open_menu()
    checkout_page.click_reset_app_state()
    cart_badge_gone = WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(CartPageLocators.CART_BADGE))
    soft_assert.assert_true(cart_badge_gone, f"'{username}' Expected: cart_badge_gone to be True")






# ------------------ CHECK INFO DISPLAY & UI VALIDATION TESTS ------------------

# Xray: TEST-69
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_click_cart(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.go_to_cart()
    soft_assert.assert_in("cart.html", driver.current_url, f"'{username}' Expected: 'cart.html' in driver.current_url to be True")




# Xray: TEST-70
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_title_visibility(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(
        checkout_page.is_checkout_title_present(),
        f"'{username}' Expected: Title 'Checkout: Your Information' to be visible on page"
    )




# Xray: TEST-71
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_fields_visibility(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(checkout_page.is_first_name_field_present(),
                            f"'{username}' Expected: First Name field to be visible on Checkout Info page")
    soft_assert.assert_true(checkout_page.is_last_name_field_present(),
                            f"'{username}' Expected: Last Name field to be visible on Checkout Info page")
    soft_assert.assert_true(checkout_page.is_postal_code_field_present(),
                            f"'{username}' Expected: Postal Code field to be visible on Checkout Info page")



# Xray: TEST-72
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("firstname, expected_valid", [
    ("John", True),
    ("Anna-Marie", True),
    ("12345", False),
    ("!@#$%", False),
    ("", False)
])
def test_checkout_info_equivalence_partitioning_firstname(setup, firstname, expected_valid, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout(firstname, "Doe", "BR654BR")
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
                                f"'{username}' Expected error message to be displayed due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if not is_error_visible else ''}blocked correctly with UI feedback")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if is_on_step_two else ''}blocked — defect {'still active' if is_on_step_two else 'confirmed'}")
    else:
        if expected_valid:
            soft_assert.assert_true(is_on_step_two,
                                    f"'{username}' Expected to proceed with valid first name '{firstname}'")
            if is_on_step_two:
                print(f"PASS: '{username}' proceeded with valid first name '{firstname}'")
        else:
            soft_assert.assert_true(not is_on_step_two,
                                    f"'{username}' Expected to be blocked with invalid first name '{firstname}'")
            soft_assert.assert_true(is_error_visible,
                                    f"'{username}' Expected error message for invalid first name")
            if not username.startswith(("problem_user", "error_user")):  # Prevent info duplicate
                soft_assert.assert_info(
                    f"'{username}' error message {'shown' if is_error_visible else 'missing'} for invalid first name")




# Xray: TEST-73
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("lastname, expected_valid", [
    ("Doe", True),
    ("O'Connor", True),
    ("!@#$", False),
    ("12345", False),
    ("", False)
])
def test_checkout_info_equivalence_partitioning_lastname(setup, lastname, expected_valid, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", lastname, "BR654BR")
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
                                f"'{username}' Expected error message to be displayed due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if not is_error_visible else ''}blocked correctly with UI feedback")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if is_on_step_two else ''}blocked — defect {'confirmed' if not is_on_step_two else 'still active'}")
    else:
        if expected_valid:
            soft_assert.assert_true(is_on_step_two,
                                    f"'{username}' Expected to proceed with valid last name '{lastname}'")
            if is_on_step_two:
                print(f"PASS: '{username}' proceeded with valid lastname '{lastname}'")
        else:
            soft_assert.assert_true(not is_on_step_two,
                                    f"'{username}' Expected to be blocked with invalid last name '{lastname}'")
            soft_assert.assert_true(is_error_visible,
                                    f"'{username}' Expected error message for invalid last name")
            soft_assert.assert_info(
                f"'{username}' error message {'shown' if is_error_visible else 'missing'} for invalid last name")




# Xray: TEST-74
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("postcode, expected_valid", [
    ("BR123", True),
    ("CT4 2HN", True),
    ("123!", False),
    ("", False),
    ("     ", False)
])
def test_checkout_info_equivalence_partitioning_postalcode(setup, postcode, expected_valid, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", postcode)
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
            f"'{username}' Expected error message to be displayed due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if not is_error_visible else ''}blocked correctly with UI feedback")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if is_on_step_two else ''}blocked — defect {'confirmed' if not is_on_step_two else 'still active'}")
    else:
        if expected_valid:
            soft_assert.assert_true(is_on_step_two,
                f"'{username}' Expected to proceed with valid postcode '{postcode}'")
            if is_on_step_two:
                print(f"PASS: '{username}' proceeded with valid postcode '{postcode}'")
        else:
            soft_assert.assert_true(not is_on_step_two,
                f"'{username}' Expected to be blocked with invalid postcode '{postcode}'")
            soft_assert.assert_true(is_error_visible,
                f"'{username}' Expected error message for invalid postcode")
            soft_assert.assert_info(
                f"'{username}' error message {'shown' if is_error_visible else 'missing'} for invalid postcode")





# Xray: TEST-75
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("firstname", ["J", "Jo", "Joh" * 10 + "n"])
def test_checkout_info_firstname_length_boundaries(setup, firstname, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout(firstname, "Doe", "BR123")
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    firstname_length = len(firstname)
    is_valid = 2 <= firstname_length <= 30
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
            f"'{username}' Expected error message to be displayed due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if not is_error_visible else ''}blocked correctly with UI feedback")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}'  Expected to be blocked due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if is_on_step_two else ''}blocked — defect {'confirmed' if not is_on_step_two else 'still active'}")
    else:
        if is_valid:
            soft_assert.assert_true(is_on_step_two,
                f"'{username}' Expected to proceed with valid firstname length {firstname_length}")
        else:
            soft_assert.assert_true(not is_on_step_two,
                f"'{username}' Expected to be blocked with invalid firstname length {firstname_length}")
            soft_assert.assert_true(is_error_visible,
                f"'{username}' Expected error message for invalid firstname")
            soft_assert.assert_info(
                f"'{username}' error message {'shown' if is_error_visible else 'missing'} for invalid firstname")





# Xray: TEST-76
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("lastname", ["D", "Do", "Doe" * 10 + "e"])
def test_checkout_info_lastname_length_boundaries(setup, lastname, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", lastname, "BR123")
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    lastname_length = len(lastname)
    is_valid = 2 <= lastname_length <= 30
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
            f"'{username}' Expected error message to be displayed due to broken last name field")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if not is_error_visible else ''}blocked correctly with UI feedback")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field (known defect)")
        soft_assert.assert_info(
            f"'{username}' was {'not ' if is_on_step_two else ''}blocked — defect {'confirmed' if not is_on_step_two else 'still active'}")
    else:
        if is_valid:
            soft_assert.assert_true(is_on_step_two,
                f"'{username}' Expected to proceed with valid lastname length {lastname_length}")
        else:
            soft_assert.assert_true(not is_on_step_two,
                f"'{username}' Expected to be blocked with invalid lastname length {lastname_length}")
            soft_assert.assert_true(is_error_visible,
                f"'{username}' Expected error message for invalid lastname")
            soft_assert.assert_info(
                f"'{username}' error message {'shown' if is_error_visible else 'missing'} for invalid lastname")




# Xray: TEST-77
@pytest.mark.info
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
@pytest.mark.parametrize("postcode", ["123", "1234", "12345678901"])
def test_checkout_info_postcode_length_boundaries(setup, postcode, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", postcode)
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    postcode_length = len(postcode)
    is_valid = 4 <= postcode_length <= 10
    try:
        error_element = driver.find_element(By.CLASS_NAME, "error-message-container")
        is_error_visible = error_element.is_displayed()
    except NoSuchElementException:
        is_error_visible = False
    if username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
            f"'{username}' Expected error message to be displayed due to broken last name field")
        if not is_error_visible:
            soft_assert.assert_info(
                f"'{username}' was blocked but no error message shown — UI bug")
        else:
            soft_assert.assert_info(
                f"'{username}' was correctly blocked with an error message")
    elif username == "error_user":
        soft_assert.assert_true( not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field (known defect)")
        if not is_on_step_two:
            soft_assert.assert_info(
                f"'{username}' was blocked — unexpected behavior (defect confirmed)")
        else:
            soft_assert.assert_info(
                f"'{username}' was NOT blocked — broken field bug confirmed")
    else:
        if is_valid:
            soft_assert.assert_true(is_on_step_two,
                f"'{username}' Expected to proceed with valid postcode length {postcode_length}")
            if is_on_step_two:
                print(f"PASS: '{username}' proceeded with valid postcode length {postcode_length}")
        else:
            soft_assert.assert_true(not is_on_step_two,
                f"'{username}' Expected to be blocked with invalid postcode length {postcode_length}")
            soft_assert.assert_true(is_error_visible,
                f"'{username}' Expected error message for invalid postcode")
            if not is_error_visible:
                soft_assert.assert_info(
                    f"'{username}' was NOT blocked for invalid postcode length {postcode_length}")
            else:
                print(f"PASS: '{username}' blocked with invalid postcode length {postcode_length}")




# Xray: TEST-78
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_page_ui_layout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_info_page = CheckoutProcessPage(driver)
    layout_issues = checkout_info_page.get_ui_layout_issues()
    if username == "visual_user":
        if "cart_icon_overlap" in layout_issues:
            soft_assert.assert_info(
                f"'{username}'  Info: 'cart_icon_overlap' detected — cart icon overlaps with the header (known layout issue).")
    else:
        soft_assert.assert_true("cart_icon_overlap" not in layout_issues,
                                f"'{username}' Expected: cart_icon_overlap not in layout_issues to be True.")
    soft_assert.assert_true("form_title_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'form_title_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("first_name_field_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'first_name_field_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("last_name_field_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'last_name_field_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("postal_code_field_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'postal_code_field_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("continue_button_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'continue_button_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("cancel_button_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'cancel_button_misaligned' not in layout_issues to be True")
    soft_assert.assert_true("footer_misaligned" not in layout_issues,
                            f"'{username}' Expected: 'footer_misaligned' not in layout_issues to be True")




# Xray: TEST-79
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_cancel_button_visibility(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(
        checkout_page.is_cancel_button_present(),
        f"'{username}' Expected: Cancel button to be visible on Checkout Info page"
    )




# Xray: TEST-80
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_cancel_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.cancel_checkout()
    soft_assert.assert_true("cart" in driver.current_url, f"'{username}' Expected: 'cart' in driver.current_url to be True")




# Xray: TEST-81
@pytest.mark.info
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_cancel_button_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    start_time = time.time()
    checkout_page.cancel_checkout()
    end_time = time.time()
    navigation_time = end_time - start_time
    soft_assert.assert_true("cart" in driver.current_url, f"'{username}' Expected: 'cart' in driver.current_url to be True")
    soft_assert.assert_true(navigation_time < 2,
            f"Expected: navigation_time < 2 for '{username}'.")



# Xray: TEST-82
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_continue_button_visibility(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(
        checkout_page.is_continue_button_present(),
        f"'{username}' Expected: Continue button to be visible on Checkout Info page"
    )



# Xray: TEST-83
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_continue_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR65BR")
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    is_error_visible = checkout_page.is_error_message_displayed()
    if username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        if not is_on_step_two:
            soft_assert.assert_info(
                f"'{username}' was blocked as expected — but no error message shown (known defect)")
        else:
            soft_assert.assert_info(
                f"'{username}' was NOT blocked — broken field bug confirmed")
    elif username == "problem_user":
        soft_assert.assert_true(not is_on_step_two,
            f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(is_error_visible,
            f"'{username}' Expected: Error message should be displayed when blocked")
        if not is_error_visible:
            soft_assert.assert_info(
                f"'{username}' was blocked but no error message appeared — UI bug")
        else:
            soft_assert.assert_info(
                f"'{username}' was correctly blocked with an error message")
    else:
        soft_assert.assert_true(is_on_step_two,
            f"'{username}' Expected to proceed to 'checkout-step-two'")
        print(f"PASS: '{username}' proceeded to 'checkout-step-two'")




# Xray: TEST-84
@pytest.mark.info
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_checkout_info_continue_button_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    start_time = time.time()
    checkout_page.complete_checkout("John", "Doe", "BR65BR")
    end_time = time.time()
    navigation_time = end_time - start_time
    current_url = driver.current_url
    is_on_step_two = "checkout-step-two" in current_url
    if username == "problem_user":
        blocked = not is_on_step_two
        error_displayed = checkout_page.is_error_message_displayed()

        soft_assert.assert_true(blocked,
                                f"'{username}' Expected to be blocked due to broken last name field")
        soft_assert.assert_true(error_displayed,
                                f"'{username}' Expected: error message to be shown on broken last name field")
        if blocked and error_displayed:
            soft_assert.assert_info(
                f"'{username}' was correctly blocked and error message was shown")
        else:
            soft_assert.assert_info(
                f"'{username}' behavior was unexpected. Check blockage and error visibility")
    elif username == "error_user":
        soft_assert.assert_true(not is_on_step_two,
                                f"'{username}' Expected to be blocked due to broken last name field")
        if not is_on_step_two:
            soft_assert.assert_info(
                f"'{username}' was blocked as expected — but no error message shown (known defect)")
            print(f"PASS: '{username}' was blocked as expected (known bug)")
        else:
            soft_assert.assert_info(
                f"'{username}' was NOT blocked — broken field bug confirmed")
    else:
        soft_assert.assert_true(is_on_step_two,
                                f"'{username}' Expected to proceed to 'checkout-step-two'")
        soft_assert.assert_true(navigation_time < 2,
                                f"Expected: navigation_time < 2 for '{username}' (actual: {navigation_time:.2f}s)")




# ------------------ FOOTER COMPONENTS AND SOCIAL LINKS TESTS ------------------

# Xray: TEST-85
@pytest.mark.info
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_info_page_footer_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    soft_assert.assert_true(checkout_page.is_footer_social_link_present("Twitter"),
                            "Expected: product_page.is_footer_social_link_present('Twitter') to be True")
    soft_assert.assert_true(checkout_page.is_footer_social_link_present("Facebook"),
                            "Expected: product_page.is_footer_social_link_present('Facebook') to be True")
    soft_assert.assert_true(checkout_page.is_footer_social_link_present("LinkedIn"),
                            "Expected: product_page.is_footer_social_link_present('LinkedIn') to be True")
    expected_copy = "© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    actual_copy = checkout_page.get_footer_legal_text()
    soft_assert.assert_equal(actual_copy, expected_copy, f"Expected: {expected_copy}")



# Xray: TEST-86
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_info_twitter_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.scroll_to_footer()
    original_window = driver.current_window_handle
    checkout_page.click_footer_social_link("Twitter")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://x.com/saucelabs"))
    soft_assert.assert_true(
        "https://x.com/saucelabs" in driver.current_url.lower(),
        "Expected: 'https://x.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



# Xray: TEST-87
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_info_facebook_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.scroll_to_footer()
    original_window = driver.current_window_handle
    checkout_page.click_footer_social_link("Facebook")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.facebook.com/saucelabs"))
    soft_assert.assert_true(
        "https://www.facebook.com/saucelabs" in driver.current_url.lower(),
        "Expected: 'https://www.facebook.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



# Xray: TEST-88
@pytest.mark.info
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_info
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_info_linkedin_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.scroll_to_footer()
    original_window = driver.current_window_handle
    checkout_page.click_footer_social_link("LinkedIn")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.linkedin.com/company/sauce-labs/"))
    soft_assert.assert_true(
        "https://www.linkedin.com/company/sauce-labs/" in driver.current_url.lower(),
        "Expected: 'https://www.linkedin.com/company/sauce-labs/' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)

