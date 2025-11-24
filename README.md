# App Folder

This folder contains the core components of the application. Below is an overview of the files and their purposes:

## File Structure

```
app/
├── app.py          # Main application logic and routes
├── translate.py    # Translation utilities for handling i18n (internationalization)
├── __pycache__/    # Compiled Python files (auto-generated)
├── static/         # Static assets (CSS, JavaScript, images)
│   ├── i18n/       # JSON files for translations
│   │   └── en.json # Default English translations
│   ├── styles/     # CSS stylesheets
│   │   └── theme.css # Main theme stylesheet
├── templates/      # HTML templates for rendering views
│   ├── main.html   # Main page template
│   └── result.html # Result page template
```

## Files and Their Purpose

### `app.py`

- Contains the main application logic.
- Defines routes and handles HTTP requests.

### `translate.py`

- Provides utilities for handling translations.
- Loads JSON translation files and allows dynamic translation of keys.

### `static/`

- Contains static assets such as CSS, JavaScript, and images.
- **`i18n/`**: Stores JSON files for translations (e.g., `en.json` for English).
- **`styles/`**: Contains CSS files for styling the application.

### `templates/`

- Contains HTML templates for rendering views.
- **`main.html`**: Template for the main page.
- **`result.html`**: Template for displaying results.

## How to Use

1. **Run the Application**:

   - Ensure you have Python installed.
   - Navigate to the `app` folder and run the application using:
     ```bash
     python app.py
     ```

2. **Add Translations**:

   - Add new JSON files in the `static/i18n/` folder for additional languages.
   - Use the `translate.py` utility to dynamically fetch translations.

3. **Modify Templates**:

   - Update or add new HTML templates in the `templates/` folder.

4. **Customize Styles**:
   - Modify the CSS files in `static/styles/` to change the application's appearance.

## Notes

- Ensure all translation files are valid JSON.
- The `__pycache__/` folder is auto-generated and can be ignored.

## License

This project is licensed under the MIT License.
