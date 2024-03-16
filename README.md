# ParkMeter

Parking Ticket Management System: Develop a system for tracking and managing parking tickets, including features for payment processing, ticket history, and notifications.


# Commands to Run the Project Project
```pwsh
cd ParkMeter
venv\Scripts\activate
cd parking_ticket_system
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
There are a few scripts that are used to run the project. The first command is used to activate the virtual environment. The second command is used to navigate to the project directory. The third command is used to create the migration files. The fourth command is used to apply the migration files to the database. The fifth command is used to run the server.
The Project is now running on the local server. You can access the project by going to the following URL: http://127.0.0.1:8000/

The scripts in home directory are still work in progress.

# Credentials for First Administrative Accounts
* `UserName` - `admin`
* `password` - `zqxwcevr1234`

* When logging in you can observer a few logs which are purely for testing purpose and demonstrations.

# Project Structure:

`parking_ticket_system: Main` project directory containing manage.py.
`parking_ticket_system/ (subdirectory)`: Contains Django apps:
`tickets`: Manages ticket information (vehicle, phone number, license plate, entry/exit times).
`users`: Manages user accounts (workers) with basic authentication (username, password).
`parking_ticket_system/parking_ticket_system/`: Contains project-level settings and configuration:
`settings.py`
`urls.py` (optional for API endpoints if needed)
**Other directories and files**:
`migrations (inside each app)`: Stores database migration files (Django creates these).
`__init__.py (inside each app)`: An empty file to mark it as a Python package.


# Parking Ticket Management System: Detailed Roadmap

This document outlines a comprehensive roadmap for developing a parking ticket management system, catering to your college project requirements and incorporating a mock UPI-based payment process for India.

*1. System Design and Overview:*

* *Frontend:*
    * *Technologies:* ReactJS for a user-friendly and interactive interface.
    * *Components:*
        * Login/Signup for registered users and guest parking options.
        * Dashboard for viewing active parking sessions, ticket history, and managing payment methods.
        * Payment gateway integration for processing mock UPI payments.
        * Notification section for displaying alerts and reminders (parking expiration, violation notices).
* *Backend:*
    * *Technologies:* Python with Django framework for robust server-side logic and API development.
    * *API Endpoints:*
        * User authentication and management (register, login, update profile).
        * Parking management (initiate parking session, record vehicle details, calculate duration, generate ticket).
        * Payment processing (mock UPI integration, payment status updates).
        * Ticket history retrieval and display.
        * Notification generation and delivery (email, SMS).
* *Database:*
    * *Technology:* PostgreSQL for a scalable and reliable database solution.
    * *Tables:*
        * Users (stores user information, credentials, and preferences).
        * Parking sessions (tracks active parking details, vehicle info, entry/exit times, duration).
        * Tickets (stores generated ticket data, timestamps, status, payment details).
        * Payment transactions (records mock UPI transactions, amount, timestamp, status).

*2. Development Stages:*

*Stage 1: Frontend Development*

* Design user interface wireframes and mockups for each component.
* Implement the ReactJS application using appropriate UI libraries (e.g., Material-UI).
* Integrate mock payment gateway component for user interaction.
* Integrate notification display functionality.

*Stage 2: Backend Development*

* Set up Django project and configure database connection.
* Develop API endpoints for user management, parking operations, payment processing, and data retrieval.
* Implement mock UPI integration using a library like easypay or similar. This will simulate the UPI payment flow without actual connection to a payment gateway (remember, this is for educational purposes only).
* Develop logic for generating and managing parking tickets.
* Implement notification generation mechanism (e.g., using email libraries or APIs for SMS).

*Stage 3: Database Design and Implementation*

* Create database schema and tables as described in the system design section.
* Implement data models in Django using appropriate field types and relationships.
* Develop database migration scripts to manage schema changes.

*Stage 4: Integration and Testing*

* Connect the frontend and backend by integrating API calls within the React application.
* Implement user authentication and authorization logic.
* Test all functionalities thoroughly, including various scenarios like successful and failed payments, ticket expiration notifications, and user data management.

*5. Deployment and Maintenance*

* Choose a suitable hosting platform like Heroku or AWS for deployment(netlify or github pages).
* Configure the application and database for deployment environment.
* Implement a version control system (e.g., Git) for code management and future updates.
* Establish a maintenance plan for addressing bugs, adding new features, and updating dependencies.

*Note:* This roadmap provides a high-level overview. Each stage should be further broken down into smaller tasks and milestones during development.

*Additional Considerations:*

* *Security:* Implement robust security measures like user authentication, data encryption, and secure coding practices.
* *Scalability:* Design the system with scalability in mind to accommodate future growth and user base expansion.
* *Documentation:* Maintain clear and concise documentation for the system, including code comments, API references, and user guides.

This roadmap, alongside the mock UPI integration, should provide a solid foundation for developing your parking ticket management system as a college project. Remember to adapt and modify it according to your specific requirements and chosen technologies.


## This is our roadmap for backend
### Detailed Backend Development Roadmap for Parking Ticket Management System

This roadmap outlines the steps involved in developing the backend for your parking ticket management system using Python and Django:

*1. Project Setup and Environment:*

* *Install Python:* Ensure you have the latest version of Python installed on your system. Download and install from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
* *Install Django:* Use pip to install Django: pip install django.
* *Create Project:* Start a new Django project: `django-admin startproject parking_ticket_system`.
* *Create App:* Create a Django app for the core functionalities: `python manage.py startapp core`.
    - The command `python manage.py startapp core` creates a new Django app named "core" within your project directory. This app will hold the models, views, and other functionalities related to the core logic of your parking ticket management system.
* *Configure Settings:* Update the settings.py file in the main project directory to:
    * Specify database details (e.g., database engine, name, user, password).
    * Configure secret key for security.
    * Add core app to the INSTALLED_APPS list.
    - You'll need to update the settings.py file located in the main project directory.
    - This file holds various configurations for your project, including:
        - *Database details*: Specify the database connection information, such as engine (e.g., MySQL, PostgreSQL), name, username, and password. This allows Django to connect and interact with your chosen database to store data.
        - *Secret key*: Generate a strong, unique secret key using tools like django-utils-secrets.get_secret_key(). This key is crucial for various security features like user sessions and password encryption within your Django application.
        - *Installed Apps*: Update the INSTALLED_APPS list within settings.py to include your newly created app, "core". This tells Django to recognize and use the models and functionalities defined within the "core" app.

* *Run Migrations:* Initialize the database schema: `python manage.py makemigrations` followed by `python manage.py migrate`.
    - After defining your models (which will come later), you need to create the corresponding tables in the database. This is achieved through a two-step process:
    - `python manage.py makemigrations`: This command analyzes your models and generates migration files that describe the changes needed to the database schema.
    - `python manage.py migrate`: This command executes the generated migration files, creating (or modifying) the tables in your database based on your models' structure.

*2. User Management:*

* *Models:* Define a User model in models.py to store user information (email, password, etc.).
* *Authentication:* Integrate Django's built-in user authentication system using django.contrib.auth.
* *Serializers:* Create serializers in core/serializers.py to convert User objects to JSON and vice versa for API interactions.
* *Views:* Develop views in core/views.py for handling user registration, login, and profile management using relevant forms and authentication functionalities.
* *URLs:* Define URL patterns in parking_ticket_system/urls.py to map API endpoints to corresponding views (e.g., /users/register, /users/login).

*3. Parking Management:*

* *Models:* Define models in core/models.py for:
    * ParkingSession: Stores details like vehicle information, entry/exit times, duration, and associated user.
    * Ticket: Stores generated ticket data, timestamps, status (paid/unpaid), and associated parking session.
* *API Endpoints:* Create views in core/views.py for:
    * Initiating a parking session:
        * User provides vehicle details and desired parking duration.
        * System validates user and vehicle information.
        * Creates a new ParkingSession object and generates a corresponding Ticket object.
        * Returns API response with ticket details.
    * Recording vehicle exit:
        * User provides ticket ID or other identifier.
        * System fetches the ParkingSession and calculates final duration based on entry time.
        * Updates the ParkingSession with exit time and calculates the payable amount based on defined pricing logic.
        * Returns API response with updated ticket information and payable amount.

*4. Mock UPI Payment Processing:*

* *Mock Payment Library:* Install a library like easypay using `pip install easypay`. Remember, this is for educational purposes and doesn't involve actual payment processing.
* *Payment View:* Develop a view in core/views.py to handle mock UPI payments:
    * User provides UPI details within the API request.
    * Simulate a successful or failed payment using the chosen library's functionalities.
    * Update the Ticket object's status to "paid" upon successful payment.
    * Return API response with payment confirmation or error message.

*5. Notifications:*

* *Notification Model:* Consider defining a Notification model in core/models.py to store notification details (type, message, recipient, etc.).
* *Notification Logic:* Implement logic within views or separate tasks to generate notifications:
    * Upon ticket expiration or violation, create a Notification object with appropriate message.
    * Choose a notification delivery method (e.g., email or SMS APIs) and integrate it within the view or task.

*6. Testing and Deployment:*

* *Write Unit Tests:* Use a testing framework like pytest to write unit tests for your views, models, and serializers.
* *Integrate with Frontend:* Once backend functionalities are developed and tested, integrate API endpoints with your frontend application using appropriate methods (e.g., Axios for React).
* *Deployment:* Choose a suitable hosting platform like Heroku or AWS and follow their deployment instructions.

*Remember:* This roadmap provides a general structure. You may need to adapt and add functionalities based on your specific project requirements and chosen technologies.



**Frontend Development:**

* Choose a framework like React, Vue.js, or AngularJS to build the user interface, interacting with the Django backend through API calls.
* Design user-friendly interfaces for:
    * User registration, login, and profile management.
    * Initiating parking sessions, providing vehicle details, and displaying parking duration.
    * Recording vehicle exit, displaying payable amount, and initiating mock payments.
    * Viewing ticket history and receiving notifications.

**Database Management:**

* Consider using Django's built-in ORM (Object-Relational Mapper) to interact with the database and manage models efficiently.
* Define proper data types and constraints for model fields to ensure data integrity.

**Security:**

* Implement best practices for user authentication and authorization to prevent unauthorized access to sensitive information.
* Protect API endpoints from potential vulnerabilities like cross-site scripting (XSS) and SQL injection.

**Testing and Deployment:**

* Follow the roadmap's guidance on writing unit tests and integrating the backend with your frontend.
* Ensure proper testing and debugging of all functionalities before deployment.
* Choose a secure and reliable hosting platform following their specific deployment instructions.

**Additional Considerations:**

* As mentioned in the roadmap, the provided mock payment processing is for educational purposes only. Integrating real payment gateways requires careful consideration of security and compliance regulations.
* Explore advanced functionalities like automatic license plate recognition (ALPR) for vehicle identification if your project scope allows.

Remember, this is a general guideline, and you might need to adapt it based on your specific project requirements and chosen technologies. It's recommended to continuously research and explore relevant documentation and tutorials to enhance your project and address any specific challenges you encounter.


----------------

I apologize, I understand this is your Parking Ticket Management System project and I'm here to help you with the Django backend setup. Here's a basic structure to get you started:

**1. Project Setup:**

- Create a new Django project named `parking_ticket_system`:

```bash
django-admin startproject parking_ticket_system
```

- Navigate to the project directory:

```bash
cd parking_ticket_system
```

**2. Create a Django App:**

- Create a Django app named `tickets` to manage the parking ticket information:

```bash
python manage.py startapp tickets
```

**3. Define Ticket Model:**

- In the `tickets/models.py` file, define a model for `ParkingTicket`:

```python
from django.db import models

class ParkingTicket(models.Model):
    vehicle_registration_number = models.CharField(max_length=20, unique=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    parked_duration = models.DurationField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
```

**4. Additional Models (Optional):**

- Consider adding additional models if needed, such as:
    * `ParkingSlot` (to represent parking spaces and their availability)
    * `Payment` (to store details of completed payments)

**5. Create Admin Interface (Optional):**

- To manage tickets through the Django admin interface, register your models:

```python
# admin.py (in tickets app)
from django.contrib import admin
from .models import ParkingTicket

admin.site.register(ParkingTicket)
```

- Run `python manage.py createsuperuser` to create an admin user.
- Access the admin interface at `http://127.0.0.1:8000/admin/` (default URL, change if needed).

**6. Django REST Framework (Optional):**

- Consider using Django REST framework ([https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)) to create an API for interacting with your backend from your frontend (if applicable).

**7. Payment Processing (Optional):**

- Integrate a payment processing service like Stripe or PayPal if you want to handle online payments. Refer to their documentation for specific Django integrations.

**8. Notifications (Optional):**

- Implement notifications using email or SMS if needed to send alerts about pending payments, parking violations, etc. Use libraries like `django-allauth` or external services for sending emails and SMS.

**9. Security:**

- Implement proper authentication and authorization mechanisms to secure your application and user data. Use Django's built-in user authentication or integrate a third-party service like Auth0.

**10. Testing:**

- Write unit tests for your models and views to ensure their functionality.

**Remember:**

- This is a basic example and can be extended based on your specific requirements.
- Refer to the Django documentation and relevant libraries' documentation for detailed information and code examples.
- Explore additional features like integrating with parking sensors, license plate recognition, etc., if applicable to your project scope.

By following these steps and customizing them to your project's requirements, you can set up the backend for your parking ticket management system using Django.