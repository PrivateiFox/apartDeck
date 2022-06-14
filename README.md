# Basic usage
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m uvicorn main:app --reload
```

# Update requirements
```shell
pip3 freeze > requirements.txt
```