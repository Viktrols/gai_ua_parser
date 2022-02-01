# gai_ua_parser

This simple parser:
- Accepts a list with car numbers to be checked through API https://baza-gai.com.ua/api
- Sends a request to api and receives a json with a response for each of the numbers
- Checks for empty values (if the number is not found)
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
### Get your api key by filling the form at https://baza-gai.com.ua/api and enter its value in a variable API KEY in code/check_cars_numbers.py <br> Better yet, place it in an environment variable.
(I left my key for a quick code check)
### Run the file check_cars_numbers.py
```
python code/check_cars_numbers.py
```

P.S. You can use json_unpacking.py not only in this project:)
