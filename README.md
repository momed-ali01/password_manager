# Password Manager

A secure password management application built with Python, available in both GUI and CLI versions. This application helps you store, generate, and manage your passwords in a safe and organized way.

## Features

### GUI Version

- Generate strong, random passwords
- Store website credentials securely
- Search for saved passwords
- Automatic password copying to clipboard
- User-friendly graphical interface
- JSON-based secure storage
- Input validation and error handling

### CLI Version

- Simple command-line interface
- Add new passwords
- View saved passwords
- Text-based storage
- Easy to use in terminal

## Requirements

- Python 3.x
- pyperclip==1.9.0 (for GUI version)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/password_manager.git
cd password_manager
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate # On Windows
source venv/bin/activate # On macOS/Linux
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### GUI Version

Run the GUI application:

```bash
python password_manager_gui.py
```

### CLI Version

Run the command-line application:

```bash
python password_manager_cli.py
```

### Features in Detail

#### GUI Version

1. **Password Generation**
   - Generates 12-character strong passwords
   - Includes uppercase letters, lowercase letters, numbers, and special characters
   - Automatically copies generated password to clipboard

2. **Password Storage**
   - Securely stores website credentials
   - Saves data in JSON format
   - Includes website name, email/username, and password

3. **Password Search**
   - Quick search functionality for saved passwords
   - Displays email and password for the requested website
   - Case-insensitive search

4. **User Interface**
   - Clean and intuitive GUI
   - Input validation
   - Error messages for invalid inputs
   - Default email field for convenience

#### CLI Version

1. **Simple Commands**
   - Type 'add' to add a new password
   - Type 'view' to see existing passwords
   - Type 'q' to quit

2. **Password Storage**
   - Stores passwords in a simple text file
   - Easy to read and modify manually if needed

## Data Storage

### GUI Version

The application stores all passwords and credentials in a `data.json` file. The data is stored in the following format:

```json
{
  "Website": {
    "email": "user@example.com",
    "password": "generated_password"
  }
}
```

### CLI Version

The application stores passwords in a `passwords.txt` file in the format:

```
username|password
```

## Security Features

- Input validation to prevent empty submissions
- Strong password generation (GUI version)
- No plain text password display in the interface (GUI version)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is for educational purposes.
