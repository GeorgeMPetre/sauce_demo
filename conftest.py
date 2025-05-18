import datetime
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pytest_html import extras




BLOCKED_USERS = ["locked_out_user", "invalid_user"]
REPORT_DIR = os.path.join(os.getcwd(), "reports")
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)



@pytest.fixture
def setup(driver, request):
    from utils.soft_assert import SoftAssert
    from pages.page_login import LoginPage
    soft_assert = SoftAssert(driver, request)
    request.node.soft_assert = soft_assert
    login_page = LoginPage(driver)
    yield driver, soft_assert, login_page




@pytest.fixture
def driver(request):
    browser_name = request.param or "chrome"
    print(f"\nLaunching browser: {browser_name}")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.startup.homepage", "about:blank")
        options.set_preference("startup.homepage_welcome_url", "about:blank")
        options.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(1920, 1080)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()




@pytest.fixture
def skip_if_blocked_user(request):
    username = request.param if hasattr(request, "param") else request.getfixturevalue("username")
    if username in BLOCKED_USERS:
        pytest.skip(f"Skipping post-login steps for blocked user: '{username}'")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="append",
        help="Browser(s) to run tests on. Example: --browser=chrome --browser=edge"
    )



def pytest_generate_tests(metafunc):
    browsers = metafunc.config.getoption("browser")
    if not browsers:
        browsers = ["chrome"]
    metafunc.parametrize("driver", browsers, indirect=True)


def _capture_screenshot(self, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    self.driver.save_screenshot(screenshot_path)
    return screenshot_path


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.extras = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    sa = getattr(item, "soft_assert", None)
    if not hasattr(report, "extras"):
        report.extras = []
    if sa:
        for msg, path in sa._infos:
            if path and os.path.exists(path):
                rel_path = os.path.relpath(path, start=os.path.dirname(report.location[0]))
                report.sections.append(("Soft Assertion Info", msg))
                report.extras.append(extras.image(rel_path))
        if call.when == "call":
            try:
                sa.assert_all()
            except AssertionError as e:
                report.outcome = "failed"
                report.longrepr = str(e)
                for msg, path in sa._errors:
                    if path and os.path.exists(path):
                        rel_path = os.path.relpath(path, start=os.path.dirname(report.location[0]))
                        report.extras.append(extras.image(rel_path))


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "SauceDemo Test Report with Screenshots"


@pytest.hookimpl
def pytest_configure(config):
    config.option.htmlpath = os.path.join(REPORT_DIR, "report.html")
