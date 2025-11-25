# KickStarter

This folder contains the core components of the application. Below is an overview of the files and their purposes:

## File Structure

```
main.ipynb          # Data processing and modeling
app/
├── app.py          # Main application logic and routes
├── translate.py    # Translation utilities for handling i18n (internationalization)
├── static/
│   ├── i18n/
│   │   └── en.json # JSON files for translations
│   ├── styles/
│   │   └── theme.css # Main theme stylesheet
├── templates/
│   ├── main.html   # Main page template
│   └── result.html # Result page template
```

## Getting Started

1. **Dependencies**:

   - Ensure you have Python installed (Python 3.13.x is used to run this app)
   - `git clone https://github.com/Duahau1/CS533-course-project.git` to clone the repo
   - Download the dataset from `https://s3.amazonaws.com/weruns/forfun/Kickstarter/Kickstarter_2025-11-12T12_09_07_111Z.zip` or you can go to `https://webrobots.io/kickstarter-datasets/` and download any CSV file you like.
   - Go to `main.ipynb` and make sure in the first code block change the name of the folder that you want to merge.
   - Create a virtual environment and activate the env using the following command `mkdir ./.venv && python3 -m venv ./.venv && source ./.venv/bin/activate`
   - `pip install -r requirements.txt` to install all the dependencies

2. **Executing program**:

   - To run the program, you can open this in VSCode or open Jupiter Notebook (`jupyter notebook`) and hit run to execute `main.ipynb`
   - To run the app locally, you will first `cd app` then `flask run` to run the app
   - If you want to run the app in debugger mode, run `export FLASK_DEBUG=1 flask run`

## Authors

Contributors names and contact info
Van Nguyen
vannguyen599@u.boisestate.edu

## License

This project is licensed under the MIT License.
