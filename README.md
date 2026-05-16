# Vehicle Maintenance SchedulerA Flask-based full stack web application developed for vehicle maintenance scheduling and depot management.  The system integrates external APIs, backend scheduling logic, logging middleware, and a responsive dashboard UI.---## Features- Vehicle maintenance scheduling dashboard- Depot data integration using external APIs- Backend optimization calculations- Logging middleware implementation- Dynamic Flask routing- Responsive multi-page UI- Maintenance tracking system- Vehicle status monitoring- Schedule analytics display---## Tech Stack### Backend- Python- Flask- REST API Integration- Requests Library### Frontend- HTML5- CSS3- Jinja Templates### Tools & Utilities- Git & GitHub- Virtual Environment (venv)- dotenv- Logging Middleware---## Project Structure```bash22MIA1176/│├── logging_middleware/│   ├── config.py│   ├── logger.py│   └── test_logger.py│├── vehicle_maintenance_scheduler/│   ├── routes/│   ├── services/│   ├── static/│   ├── templates/│   ├── utils/│   └── app.py│├── .env├── requirements.txt└── notification_system_design.md

Functional Modules
Dashboard
Displays maintenance overview and depot insights.
Schedule Management
Calculates maintenance hours and impact levels for vehicles.
Vehicle Management
Tracks vehicle availability and maintenance status.
Maintenance Logs
Maintains maintenance activity records and logs.
Logging Middleware
Captures and manages backend API logs.

API Integration
The application integrates depot APIs to:


Fetch depot details


Calculate maintenance allocations


Process scheduling information dynamically



Installation
Clone Repository
git clone https://github.com/devveldev-sketch/22MIA1176.git
Navigate to Project
cd 22MIA1176
Create Virtual Environment
python3 -m venv venv
Activate Virtual Environment
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Application
python app.py

Future Enhancements


Database integration


Authentication system


Real-time notifications


Advanced optimization algorithms


Interactive charts and analytics


Cloud deployment



Author
Devadharshini S
Integrated M.Tech CSE (Business Analytics)
VIT Chennai

License
This project is developed for educational and academic purposes.
