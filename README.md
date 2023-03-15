# RESTAPI-python-using-FastAPI

## Steps to start with FastAPI.
#### 1. Install Virtuale Environment
```
pip install virtualenv
```

#### 2. Create Virtual Environment for project.
##### Locate the directory of your project in your terminal and below mentioned command.
```
virtualenv venv
```

#### 3. Activate virtual environment
```
For Windows:  1) cd venv/scripts
              2) activate
              
For Linux:    source venv/bin/activate
```

#### 4. Install required packages.
```
cd ..
pip install pymongo fastapi uvicorn
```

#### 5. Create main python file. e.g. index.py, main.py etc

#### 6. Run the app
```
uvicorn index:app --reload
```

#### 7. To deactivate virtual environment use this command:
```
deactivate
```
