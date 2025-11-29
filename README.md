**redBus Automation Framework (Selenium + Python + Pytest)**

This project automates the redBus Train Search flow using
Python, Selenium, Pytest, the Page Object Model (POM), and JSON-based test data.

The framework covers the complete search process:
Landing Page → Trains Module → Source & Destination → Date Selection → Filter → Suggestions,
with data-driven inputs and validations at each step.

---

**Tech Stack**

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* JSON-based Test Data
* HTML Test Reporting (pytest-html)
* Screenshot Capture on Failures

---

**Supported Browsers**

The test framework supports running tests on the following browsers:

* Chrome
* Edge
* Firefox

Choose the browser at runtime using:

```
--browser_name=edge
```

If no browser is provided, Chrome is the default.

---

**Test Scenarios Automated**

**1. JSON-Driven Train Search**

Reads train search data from `test_data.json`:

* Loads source station from JSON
* Loads destination station from JSON
* Loads and selects journey date from JSON
* Handles auto-suggestions and selects correct station

---

**2. Cancellation Fee Validation**

Uses values from JSON to validate:

* Cancellation fee
* Free cancellation message (if applicable)
* UI text matched with expected JSON data

---

**3. Filter Application and Suggestions**

* Applies a train/class filter
* Ensures results update
* Prints top suggestions or result summaries for verification

---

**4. Calendar & Date Selection**

* Handles dynamic date picker
* Navigates months if required
* Selects JSON-driven date correctly

---

**5. Framework Structure (POM + Pytest)**

* Uses Page Object Model for clean separation
* Reusable pytest fixtures for setup and teardown
* Utilities for waits, element handling, and browser management

---

**How to Run the Tests**

Run the main test with HTML reporting:

```
python -m pytest redbus_Automation/Tests/test_trains_search.py --browser_name=edge --html=reports/report.html --self-contained-html -q -vv
```

Explanation:

* `--browser_name=edge` : choose browser (chrome / edge / firefox)
* `--html=reports/report.html` : generate HTML test report
* `--self-contained-html` : create a single-file report
* `-q -vv` : quiet mode + verbose logs

---

**Project Highlights**

* JSON-driven source, destination, date, and cancellation data
* Clean and maintainable POM structure
* Dynamic waits for stable execution
* Filter handling and auto-suggestion printing
* HTML reports with screenshots on failure
* Simple, scalable, and ready to extend

Suggestions and improvements are welcome.
