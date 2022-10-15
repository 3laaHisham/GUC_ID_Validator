# GUC_ID_Validator
Simple Django API to Validate GUCians IDs


## Installation
Inside your terminal, clone the repo and install dependencies in a virtual environement with pipenv.


```bash
git clone https://github.com/3laaHisham/GUC_ID_Validator.git
cd GUC_ID_Validator/
pip install pipenv #Replace with sudo pip3 for Linux
pipenv install django
pipenv shell
```


## Usage
Run the following command to Launch the server
```bash
python manage.py runserver
```

Finally, open this Link to Preview the result
```bash
http://127.0.0.1:8000/{ID} # instead of {ID} write your GUCian ID.
```


## Example
This input
```bash
http://127.0.0.1:8000/52-23873
```
outputs this 
```bash
"Valid ID, Entrance Year is 2020"
```
Invalid Input
```bash
http://127.0.0.1:8000/51-23873
```
outputs
```bash
"Not a Valid ID :("
```

## ID Format

```bash
x(x| ) - yyyy(y| ) 
```


- x(x| ) represents class number (can be one or two numbers) and has to satisfy the equation ( x(x| ) - 1 ) % 3 = 0

- yyyy(y| ) represents student number (can be four or five numbers) and cannot equal 0

<br><br>
This project was completed as an IEEE enrolment task and was inspired by here [Egyptian national ID validator](https://github.com/aboueleyes/id-validator). 
