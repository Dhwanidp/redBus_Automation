redBus Automation Framework (Selenium + Python + Pytest)

This project automates the redBus train search flow using Python, Selenium, Pytest, the Page Object Model (POM), and JSON-driven test data. It performs JSON-driven source/destination selection, dynamic date selection, cancellation fee validation, applies a filter, and prints top auto-suggestions from the results. The framework includes HTML reporting and screenshot capture on failure.

Tech Stack

Python
Selenium WebDriver
Pytest
Page Object Model (POM)
JSON-based Test Data
Pytest HTML Reporting
Screenshot Capture on Failures
WebDriver Manager / Browser Drivers

Supported Browsers

Chrome
Edge
Firefox

Choose the browser at runtime using:
--browser_name=edge

If no browser is provided, Chrome is the default.

Test Scenarios Automated

1. JSON-Driven Train Search
   Reads source, destination, and date from test_data.json, selects them in the UI, and handles station auto-suggestions.

2. Cancellation Fee Validation
   Reads expected cancellation information from JSON and validates the displayed cancellation or free-cancellation messages.

3. Filter Application and Suggestions
   Applies a filter (class/type), verifies updated results, and prints top auto-suggestions or top search summaries.

4. Calendar and Date Selection
   Selects journey date dynamically from the calendar and handles month navigation and basic validations.

5. POM + Pytest Structure
   Uses Page Object Model classes and pytest fixtures for setup, teardown, and reusable utilities.

How to Run the Tests

python -m pytest redbus_Automation/Tests/test_trains_search.py --browser_name=edge --html=reports/report.html --self-contained-html -q -vv

Explanation:
--browser_name=edge : choose browser (chrome/edge/firefox)
--html=reports/report.html : generate HTML report
--self-contained-html : single-file HTML report
-q -vv : quiet mode with verbose logs

Project Highlights

JSON-driven route, date, and cancellation data
Clean Page Object Model structure
Dynamic waits and reusable utility functions
Filter application and printed suggestions for quick verification
HTML reports with screenshots for failures
Easy to extend for more scenarios and validations
