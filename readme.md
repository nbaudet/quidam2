# Quidam2

## Installation
### Windows
- Install Python 3.6 executable and choose to add python in the PATH
- Install Git executable
- Write following commands to create a new directory in C:\ and download quidam2's sources:
```
mkdir "C:\quidam2"
cd "C:\quidam2"
git clone "... quidam2 url ..."
```
- Write following commands to create a new directory in C:\, install and setup the proper running environment:
```
mkdir "C:\envs"
cd "C:\envs"
pip install virtualenv
virtualenv quidam2
"C:\envs\quidam2\Scripts\activate.bat"
```
- Now with the virtual environment activated, install the project's packages:
```
cd "C:\quidam2"
pip install -r requirements.txt
```
### MacOS/Linux

## Run quidam2
After successful installation, create the Django database (here SQLite), then a superuser, then run:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```