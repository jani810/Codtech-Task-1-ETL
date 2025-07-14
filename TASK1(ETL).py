import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)

print(df.head())
print(df.isnull().sum())

le = LabelEncoder()
df['species_encoded'] = le.fit_transform(df['species'])

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

df_scaled = pd.DataFrame(scaled_features, columns=features)
df_scaled['species'] = df['species']
df_scaled['species_encoded'] = df['species_encoded']

df_scaled.to_csv("iris_cleaned.csv", index=False)
print("iris_cleaned.csv saved.")
