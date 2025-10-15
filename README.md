# User API Automation Framework

## Overview
This framework automates testing of a User Management API using Python, Pytest, and Allure.

## Tech Stack
- Python
- Pytest
- Requests
- Allure Reports
- Faker (for fake test data)

## Directory Structure
Refer to the structure in this repo.

## How to Run
```bash
pytest --alluredir=reports
allure serve reports
```

## Multi-Environment
Modify `config/environment.yaml` to switch between test/staging environments.


---

## 🎯 **Step 11 — Run the Tests**

```bash
# Activate environment
venv\Scripts\activate

# Run pytest
pytest --alluredir=reports

# View allure report
allure serve reports
