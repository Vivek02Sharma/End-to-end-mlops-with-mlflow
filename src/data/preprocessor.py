from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


class DataPreprocessor:
    def __init__(self):
        self.target_feature = 'annual_medical_cost'

        self.num_features = ['age', 'bmi', 'diabetes', 'hypertension', 'heart_disease', 'asthma',
        'daily_steps', 'sleep_hours', 'stress_level', 'doctor_visits_per_year',
        'hospital_admissions', 'medication_count', 'insurance_coverage_pct',
        'previous_year_cost']

        self.cat_features = ['gender', 'smoker', 'physical_activity_level', 'insurance_type',
        'city_type']

    def data_preprocessor(self):
        num_pipeline = Pipeline(steps = [
            ('scaler', StandardScaler())
        ])

        cat_pipeline = Pipeline(steps = [
            ('imputer', SimpleImputer(strategy = 'most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown = 'ignore'))
        ])

        preprocessor = ColumnTransformer(
            transformers = [
                ('num', num_pipeline, self.num_features),
                ('cat', cat_pipeline, self.cat_features)
            ]
        )

        return preprocessor

    def split_data(self, df):
        X = df.drop(self.target_feature, axis = 1)
        y = df[self.target_feature]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size = 0.2,
            random_state = 42
        )

        return X_train, X_test, y_train, y_test


