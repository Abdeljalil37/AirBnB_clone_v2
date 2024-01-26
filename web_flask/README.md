# AirBnB Clone v2

## Overview

AirBnB Clone v2 is a Flask-based web application that mimics the functionality of the popular Airbnb platform. This project is designed to showcase various features of web development, including routing, templates, and static files.

## Project Structure

The project is organized with the following directory structure:

- **templates**: Contains HTML templates for rendering web pages.
- **models/engine**: Includes engine-related models for handling data storage.
- **models**: Contains models for the application.
- **web_flask**: The main Flask application directory.
  - **templates**: Additional templates for specific routes.
  - **static**: Static files such as stylesheets or client-side scripts.

## Implemented Routes

1. **0-hello_route.py**: Basic route to demonstrate Flask setup.
2. **1-hbnb_route.py**: Route for the main page of the Airbnb Clone.
3. **2-c_route.py**: Route for displaying the letter 'C'.
4. **3-python_route.py**: Route for displaying the word 'Python'.
5. **4-number_route.py**: Route for handling numeric input.
6. **5-number_template.py**: Route and template for rendering numeric input.
7. **6-number_odd_or_even.py**: Route and template for determining if a number is odd or even.
8. **7-states_list.py**: Route for displaying a list of states.
9. **8-cities_by_states.py**: Route for displaying cities organized by states.
10. **9-states.py**: Route for displaying a list of states with a dynamic URL.
11. **10-hbnb_filters.py**: Route for displaying a page with filters for Airbnb listings.

## Model Files

- **models/engine/file_storage.py**: Implementation of file-based storage.
- **models/engine/db_storage.py**: Implementation of database storage.
- **models/state.py**: Model for representing states.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Abdeljalil37/AirBnB_clone_v2.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB_clone_v2
   ```

3. Install dependencies (assuming you have Python and pip installed):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python -m web_flask.0-hello_route
   ```

   Replace `0-hello_route` with the desired Python file to run the corresponding Flask application.
