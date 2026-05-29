Model Risk Management System

--------------------------------------------------

📌 Project Description:
This project is a Model Risk Management System that allows users to register models and manage them through a centralized inventory.

The system captures key model attributes, generates a unique Model ID, and displays all registered models in a structured grid format.

--------------------------------------------------

🎯 Objective:
To implement a system where users can:
- Register new models with required details
- Automatically generate unique Model IDs
- View all models in a centralized inventory

--------------------------------------------------

⚙️ Features:

✅ Model Registration
- Capture model details such as:
  - Model Name
  - Model Version
  - Model Sponsor
  - Business Line
  - Model Type (Fraud Model / Risk Model)
  - Risk Rating (High / Medium / Low)
  - Status (Development / Production / etc.)

✅ Automatic Model ID Generation
- Each model is assigned a unique ID
- Format: MODEL-1, MODEL-2, MODEL-3, etc.

✅ Model Inventory Dashboard
- Displays all registered models in a table format
- Includes all model attributes in separate columns
- Provides a centralized view of all models

✅ User-Friendly Interface
- Web-based UI using Flask and HTML/CSS
- Clean and interactive forms for easy input

--------------------------------------------------

🏗️ Technologies Used:

- Python
- Flask (Backend & Web Framework)
- HTML
- CSS
- JSON (for data storage)

--------------------------------------------------

📂 Project Structure:

project/
│
├── web_app.py          → Main Flask application
├── model_registry.py   → Backend logic for storing models
├── models.json         → Data storage file
│
└── templates/
    ├── register.html    → Model Registration UI
    └── inventory.html   → Model Inventory UI

--------------------------------------------------

▶️ How to Run:

1. Open terminal
2. Navigate to project folder
3. Run command:

   python web_app.py

4. Open browser and go to:

   http://127.0.0.1:5000/

--------------------------------------------------

🧠 System Workflow:

Register Model → Store Data → Generate ID → Display in Inventory

--------------------------------------------------

📊 Example:

MODEL-1 → Fraud Detection Model → Risk Management → High → Production  
MODEL-2 → Risk Assessment Model → Risk Management → Medium → Development  

--------------------------------------------------

📌 Notes:

- The system is rule-based and focuses on model management
- Fraud Model and Risk Model are used as sample model types
- Data is stored locally using JSON file

--------------------------------------------------

🚀 Future Enhancements:

- Add database integration (MySQL / SQLite)
- Add search and filter functionality in inventory
- Add model update and delete features
- Improve UI with dashboard analytics

--------------------------------------------------

👩‍💻 Developed By:
Khushi Wadhwa
