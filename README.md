# gai_ua_parser

This simple parser:
- Accepts a list with car numbers to be checked through API https://baza-gai.com.ua/api
- Sends a request to api and receives a json with a response for each of the numbers
- Checks for empty values (if an error 404 is returned)
- For each of the checked numbers, it returns a fully unpacked json (without values of type dictionary or list)
- The results are recorded in excel file "checked_cars.xlsx" (<a href='checked_cars.xlsx'>Example</a>)

Description of the task is <a href='task.txt'>here</a>

## How to use
### Clone this repo
```
git clone https://github.com/Viktrols/gai_ua_parser
```

### Create and activate the virtual environment
```
python -m venv venv
source ./venv/Scripts/activate  # Windows
source ./venv/bin/activate      # Linux or macOS
```

### Install required dependencies
```
pip install -r requirements.txt
```

### Run the file check_cars_numbers.py
```
python code/check_cars_numbers.py
```

P.S. You can use json_unpacking.py not only in this project:)
