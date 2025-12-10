# ✅ Python Script QA Utilities

This repository contains small but highly useful **Python automation utilities for QA workflows**.  
These scripts help with **test data preparation, log validation, and cleanup automation**, commonly used in manual and automation testing environments.

---

## 📁 Project Structure
```
QA-Automation-Utilities/
│
├── csv_to_json.py # Convert test data from CSV to JSON
├── log_reader.py # Read logs & highlight failures
├── folder_cleanup.py # Clean temp/log files after test execution
└── README.md

yaml
Copy code
```
---

## 🛠️ Scripts Overview

### ✅ 1. csv_to_json.py
Converts test data from CSV file into JSON format.

📌 **Used for:**
- Data-driven automation testing
- Converting Excel/CSV to JSON
- API testing payload prep

▶️ **Run:**
```bash
python csv_to_json.py
📄 Example Output:

pgsql
Copy code
✅ CSV successfully converted to JSON
✅ 2. log_reader.py
Reads application/system logs and displays only error or failure lines.

📌 Used for:

Post-test log validation

Debugging failed test executions

Monitoring system errors

▶️ Run:

bash
Copy code
python log_reader.py
📄 Example Output:

vbnet
Copy code
🔍 Error Lines Found:

ERROR: Login failed for user admin
FAIL: Payment gateway timeout
✅ 3. folder_cleanup.py
Deletes temporary .tmp and .log files after test execution.

📌 Used for:

Automation result cleanup

Test workspace hygiene

Preventing log accumulation

▶️ Run:

bash
Copy code
python folder_cleanup.py
📄 Example Output:

Copy code
✅ Cleanup complete. Deleted 5 files.
🧪 Skills Demonstrated
Python automation

QA utility scripting

Log analysis

File handling

Data-driven testing support

Automation hygiene

🎯 Purpose of This Project
This project shows my ability to:

Write practical QA automation utilities

Support manual & automated testing workflows

Handle test data, logs, and execution artifacts

Think like a QA Automation Engineer

👤 Author
Harsh Bansal
GitHub: https://github.com/harshbansal95623
