# super_dan
Don't go to that street today. 

For development:
```
git clone https://github.com/Italosayan/super-dan.git
cd super-dan
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Getting data and preprocess

```
python3 super_dan_app/dataset/get_data.py
python3 super_dan_app/dataset/pre_processing.py
```

For testing:

```
python -m pytest
```
