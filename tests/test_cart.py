import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.locators import BasePageLocators, CartPageLocators
from pages.page_cart import CartFunctionalityPage
from pages.page_products import ProductBrowsingPage
from utils.data_loader import load_active_users_for_full_tests




# ------------------ HEADER COMPONENTS TESTS ------------------

# Xray: TEST-33
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_page_primary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_equal(cart_page.get_app_logo_text(), "Swag Labs", f"'{username}'Expected: Swag Labs")
    soft_assert.assert_true(cart_page.is_cart_icon_visible(), f"'{username}' Expected: cart_page.is_cart_icon_visible() to be True")
    soft_assert.assert_true(cart_page.is_burger_menu_button_visible(),
                            f"'{username}' Expected: cart_page.is_burger_menu_button_visible() to be True")




# Xray: TEST-34
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_page_secondary_header_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_true(cart_page.is_products_title_visible(), f"'{username}'Expected: cart_page.is_products_title_visible() to be True")





# ------------------ BURGER MENU FUNCTIONALITY TESTS ------------------

# Xray: TEST-35
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_menu_open(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    expected_menu_options = BasePageLocators.EXPECTED_MENU_OPTIONS
    actual_menu_options = cart_page.get_menu_options()
    soft_assert.assert_true(cart_page.is_menu_open(), f"'{username}'Expected: product_page.is_menu_open() to be True")
    soft_assert.assert_equal(sorted(actual_menu_options), sorted(expected_menu_options),
                             f"'{username}'Expected: {sorted(expected_menu_options)}")



# Xray: TEST-36
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_logout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    cart_page.click_logout()
    soft_assert.assert_true("www.saucedemo.com" in driver.current_url,
                            f"'{username}'Expected: 'www.saucedemo.com' in driver.current_url to be True")




# Xray: TEST-37
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_logout_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    start_time = time.time()
    cart_page.click_logout()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))
    end_time = time.time()
    logout_time = end_time - start_time
    soft_assert.assert_true(logout_time < 2, f"'{username}' Expected: logout_time < 2")
    soft_assert.assert_true("www.saucedemo.com" in driver.current_url,
                            f"'{username}' Expected: 'www.saucedemo.com' in driver.current_url to be True")



# Xray: TEST-38
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_navigation_to_all_items(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    cart_page.click_all_items()
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}'Expected: 'inventory.html' in driver.current_url to be True")





# Xray: TEST-39
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_navigation_to_all_items_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    start_time = time.time()
    cart_page.open_menu()
    cart_page.click_all_items()
    end_time = time.time()
    navigation_time = end_time - start_time
    soft_assert.assert_true("inventory.html" in driver.current_url,
                            f"'{username}'Expected: 'inventory.html' in driver.current_url to be True")
    if username == "performance_glitch_user":
        if navigation_time > 5:
            soft_assert.assert_info(f"Expected: navigation_time > 5s for '{username}' - Actual: {navigation_time:.2f}s")
        else:
            soft_assert.assert_info(f"UNEXPECTED: navigation_time was {navigation_time:.2f}s for '{username}', expected > 5s")
    else:
        soft_assert.assert_true(navigation_time < 2,
            f"Expected: navigation_time < 2s for '{username}', but was {navigation_time:.2f}s")




# Xray: TEST-40
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_navigation_to_about(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    soft_assert.assert_true(cart_page.is_menu_open(), f"'{username}'Expected: cart_page.is_menu_open() to be True")
    url = cart_page.click_about_and_handle_redirect()
    soft_assert.assert_true(
        "saucelabs.com" in url,
        f"'{username}'Expected: 'saucelabs.com' in driver.current_url to be True"
    )
    if len(driver.window_handles) > 1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



# Xray: TEST-41
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_reset_app_state_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    start_time = time.time()
    cart_page.click_reset_app_state()
    end_time = time.time()
    reset_time = end_time - start_time
    soft_assert.assert_true(reset_time < 2, f"'{username}'Expected: reset_time < 2")



# Xray: TEST-42
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_reset_app_state_cart_badge_disappearance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.open_menu()
    cart_page.click_reset_app_state()
    cart_badge_gone = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(CartPageLocators.CART_BADGE))
    soft_assert.assert_true(cart_badge_gone, f"'{username}'Expected: cart_badge_gone to be True")






# ------------------ CART DISPLAY & UI VALIDATION TESTS ------------------

# Xray: TEST-43
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_qty_description(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_equal(cart_page.get_qty_header_text(), "QTY", f"'{username}'Expected: QTY")
    soft_assert.assert_equal(cart_page.get_description_header_text(), "Description", f"'{username}'Expected: Description")




# Xray: TEST-44
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_product_description(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_equal(cart_page.get_product_name(), "Sauce Labs Backpack", f"'{username}'Expected: Sauce Labs Backpack")
    soft_assert.assert_equal(cart_page.get_product_description(),
                             "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
                             f"'{username}'Expected: correct product description")




# Xray: TEST-45
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_product_price(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_equal(cart_page.get_product_price_in_cart()[0], "$29.99", f"'{username}'Expected: $29.99")





# Xray: TEST-46
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_page_ui_layout(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    layout_issues = cart_page.get_ui_layout_issues()
    soft_assert.assert_true("cart_title_missing" not in layout_issues,
                            f"'{username}'Expected: cart_title_missing not in layout_issues to be True")
    if username == "visual_user":
        soft_assert.assert_info("cart_icon_overlap" in layout_issues,
                                f"'{username}'Expected: 'cart_icon_overlap' in layout_issues to be True.")
    else:
        soft_assert.assert_true("cart_icon_overlap" not in layout_issues,
                                f"'{username}'Expected 'cart_icon_overlap' not in layout_issues to be True.")

    soft_assert.assert_true("product_info_missing" not in layout_issues,
                            f"'{username}'Expected: product_info_missing not in layout_issues to be True")
    if "checkout_button_issue" in layout_issues:
        if username == "visual_user":
            soft_assert.assert_info(
                f"'{username}'Expected: 'checkout_button_issue' in layout_issues to be True.")
        else:
            soft_assert.assert_true(False,
                                    f"'{username}'Expected: checkout_button_issue not in layout_issues to be True.")
    else:
        soft_assert.assert_true(True,
                                f"'{username}'Expected: checkout_button_issue not in layout_issues to be True.")
    soft_assert.assert_true("continue_button_issue" not in layout_issues,
                            f"'{username}'Expected: continue_button_issue not in layout_issues to be True")

    soft_assert.assert_true("footer_layout_broken" not in layout_issues,
                            f"'{username}'Expected: footer_layout_broken not in layout_issues to be True")

    soft_assert.assert_true("qty_column_not_left_of_description" not in layout_issues,
                            f"'{username}'Expected: QTY column to be left of Description column.")




# Xray: TEST-47
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_remove_button_present(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_true(
        cart_page.is_remove_button_present(),
        f"'{username}' Expected: Remove button to be present"
    )





# Xray: TEST-48
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_remove_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_remove_button()
    soft_assert.assert_true(cart_page.is_cart_empty(), f"'{username}'Expected: cart_page.is_cart_empty() to be True")




# Xray: TEST-49
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_continue_shopping_button_present(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_true(
        cart_page.is_continue_shopping_button_present(),
        f"'{username}' Expected: Continue Shopping button to be present"
    )





# Xray: TEST-50
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_continue_shopping_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.remove_all_items_from_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_continue_shopping_button()
    soft_assert.assert_true(cart_page.is_on_inventory_page(), f"'{username}'Expected: cart_page.is_on_inventory_page() to be True")




# Xray: TEST-51
@pytest.mark.cart
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_continue_shopping_button_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.remove_all_items_from_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    start_time = time.time()
    cart_page.click_continue_shopping_button()
    duration = time.time() - start_time
    if username == "performance_glitch_user":
        if duration > 5:
            soft_assert.assert_info(
                f"Expected: continue shopping button response time > 5 seconds for user '{username}'. Actual: {duration:.2f}s")
        else:
            soft_assert.assert_info(
                f"UNEXPECTED: continue shopping button was too fast ({duration:.2f}s) for user '{username}', expected > 5s.")
    else:
        soft_assert.assert_true(
            duration <= 2,
            f"Expected: login time <= 2 seconds for user '{username}'."
        )
    soft_assert.assert_true(cart_page.is_on_inventory_page(), f"'{username}'Expected: cart_page.is_on_inventory_page() to be True")





# Xray: TEST-52
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_checkout_button_present(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_true(
        cart_page.is_checkout_button_present(),
        f"'{username}' Expected: Checkout button to be present"
    )





# Xray: TEST-53
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_checkout_button_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.click_checkout_button()
    soft_assert.assert_true(cart_page.is_on_checkout_page(), f"'{username}'Expected: cart_page.is_on_checkout_page() to be True")




# Xray: TEST-54
@pytest.mark.cart
@pytest.mark.performance
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_checkout_button_response_time(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    start_time = time.time()
    cart_page.click_checkout_button()
    duration = time.time() - start_time
    soft_assert.assert_true(duration < 2.0, f"'{username}'Expected: Checkout button response < 2s, Actual: {duration:.2f}s")
    soft_assert.assert_true(cart_page.is_on_checkout_page(), f"'{username}'Expected: cart_page.is_on_checkout_page() to be True")



# ------------------ FOOTER COMPONENTS AND SOCIAL LINKS TESTS ------------------

# Xray: TEST-55
@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_page_footer_components(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    soft_assert.assert_true(cart_page.is_footer_social_link_present("Twitter"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('Twitter') to be True")
    soft_assert.assert_true(cart_page.is_footer_social_link_present("Facebook"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('Facebook') to be True")
    soft_assert.assert_true(cart_page.is_footer_social_link_present("LinkedIn"),
                            f"'{username}'Expected: product_page.is_footer_social_link_present('LinkedIn') to be True")
    expected_copy = "© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    actual_copy = cart_page.get_footer_legal_text()
    soft_assert.assert_equal(actual_copy, expected_copy, f"'{username}'Expected: {expected_copy}")





# Xray: TEST-56
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_twitter_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.scroll_to_footer()
    original_window = driver.current_window_handle
    cart_page.click_footer_social_link("Twitter")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://x.com/saucelabs"))
    soft_assert.assert_true(
        "https://x.com/saucelabs" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://x.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)




# Xray: TEST-57
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_facebook_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.scroll_to_footer()
    original_window = driver.current_window_handle
    cart_page.click_footer_social_link("Facebook")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.facebook.com/saucelabs"))
    soft_assert.assert_true(
        "https://www.facebook.com/saucelabs" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://www.facebook.com/saucelabs' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)





# Xray: TEST-58
@pytest.mark.cart
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression_cart
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_cart_linkedin_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    product_page = ProductBrowsingPage(driver)
    product_page.go_to_cart()
    cart_page = CartFunctionalityPage(driver)
    cart_page.scroll_to_footer()
    original_window = driver.current_window_handle
    cart_page.click_footer_social_link("LinkedIn")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window([w for w in windows if w != original_window][0])
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.linkedin.com"))
    soft_assert.assert_true(
        "https://www.linkedin.com/company/sauce-labs/" in driver.current_url.lower(),
        f"'{username}'Expected: 'https://www.linkedin.com/company/sauce-labs/' in driver.current_url.lower() to be True")
    driver.close()
    driver.switch_to.window(original_window)