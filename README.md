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

Each part of the pipeline is independent:
-Getting the data
-Data preprocess
-Training

```
python3 super_dan_app/dataset/get_data.py
python3 super_dan_app/dataset/pre_processing.py
python3 training/training.py
```

For testing:

```
python -m pytest
```
