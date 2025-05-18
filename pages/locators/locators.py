from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")




class ProductsPageLocators:
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@class='inventory_item_desc']")
    BACKPACK_IMAGE = (By.CLASS_NAME, "inventory_details_img")
    SECONDARY_HEADER = (By.CLASS_NAME, "header_secondary_container")
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    HEADER_CONTAINER = (By.CLASS_NAME, "header_container")




class CartPageLocators:
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    DESCRIPTION_HEADER = (By.CLASS_NAME, "cart_desc_label")
    QTY_HEADER = (By.CLASS_NAME, "cart_quantity_label")
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@class='inventory_item_desc']")
    SECONDARY_HEADER = (By.CLASS_NAME, "header_secondary_container")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.XPATH, "//*[@class='cart_item']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name")




class CheckoutPageLocators:
    SECONDARY_HEADER = (By.CLASS_NAME, "header_secondary_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    DISPLAYED_POSTAL_CODE = (By.ID, "postal-code")
    DISPLAYED_LAST_NAME = (By.ID, "last-name")
    DISPLAYED_FIRST_NAME = (By.CLASS_NAME, "first-name")
    FINISH_BUTTON = (By.CLASS_NAME, "btn btn_action btn_medium cart_button")
    ERROR_MESSAGE = (By.CLASS_NAME, "checkout_info")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    CANCEL_BUTTON = (By.ID, "cancel")
    MENU_PANEL = (By.CLASS_NAME, "bm-burger-button")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")




class CheckoutOverviewPageLocators:
    ORDER_CONFIRMATION_TEXT = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PAYMENT_INFO = (By.XPATH, "//div[@class='summary_info']//div[contains(text(),'SauceCard')]")
    SHIPPING_INFO = (By.XPATH, "//div[@class='summary_info']//div[contains(text(),'Free Pony')]")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")




class BasePageLocators:
    MENU_CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")
    MENU_PANEL = (By.CLASS_NAME, "bm-burger-button")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    EXPECTED_MENU_OPTIONS = ["All Items", "About", "Logout", "Reset App State"]
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    HEADER_CONTAINER = (By.CLASS_NAME, "header_container")







