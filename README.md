# super_dan
Don't go to that street today. For now predicting larcenies vs burglaries

For development:
```
git clone https://github.com/Italosayan/super-dan.git
export PYTHONPATH="/Users/path/to/super_dan":$PYTHONPATH
cd super-dan
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

-Change "/Users/path/to/super_dan" to path where the project was cloned

Each part of the pipeline is independent:

* Getting the data
* Data preprocess
* Training

```
python3 super_dan_app/dataset/get_data.py
python3 super_dan_app/dataset/pre_processing.py
python3 training/training.py
```

For testing:

```
python -m pytest
```

Great Expectations workflow and basics

* Suite: Group of expectations
* Expectation : Data test

```
great_expectations suite list
great_expectations init # Only ran once
great_expectations docs build # See expectations in jupyter
great_expectations suite edit # Edits a data doc
great_expectations suite new # Create new group of tests.(Use when new sql or new data source)
```

* Workflow
```
great_expectations tap new day_2020-04-04_crimes day_2020-04-04_crimes_test.py
```

Execute Jenkins
```
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
java -jar jenkins.war --httpPort=8080
```

Next Steps:

1. Set up test workflow: Always run the full test suite before a coding session, and run it again after. This will give you more confidence that you did not break anything in the rest of the code.
2. Set up Jenkins job
3. Set up WandB with current model.
4. Think about workflow and best practices
5. Deploy Pipeline that outputs .pkl to the API using Metaflow
6. Deploy the API using Sagemaker or AWS Lambda
7. Load test


contact : superdancontact@gmail.com
