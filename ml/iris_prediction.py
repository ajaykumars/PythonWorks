import pandas

url = "data_sets/iris.data"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url,names=names)
print(dataset.shape)
print(dataset.describe())
print(dataset.groupby('class').size())




