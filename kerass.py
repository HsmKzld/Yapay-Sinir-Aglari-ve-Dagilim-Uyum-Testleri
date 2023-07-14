import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Panda Dataframe ile verinin Excel dosyasından okunmasını sağlar.
df = pd.read_excel("d://DagilimEgitimSeti.xls")

# Giriş değerlerinin (X) ve çıkış değerlerinin (y) olarak ayrılması
X = df.iloc[:, :10].values
y = df.iloc[:, 10:16].values

# Sinir Ağı modelinin tanımlanması
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(6, activation='linear'))
# Modelin derlenmesi
model.compile(loss='mean_squared_error', optimizer='adam')

# keras modelinin veri kümesine sığdırılması ve eğitilmesi
model.fit(X, y, epochs=200, batch_size=32, verbose=False)

# Veri üzerinde tahmin yapılması
y_pred = model.predict(X)

# Tahmin sonuçlarını DataFrame'e aktar
df_pred = pd.DataFrame(y_pred, columns=['Prediction_1', 'Prediction_2', 'Prediction_3', 'Prediction_4', 'Prediction_5', 'Prediction_6'])
# Tahmin sonuçlarını df DataFrame'ine ekleyin
df[['Prediction_1', 'Prediction_2', 'Prediction_3', 'Prediction_4', 'Prediction_5', 'Prediction_6']] = df_pred[['Prediction_1', 'Prediction_2', 'Prediction_3', 'Prediction_4', 'Prediction_5', 'Prediction_6']]
# df DataFrame'ini Excel dosyasına aktar
df.to_excel('d://data_with_prediction.xls', index=False)





