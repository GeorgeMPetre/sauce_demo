import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.locators import BasePageLocators, CartPageLocators
from pages.page_cart import CartFunctionalityPage
from pages.page_checkout_info import CheckoutProcessPage
from pages.page_checkout_overview import CheckoutOverviewPage
from pages.page_products import ProductBrowsingPage
from utils.data_loader import load_checkout_valid_users





# ------------------ HEADER COMPONENTS TESTS ------------------

# Xray: TEST-89
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_primary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_equal(overview_page.get_app_logo_text(), "Swag Labs", f"'{username}' Expected: Swag Labs")
    soft_assert.assert_true(overview_page.is_cart_icon_visible(),
                            f"'{username}' Expected: overview_page.is_cart_icon_visible() to be True")
    soft_assert.assert_true(overview_page.is_burger_menu_button_visible(),
                            f"'{username}'Expected: overview_page.is_burger_menu_button_visible() to be True")



# Xray: TEST-90
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_secondary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_true(overview_page.is_products_title_visible(), f"'{username}' Expected: overview_page.is_products_title_visible() to be True")





# ------------------ BURGER MENU FUNCTIONALITY TESTS ------------------

# Xray: TEST-91
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_page_menu_open(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    expected_menu_options = BasePageLocators.EXPECTED_MENU_OPTIONS
    actual_menu_options = overview_page.get_menu_options()
    soft_assert.assert_true(overview_page.is_menu_open(), f"'{username}' Expected: overview_page.is_menu_open() to be True")
    soft_assert.assert_equal(sorted(actual_menu_options), sorted(expected_menu_options),
                             f"'{username}' Expected: {sorted(expected_menu_options)}")



# Xray: TEST-92
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_checkout_logout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    overview_page.click_logout()
    soft_assert.assert_true("saucedemo.com" in driver.current_url,
                            f"'{username}' Expected: 'saucedemo.com' in driver.current_url to be True")



# Xray: TEST-93
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_checkout_logout_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    start_time = time.time()
    overview_page.click_logout()
    end_time = time.time()
    logout_time = end_time - start_time
    soft_assert.assert_true("saucedemo.com" in driver.current_url,
                            f"'{username}' Expected: 'saucedemo.com' in driver.current_url to be True")
    soft_assert.assert_true(logout_time < 2, f"'{username}' Expected: logout_time < 2")




# Xray: TEST-94
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_navigation_to_all_items(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    overview_page.click_all_items()
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}' Expected: 'inventory.html' in driver.current_url to be True")



# Xray: TEST-95
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_navigation_to_all_items_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    start_time = time.time()
    overview_page.click_all_items()
    end_time = time.time()
    navigation_time = end_time - start_time
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}' - Expected: 'inventory.html' in current URL after clicking All Items")
    if username == "performance_glitch_user":
        soft_assert.assert_true(navigation_time > 5,
                                f"'{username}' Expected: navigation time exceeded 5 seconds (known defect).")
        soft_assert.assert_info(
            f"'{username}' navigation delay > 5s — known performance issue.")
    else:
        soft_assert.assert_true(navigation_time < 2,
                                f"'{username}' - Expected: navigation time to be under 2 seconds.")


# Xray: TEST-96
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_navigation_to_about(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    soft_assert.assert_true(overview_page.is_menu_open(), f"'{username}'Expected: cart_page.is_menu_open() to be True")
    url = overview_page.click_about_and_handle_redirect()
    soft_assert.assert_true(
        "saucelabs.com" in url,
        f"'{username}'Expected: 'saucelabs.com' in driver.current_url to be True"
    )
    if len(driver.window_handles) > 1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



# Xray: TEST-97
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_reset_app_state_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    start_time = time.time()
    overview_page.click_reset_app_state()
    end_time = time.time()
    reset_time = end_time - start_time
    soft_assert.assert_true(reset_time < 2, f"'{username}' Expected: reset_time < 2")



# Xray: TEST-98
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_reset_app_state_cart_badge_disappearance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.open_menu()
    overview_page.click_reset_app_state()
    cart_badge_gone = WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(CartPageLocators.CART_BADGE))
    soft_assert.assert_true(cart_badge_gone, f"'{username}' Expected: cart_badge_gone to be True")





# ------------------ OVERVIEW DISPLAY & UI VALIDATION TESTS ------------------

# Xray: TEST-99
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_headers_displayed(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_equal(overview_page.get_qty_header_text(), "QTY", f"'{username}' Expected: QTY header text to be 'QTY'.")
    soft_assert.assert_equal(overview_page.get_description_header_text(), "Description", f"'{username}' Expected: Description header text to be 'Description'.")



# Xray: TEST-100
@pytest.mark.checkout_overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_product_display(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_true(overview_page.is_product_present("Sauce Labs Backpack"), f"'{username}' Expected: Product to be present on overview page.")
    soft_assert.assert_in("carry.allTheThings()", overview_page.get_product_description(), f"'{username}' Expected: description to contain product info.")
    soft_assert.assert_equal(overview_page.get_product_price(), "$29.99", f"'{username}' Expected: Product price to be '$29.99'.")



# Xray: TEST-101
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_payment_and_shipping_info(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_equal(overview_page.get_payment_info(), "SauceCard #31337", f"'{username}' Expected: Payment info to be 'SauceCard #31337'.")
    soft_assert.assert_equal(overview_page.get_shipping_info(), "Free Pony Express Delivery!", f"'{username}' Expected: Shipping info to be 'Free Pony Express Delivery!'.")


# Xray: TEST-102
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_summary_totals(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_equal(overview_page.get_item_total(), "Item total: $29.99", f"'{username}' Expected: Item total to be 'Item total: $29.99'.")
    soft_assert.assert_equal(overview_page.get_tax(), "Tax: $2.40", f"'{username}' Expected: Tax to be 'Tax: $2.40'.")
    soft_assert.assert_equal(overview_page.get_total(), "Total: $32.39", f"'{username}' Expected: Total price to be 'Total: $32.39'.")



# Xray: TEST-103
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_click_cart_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.go_to_cart()
    soft_assert.assert_in("cart.html", driver.current_url, f"'{username}' Expected: URL to contain 'cart.html' after clicking cart icon.")



# Xray: TEST-104
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_page_ui_layout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    layout_issues = overview_page.get_ui_layout_issues(username)
    if username == "visual_user":
        if "cart_icon_overlap" in layout_issues:
            soft_assert.assert_info(
                f"'{username}' Info: 'cart_icon_overlap' detected — known layout issue."
            )
    else:
        soft_assert.assert_true(
            "cart_icon_overlap" not in layout_issues,
            f"'{username}' Expected: 'cart_icon_overlap' not in layout_issues to be True"
        )
    soft_assert.assert_true(
        "qty_header_misaligned" not in layout_issues,
        f"'{username}' Expected: 'qty_header_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "description_header_misaligned" not in layout_issues,
        f"'{username}' Expected: 'description_header_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "product_block_misaligned" not in layout_issues,
        f"'{username}' Expected: 'product_block_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "price_alignment_issue" not in layout_issues,
        f"'{username}' Expected: 'price_alignment_issue' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "payment_shipping_info_misaligned" not in layout_issues,
        f"'{username}' Expected: 'payment_shipping_info_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "summary_totals_misaligned" not in layout_issues,
        f"'{username}' Expected: 'summary_totals_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "cancel_button_misaligned" not in layout_issues,
        f"'{username}' Expected: 'cancel_button_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "finish_button_misaligned" not in layout_issues,
        f"'{username}' Expected: 'finish_button_misaligned' not in layout_issues to be True"
    )
    soft_assert.assert_true(
        "footer_misaligned" not in layout_issues,
        f"'{username}' Expected: 'footer_misaligned' not in layout_issues to be True"
    )



# Xray: TEST-105
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_cancel_button_presence(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_true(
        overview_page.is_cancel_button_present(),
        f"'{username}' Expected: 'Cancel' button should be visible on Checkout Overview Page."
    )




# Xray: TEST-106
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview

@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_cancel_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.click_cancel_button()
    soft_assert.assert_true(
        "inventory.html" in driver.current_url,
        f"'{username}' Expected: URL to contain 'inventory.html' after clicking cancel."
    )



# Xray: TEST-107
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_finish_button_presence(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    soft_assert.assert_true(
        overview_page.is_finish_button_present(),
        f"'{username}' Expected: 'Finish' button should be visible on Checkout Overview Page."
    )



# Xray: TEST-108
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.e2e
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_finish_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.click_finish()
    if username == "error_user":
        soft_assert.assert_false(
            overview_page.is_order_successful(),
            f"'{username}' Expected: Order should NOT be completed — Finish button is broken (known bug)."
        )
        soft_assert.assert_info(
            f"'{username}' Finish button is broken — checkout does not complete (known bug)."
        )
    else:
        soft_assert.assert_true(
            overview_page.is_order_successful(),
            f"'{username}' Expected: Order to be completed successfully after clicking Finish."
        )



# Xray: TEST-109
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_finish_button_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    CartFunctionalityPage(driver).click_checkout_button()
    CheckoutProcessPage(driver).complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    start_time = time.time()
    overview_page.click_finish()
    end_time = time.time()
    duration = end_time - start_time
    if username == "error_user":
        soft_assert.assert_false(
            overview_page.is_order_successful(),
            "'error_user' Expected: Finish button to be broken. Known issue."
        )
        soft_assert.assert_info(
            "'error_user' Finish button did not complete checkout — defect confirmed."
        )
    else:
        soft_assert.assert_true(
            overview_page.is_order_successful(),
            f"'{username}' Expected: Order to be completed successfully after clicking Finish."
        )
        soft_assert.assert_true(
            duration <= 2,
            f"'{username}' Expected: Checkout completion time to be under 2 seconds."
        )



# Xray: TEST-110
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_checkout_overview_complete_checkout_empty_cart(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.click_finish()
    if username == "error_user":
        soft_assert.assert_false(
            overview_page.is_order_successful(),
            "'error_user' Expected: Finish button to be broken. Known issue."
        )
        soft_assert.assert_info(
            "'error_user' Finish button did not complete checkout with empty cart — defect confirmed."
        )
    else:
        soft_assert.assert_false(
            overview_page.is_order_successful(),
            f"'{username}' Expected: Checkout not to be successful when cart is empty."
        )
        soft_assert.assert_true(
            overview_page.is_error_displayed(),
            f"'{username}' Expected: An error message to be shown when trying to checkout with an empty cart."
        )






# ------------------ FOOTER COMPONENTS AND SOCIAL LINKS TESTS ------------------

# Xray: TEST-111
@pytest.mark.overview
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_overview_page_footer_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.scroll_to_footer()
    soft_assert.assert_true(overview_page.is_footer_social_link_present("Twitter"),
                            f"'{username}' Expected: overview_page.is_footer_social_link_present('Twitter') to be True")
    soft_assert.assert_true(overview_page.is_footer_social_link_present("Facebook"),
                            f"'{username}' Expected: overview_page.is_footer_social_link_present('Facebook') to be True")
    soft_assert.assert_true(overview_page.is_footer_social_link_present("LinkedIn"),
                            f"'{username}' Expected: overview_page.is_footer_social_link_present('LinkedIn') to be True")
    expected_copy = "© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    actual_copy = overview_page.get_footer_legal_text()
    soft_assert.assert_equal(actual_copy, expected_copy, f"'{username}' Expected: {expected_copy}")




# Xray: TEST-112
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_overview_twitter_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.scroll_to_footer()
    original_window = driver.current_window_handle
    overview_page.click_footer_social_link("Twitter")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://x.com/saucelabs"))
    soft_assert.assert_true(
        "https://x.com/saucelabs" in driver.current_url.lower(),
        f"'{username}' Expected: 'https://x.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



# Xray: TEST-113
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_overview_facebook_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.scroll_to_footer()
    original_window = driver.current_window_handle
    overview_page.click_footer_social_link("Facebook")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.facebook.com/saucelabs"))
    soft_assert.assert_true(
        "https://www.facebook.com/saucelabs" in driver.current_url.lower(),
        f"'{username}' Expected: 'https://www.facebook.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



# Xray: TEST-114
@pytest.mark.overview
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_overview
@pytest.mark.parametrize("username, password", load_checkout_valid_users())
def test_overview_linkedin_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    if username == "error_user":
        soft_assert.assert_info("'error_user' known bug — last name field bypassed, test continues.")
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutProcessPage(driver)
    checkout_page.complete_checkout("John", "Doe", "BR654BR")
    overview_page = CheckoutOverviewPage(driver)
    overview_page.scroll_to_footer()
    original_window = driver.current_window_handle
    overview_page.click_footer_social_link("LinkedIn")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    try:
        WebDriverWait(driver, 15).until(EC.url_contains("linkedin.com/company/sauce-labs"))
        soft_assert.assert_true(
            "linkedin.com/company/sauce-labs" in driver.current_url.lower(),
            f"'{username}' Expected: LinkedIn company page to open."
        )
    except TimeoutException:
        soft_assert.assert_true(False, f"'{username}' LinkedIn company page did not load in time — TimeoutException.")

    soft_assert.assert_true(
        "https://www.linkedin.com/company/sauce-labs/" in driver.current_url.lower(),
        f"'{username}' Expected: 'https://www.linkedin.com/company/sauce-labs/' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)



