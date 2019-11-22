"""
Training a logistic regression
"""
from super_dan_app.dataset import pre_processing as pp
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from pathlib import Path

def main():
    """
    Train dummy classifier and random forest
    """
    crime_data_for_training = pp.main()
    features = crime_data_for_training.loc[:, crime_data_for_training.columns != 'Statute_Text']
    target = crime_data_for_training.loc[:, 'Statute_Text']

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, random_state=0)

    dummy = DummyClassifier(strategy='uniform', random_state=1)
    dummy.fit(features_train, target_train)
    dummy.score(features_test, target_test)

    classifier = RandomForestClassifier()
    classifier.fit(features_train, target_train)
    classifier.score(features_test, target_test)

    training_path = Path(__file__).parent
    dump(classifier, training_path / 'RandomForestClassifier.joblib')

if __name__ == '__main__':
    main()
