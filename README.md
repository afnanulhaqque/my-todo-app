# Flask Todo Application

A simple and elegant Todo application built with Flask, SQLAlchemy, and Bootstrap. This application allows you to create, read, update, and delete todos with a clean and intuitive web interface.

## Features

- ✅ **Create Todos**: Add new todos with a title and description
- 📝 **Update Todos**: Edit existing todos
- 🗑️ **Delete Todos**: Remove todos you no longer need
- 📋 **View All Todos**: See all your todos in a table format
- ⏰ **Timestamp Tracking**: Each todo includes a creation timestamp
- 🎨 **Modern UI**: Built with Bootstrap for a responsive and clean design

## Technologies Used

- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database
- **Bootstrap** - Frontend framework for styling
- **Jinja2** - Template engine

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd flask
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and navigate to `http://localhost:8000`

## Usage

### Adding a Todo

1. Navigate to the home page (`/`)
2. Fill in the "Todo Title" and "Todo Description" fields
3. Click the "Submit" button

### Updating a Todo

1. Find the todo you want to update in the todos table
2. Click the "Update" button next to the todo
3. Modify the title and/or description
4. Click the "Update" button to save changes

### Deleting a Todo

1. Find the todo you want to delete in the todos table
2. Click the "Delete" button next to the todo
3. The todo will be permanently removed

## Project Structure

```
flask/
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── todo.db               # SQLite database (created automatically)
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page template
│   ├── update.html       # Update todo template
│   └── about.html        # About page template
└── myenv/                # Virtual environment (not tracked in git)
```

## API Routes

- `GET /` - Home page displaying all todos and add todo form
- `POST /submit` - Create a new todo
- `GET /update/<Sr_No>` - Display update form for a specific todo
- `POST /update/<Sr_No>` - Update an existing todo
- `GET /delete/<Sr_No>` - Delete a todo
- `GET /about` - About page

## Database Schema

The `Todo` model has the following fields:

- `Sr_No` (Integer, Primary Key) - Serial number/ID
- `title` (String, 200 chars) - Todo title
- `desc` (String, 500 chars) - Todo description
- `date_created` (DateTime) - Creation timestamp

## Deployment

You can deploy this Flask application to various platforms like Heroku, Railway, Render, or AWS. Each platform has its own deployment process, so refer to their respective Flask deployment guides for detailed instructions.

Common deployment steps typically include:
1. Setting up a production WSGI server (like Gunicorn)
2. Configuring environment variables
3. Setting up the database
4. Configuring the platform's deployment settings

## Development

The application runs in debug mode by default on port 8000. To modify the port or other settings, edit the `app.run()` call in `app.py`.

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

