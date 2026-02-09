# Store Management System

A comprehensive Store Management System built with Python and MySQL, designed to streamline inventory tracking, sales management, and data analysis for retail businesses.

## Features

- **Purchase Management**: Record and view purchase details for Gold, Diamond, and Alloy.
- **Raw Material Tracking**: Manage 18K Gold stock and alloy usage.
- **Issue Tracking**: Monitor materials issued to labor/artisans.
- **Manufacturing Data**: Record manufactured items and update stock automatically.
- **Stock Management**: Real-time tracking of Gold and Diamond stock with visual charts.
- **Customer Sales**: Process customer sales and generate bills.
- **Data Backup & Restore**: Securely backup and restore data using CSV files.
- **Visual Analytics**: Interactive pie charts for Gold, Diamond, and Alloy distribution.

## Prerequisites

- Python 3.x
- MySQL Server

## Dependencies

Install the required Python libraries:

```bash
pip install mysql-connector-python matplotlib tabulate
```

## Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd Store-Management-System
    ```

2.  **Database Setup**
    The system includes a script to set up the necessary database and tables.
    
    > [!IMPORTANT]
    > The default MySQL credentials are set to `user="root"` and `password="hello!123"`. 
    > You may need to update these credentials in `Backup/db.py`, `Login.py`, and `Menu.py` to match your local MySQL configuration.

    Run the setup script:
    ```bash
    python Backup/db.py
    ```

## Usage

1.  **Start the Application**
    ```bash
    python Main.py
    ```

2.  **Login**
    Use the default credentials to log in:
    - User ID: `sumit4183`
    - Password: `sp4183`
    
    *(Alternative credentials: `varad4180` / `vk4180`)*

3.  **Navigate the Menu**
    Follow the on-screen prompts to manage purchases, stock, sales, and generate reports.

## Project Structure

- `Main.py`: Entry point of the application handling user authentication.
- `Menu.py`: Core logic containing all feature modules (Purchase, Stock, Sales, etc.).
- `Login.py`: Handles database connection for login verification.
- `Backup/`: Contains the database setup script (`db.py`) and backup CSV files.

---

## 👤 Author

**Sumit Patel**
*   [LinkedIn](https://linkedin.com/in/sumit4183)
*   [GitHub](https://github.com/sumit4183)
*   [Portfolio](https://sumitp.netlify.app)