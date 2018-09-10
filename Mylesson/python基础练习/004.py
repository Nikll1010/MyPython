import pickle

city = ['ada ', ['daa'], 'a', 111]
pickle_file = open('city_data.pkl', 'wb')

pickle.dump(city, pickle_file)
pickle_file.close()

