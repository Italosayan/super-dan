"""
Training a logistic regression
"""
from super_dan_app.dataset import pre_processing as pp

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    crime_data_for_training = pp.main()


if __name__ == '__main__':
    main()
