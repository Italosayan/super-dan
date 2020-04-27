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

Workflow
```
After a commit execute jenkins:
Docker, great_expectations and pytest will be executed
```

Next Steps:

1. Set up test workflow: Always run the full test suite before a coding session, and run it again after. This will give you more confidence that you did not break anything in the rest of the code.
2. Set up Jenkins job
3. Set up WandB with current model.
4. Think about workflow and best practices
5. Deploy Pipeline that outputs .pkl to the API using Metaflow
6. Deploy the API using Sagemaker or AWS Lambda
7. Load test


Workflow Advice
* Test to know if code works
* Remove fear
* When code is changed add a test
* When a bug is found write a test
* Test explains how
* Write comments to explain why

Experimentation:
* Weights and biases is a great way to store runs
* Experimentation iteration?

Production:
* Metaflow
* Sagemaker


Data Science Workflow
1. Planning & Project setup
    * Define Goal: Benefit
        * Complex heuristics
        * Look for places where cheap prediction can help
        * Where are humans writing rules?
    * Define Goal: Cost
        * Data availability: How to acquire it?
        * Labeling expensive?
        * How costly are wrong predictions?
        * How easy to solve?
    * Choosing a metrics:
        * Define recall and precision in domain
            * Precision: How many of the recommended wines are good?
            * Recall: How many of the good wines are recommended?
        * Do we have a threshold in any of the metrics?
            * Example: recall > 0.6 and the choose the one with the highest precision
    * Requirements:
        * Realtime(Inference Pipeline) or Batch(Batch Transform)?
        * Inference time. Train time.
        * Baselines: Human performance.
    * Evaluation:
        * A/B Test Design
        * Tracking
    

2. Data collection & labeling
    * EDA
    * Domain knowledge
    * SQL like crazy

3. Training and debugging
    * Model of increasing complexity
    * Interpretable
    
4. Deployment
    * AWS Sagemaker
        0. export AWS_PROFILE=italouser
        0. aws configure --profile italouser
        1. build_and_push.sh name-of-estimator: Image pushed to ecr
        2. ARN_USER is defined in .zprofile
        3. Change name-of-estimator in sage_sdk_setup_train.py
        4. run sage_sdk_setup_train.py (without deploy command)
            - uploads training data
            - Writes model artifacts to s3 inside output sub directory
            - sagemaker-eu-west-1/output/decision-tree/output model artifact
        5. run sage_sdk_setup_train.py (with deploy command)
            - the deploy command: 
            - Upload train/serve image to sagemaker with a image type and count.
            - Endpoint config and creation
            - Model in sagemaker
        6. Change endpoint name and run sage_sdk_get_requests.py
            
        
    ML in production: 
    WSGI: server and application communication 
    Http -> Nginx(Distributes to workers) -> HTTP -> Gunicorn workers parse http using wsgi and pass inputs to python application -> (flask or django or anything)
    1. Nginx is a light-weight layer that handles the incoming HTTP requests and manages the I/O in and out of the container efficiently.
    2. Gunicorn is a WSGI pre-forking worker server that runs multiple copies of your application and load balances between them.
    3. Flask is a simple web framework used in the inference app that you write. It lets you respond to call on the /ping and /invocations endpoints without having to write much code.
    
    Sagemaker deploy explanation:
    1. Training job(docker-tag train) 
        1. Input training data to the sagemaker session using upload_data.
        2. AWS executes your train code. Gets data and trains.
        3. Train code writes model output to opt/ml/model and sagemaker copies it to s3.
    2. Deploy(docker-tag serve):  
        1. Creates deployable model: Gets it from s3. The location specified in the output_path of ESTIMATOR.
        2. Configures endpoint
        3. Launches the endpoint

5. Monitoring
    * Datadog


* https://medium.com/sequoia-capital/sequoia-data-science-8a76098035a4
* https://www.fast.ai/2020/01/07/data-questionnaire/
* http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf

Tools to explore:
* Summarize wandb plots
* https://pair-code.github.io/what-if-tool/
* https://flyte.org/
* https://www.kaggle.com/learn/machine-learning-explainability
* https://christophm.github.io/interpretable-ml-book/

contact : superdancontact@gmail.com
