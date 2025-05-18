import time
import pytest
from utils.data_loader import (
    load_all_users_for_login_only, load_active_users_for_full_tests)






# ------------------ LOGIN TESTS ------------------

# Xray: TEST-01
@pytest.mark.login
@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.validation
@pytest.mark.regression
@pytest.mark.regression_login
@pytest.mark.parametrize("username, password, expected_error", [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secr", "Epic sadface: Username is required"),
    ("   ", "   ", "Epic sadface: Username is required"),
    ("standard_user ", "secr", "Epic sadface: Username and password do not match any user in this service"),
    ("STANDARD_USER", "secr", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "wrongpass", "Epic sadface: Username and password do not match any user in this service"),
])

def test_login_field_validations(setup, username, password, expected_error, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    actual_error = login_page.get_error_message()
    if username != "" and username.strip() == "" and password.strip() == "":
        soft_assert.assert_info(
            True,
            "Whitespace-only inputs may be mishandled — visually empty but not technically empty. "
            f"Expected: '{expected_error}', got: '{actual_error}'"
        )
    soft_assert.assert_true(
        expected_error in actual_error,
        f"Expected: '{expected_error}', Got: '{actual_error}'"
    )



# Xray: TEST-02
@pytest.mark.login
@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.regression_login
@pytest.mark.parametrize("username, password", load_all_users_for_login_only())
def test_login_functionality(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    login_page.login(username, password)
    if username == "locked_out_user":
        soft_assert.assert_true(
            "inventory.html" not in driver.current_url,
            f"Expected: 'locked_out_user' should not access inventory page."
        )
        soft_assert.assert_info(f"'locked_out_user' is expected to be locked out (login fails).")
    elif username == "invalid_user":
        soft_assert.assert_true(
            "inventory.html" not in driver.current_url,
            f"Expected: login to fail for 'invalid_user'."
        )
    else:
        soft_assert.assert_true(
            "inventory.html" in driver.current_url,
            f"Expected: successful login for '{username}'."
        )




# Xray: TEST-03
@pytest.mark.login
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.regression_login
@pytest.mark.parametrize("username, password", load_active_users_for_full_tests())
def test_login_performance(setup, username, password, driver):
    driver, soft_assert, login_page = setup
    start_time = time.time()
    login_page.login(username, password)
    end_time = time.time()
    login_duration = end_time - start_time
    if username == "performance_glitch_user":
        soft_assert.assert_true(
            login_duration > 5,
            f"Expected: login time > 5 seconds for '{username}', got {login_duration:.2f} seconds."
        )
        soft_assert.assert_info(f"User '{username}' experienced intentional performance delay.")
    else:
        soft_assert.assert_true(
            login_duration <= 2,
            f"Expected: login time <= 2 seconds for user '{username}', got {login_duration:.2f} seconds."
        )



