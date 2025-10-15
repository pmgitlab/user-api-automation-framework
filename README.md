# 🧪 Python API Automation Framework (MockAPI Demo)

This project demonstrates a simple yet powerful **Python-based API
Automation Framework** using `pytest`, `requests`, and `allure` for
reporting. It showcases a robust API automation framework built with Python and Pytest, focusing on **reusability, modular design, and detailed reporting.**.

------------------------------------------------------------------------

## 🚀 Features

-   Modular structure (test data, utilities, reports)
-   Uses **MockAPI.io** for User Management endpoints
-   Supports CRUD operations (GET, POST, PUT, DELETE)
-   Dynamic JSON payloads for test data
-   Beautiful Allure HTML Reports

------------------------------------------------------------------------

## 🏗️ Framework Structure

    api_automation/
    │
    ├── tests/
    │   ├── test_create_user.py
    │   ├── test_get_user.py
    │   ├── test_update_user.py
    │   └── test_delete_user.py
    │
    ├── utils/
    │   ├── api_client.py       # Handles API requests (GET, POST, PUT, DELETE)
    │   ├── test_data.json      # Input data (username, email, etc.)
    │   └── config.py           # Base URL for MockAPI
    │
    ├── reports/                # Allure reports stored here
    ├── requirements.txt        # Python dependencies
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 2️⃣ Run Tests

``` bash
pytest -v --alluredir=reports/
```

### 3️⃣ Generate HTML Report

``` bash
allure serve reports/
```

------------------------------------------------------------------------

## 🌐 API Base URL

> Using [MockAPI.io](https://mockapi.io)

Example:

    BASE_URL = "https://<your_project>.mockapi.io/api/v1/users"

------------------------------------------------------------------------

## 🧠 Sample Test Flow

1.  **Create User** → POST `/users`
2.  **Fetch User** → GET `/users/{id}`
3.  **Update User** → PUT `/users/{id}`
4.  **Delete User** → DELETE `/users/{id}`

Each step validates response codes, schema, and data consistency.

------------------------------------------------------------------------

## 🧩 Example Output

✅ Create User → 201\
✅ Get User → 200\
✅ Update User → 200\
✅ Delete User → 200

All results displayed beautifully in **Allure HTML report**.

------------------------------------------------------------------------

## 📤 Git Upload Guide (For New Users)

1.  Initialize Git

    ``` bash
    git init
    git add .
    git commit -m "Initial API Automation Framework"
    ```

2.  Create new repo on GitHub → Copy repo URL\

3.  Add remote and push

    ``` bash
    git remote add origin https://github.com/<username>/<repo-name>.git
    git branch -M main
    git push -u origin main
    ```

------------------------------------------------------------------------

## 👨‍💻 Author

**Prashant Makwana**\
Senior QA Engineer \| Automation Enthusiast\
🧰 Tools: Python, Pytest, Allure, Selenium, API Testing\
🌐 MockAPI project for assignment demonstration\
💼 https://www.linkedin.com/in/prashant-makwana-362aa872/
------------------------------------------------------------------------

## 💡 Notes

-   You can switch to **Mock REST API** anytime by updating `config.py`.
-   This framework is extendable for real-time API automation in
    production systems.

------------------------------------------------------------------------

## 💫 Contribution & Feedback
If you'd like to contribute, improve, or suggest new test scenarios, feel free to create a pull request or open an issue.  

⭐ **If you liked this framework, don't forget to star it on GitHub!**

---