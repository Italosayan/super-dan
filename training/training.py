"""
Training a logistic regression
"""
from super_dan_app.dataset import pre_processing as pp
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from pathlib import Path
import wandb

wandb.init(project="superdan_training")


def main():
    """
    Train dummy classifier and random forest
    """
    crime_data_for_training = pp.main()
    features = crime_data_for_training.loc[:, crime_data_for_training.columns != 'Statute_Text']
    target = crime_data_for_training.loc[:, 'Statute_Text']
    labels = target.unique().tolist()
    feature_names = features.columns.tolist()

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, random_state=0)

    LogReg = LogisticRegression(C=1e5)
    LogReg.fit(features_train, target_train)
    dummy_score = LogReg.score(features_test, target_test)
    y_pred = LogReg.predict(features_test)
    y_probas = LogReg.predict_proba(features_test)
    print(dummy_score)
    # Wandb
    wandb.sklearn.plot_classifier(LogReg,
                                  features_train, features_test,
                                  target_train, target_test,
                                  y_pred, y_probas,
                                  labels, model_name='Logistic Regression', feature_names=feature_names)

    classifier = RandomForestClassifier(random_state=0)
    classifier.fit(features_train, target_train)
    acc = classifier.score(features_test, target_test)
    y_pred = classifier.predict(features_test)
    y_probas = classifier.predict_proba(features_test)
    print(acc)
    # Wandb
    wandb.sklearn.plot_classifier(classifier,
                                  features_train, features_test,
                                  target_train, target_test,
                                  y_pred, y_probas,
                                  labels, model_name='Random Forest', feature_names=feature_names)

    training_path = Path(__file__).parent
    dump(classifier, training_path / 'RandomForestClassifier.joblib')


if __name__ == '__main__':
    main()
