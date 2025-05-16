# 🧪 SauceDemo Test Automation Suite

This repository contains a comprehensive **data-driven test automation project** for [SauceDemo](https://www.saucedemo.com), built entirely from scratch with **no available documentation**. The suite covers the entire application—from login to checkout confirmation—across multiple user profiles, browsers, and defect conditions.

---

## 🚀 Project Overview

- **Framework**: `pytest` + `Selenium WebDriver`
- **Language**: `Python 3.12`
- **Testing Approach**: Black-box and exploratory
- **Design Pattern**: Page Object Model (POM)
- **Assertions**: Custom soft assertion handler with screenshot capture
- **Execution**: Supports multi-browser and parallel execution
- **Reporting**: HTML reports, screenshot evidence, and Xray/Jira integration

---

## ✅ Scope & Coverage

| Area                  | Included Tests                                                |
|-----------------------|---------------------------------------------------------------|
| Login                 | ✔️ Positive, Negative, Performance, UI                         |
| Product Inventory     | ✔️ Display, Sorting, UI Defects                                |
| Cart Functionality    | ✔️ Add/Remove, UI, Navigation, Reset                           |
| Checkout: Info        | ✔️ Field Validation, UI Alignment, Navigation                  |
| Checkout: Overview    | ✔️ Price Validation, Completion, Cancel                        |
| Cross-page Components | ✔️ Headers, Footers, Social Links                              |
| User Roles Tested     | ✔️ `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user` |

> 🔎 **Test Plan Strategy**  
> The strategy follows a **header-to-footer validation** approach using **black-box testing** techniques. It emphasizes thorough exploratory testing to detect UI inconsistencies, performance bottlenecks, functional bugs, and unexpected corner-case behavior across all user types and defect scenarios.

---

## 📊 Test Coverage Estimate

- **Estimated Coverage**: **92–95%**
  - Functional correctness
  - UI layout and visibility
  - Performance thresholds (e.g., logout time, button delays)
  - Known defect validation
  - Positive and negative equivalence partitioning
  - Data-bound validation across edge-case user types

---

## 🧬 Data-Driven Execution

This test suite is fully parameterized and dynamically loads user credentials to simulate:

- Varied authentication roles (positive, blocked, buggy users)
- Role-specific execution paths
- Scenario branching with soft assertion logs

---

## 🛠️ Installation & Execution

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/saucedemo-test-suite.git
cd saucedemo-test-suite

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the full test suite with HTML report
pytest --html=reports/report.html --self-contained-html

# 5. Run specific groups using markers
pytest -m "regression"



📁 Project Structure
├── pages/                 # Page Object Models
├── tests/                 # Test files grouped by feature
├── utils/                 # SoftAssert, data loader, configs
├── reports/               # HTML test reports & screenshots
├── requirements.txt
└── pytest.ini


🧾 Jira & Xray Integration
Each test is mapped to a unique Xray test case ID (e.g., TEST-101) and follows a consistent tagging pattern. This allows seamless integration with Jira/Xray for test management, traceability, and coverage reporting.

📷 Reports & Evidence
All failures and info-level checkpoints are logged via the custom SoftAssert class.
Screenshots are automatically captured for both failures and logged assert_info() calls.
HTML reports are saved under the /reports directory.

🔖 Useful Pytest Markers
@pytest.mark.functional
@pytest.mark.ui
@pytest.mark.performance
@pytest.mark.regression
Feature-specific: @pytest.mark.cart, @pytest.mark.checkout, @pytest.mark.overview
User-specific: @pytest.mark.negative, @pytest.mark.e2e

👤 Author
George Petre
📍 Sturry, UK
📧 george.petre23@gmail.com
🌐 Portfolio


📌 Notes
Designed entirely from scratch with no functional documentation.
Strategy based on exploratory testing and black-box validation.
Known defects are purposefully validated and clearly marked in test logs.
Built for portfolio showcasing and real-world QA process emulation.

📄 License
This project is available for educational and demonstration purposes.
Attribution is appreciated but not required.
