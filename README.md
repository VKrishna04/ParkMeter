# ParkMeter: Parking Ticket Management System

**Description:**
A system designed to manage and track parking tickets, with features like payment processing, ticket history, and notifications.

---

## How to Run the Project:

1. Navigate to the project directory:
   ```bash
   cd ParkMeter
   ```

2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

3. Move to the application folder:
   ```bash
   cd parking_ticket_system
   ```

4. Create database migration files:
   ```bash
   python manage.py makemigrations
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

Access the project at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Administrative Access:

- **Username**: `admin`
- **Password**: `zqxwcevr1234`

---

## Project Structure:

- **`parking_ticket_system/`**: Main project directory containing `manage.py`.
- **Apps**:
  - **`tickets/`**: Manages ticket data (vehicle info, entry/exit times, etc.).
  - **`users/`**: Manages user accounts for system workers.
- **Settings and Config**:
  - `settings.py`, `urls.py`, etc.
- **Migrations**: Stored in each app's directory for database changes.

---

## Future Features and Improvements:

1. **Admin Interface**:
   - Register ticket models in the admin panel for ticket management.
   - Create a superuser to access the admin panel at `/admin/`.

2. **API Integration (Optional)**:
   - Integrate the Django REST framework for API interaction.

3. **Payment Processing (Optional)**:
   - Add Stripe or PayPal for handling payments.

4. **Notifications (Optional)**:
   - Implement email or SMS notifications for pending payments or violations.

---

## Security:

- Implement user authentication and authorization using Django's built-in mechanisms or third-party services (e.g., Auth0).

---

## Testing:

- Write unit tests for models and views to ensure application stability and functionality.