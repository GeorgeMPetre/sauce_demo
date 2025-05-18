import os
import uuid
from pytest_html import extras
from datetime import datetime
import pytest_html


class SoftAssert:
    def __init__(self, driver, request):
        self._infos = []
        self._errors = []
        self.driver = driver
        self.request = request
        self.screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(self.screenshot_dir, exist_ok=True)


    def _capture_screenshot(self, label):
        try:
            current_node = self.request.node
        except Exception:
            return None
        if not hasattr(current_node, "extra"):
            current_node.extra = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{label}_{timestamp}_{uuid.uuid4().hex[:6]}.png"
        path = os.path.join(self.screenshot_dir, filename)
        self.driver.save_screenshot(path)
        current_node.extra.append(pytest_html.extras.image(path))
        return path


    def assert_equal(self, actual, expected, message=""):
        try:
            assert actual == expected, message
            print(f"PASS: {message}")
        except AssertionError as e:
            path = self._capture_screenshot("assert_equal_fail")
            error_msg = f"[ASSERT_EQUAL FAIL] {str(e)}"
            self._errors.append((error_msg, path))


    def assert_true(self, condition, message=""):
        try:
            assert condition, message
            print(f"PASS: {message}")
        except AssertionError as e:
            path = self._capture_screenshot("assert_true_fail")
            error_msg = f"[ASSERT_TRUE FAIL] {str(e)}"
            self._errors.append((error_msg, path))


    def assert_false(self, condition, message=""):
        try:
            assert not condition, message or "Expected condition to be False"
            print(f"PASS: {message or 'Expected condition to be False'}")
        except AssertionError as e:
            path = self._capture_screenshot("assert_false_fail")
            error_msg = f"[ASSERT_FALSE FAIL] {str(e)}"
            self._errors.append((error_msg, path))

    def assert_info(self, *args):
        if len(args) == 1:
            condition = True
            message = args[0]
        elif len(args) == 2:
            condition, message = args
        else:
            raise TypeError("assert_info() takes 1 or 2 arguments (condition, message)")

        #print(f"[INFO] {message}")  # Always print the message

        if condition:
            path = self._capture_screenshot("info")
            info_msg = f"[INFO] {message}"
            self._infos.append((info_msg, path))



    def assert_in(self, member, container, message=""):
        try:
            assert member in container, message
            print(f"[PASS] {message}")
        except AssertionError as e:
            print(f"[FAIL] {message}")
            self._errors.append(str(e))

    def assert_all(self):
        for msg, path in self._infos:
            print(f"{msg}\nScreenshot: {path}")
        if self._errors:
            error_details = "\n\n".join(msg for msg, _ in self._errors)
            raise AssertionError("Soft assertion errors occurred:\n\n" + error_details)

