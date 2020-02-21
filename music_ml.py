#1.import the data2.clean the data3.split the data into training/test sets4.create a model5.train the model6.make predictions7.evaluate and improve
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

'''part1
music_data = pd.read_csv('music.csv')
print(music_data.describe())
X = music_data.drop(columns=['genre'])
y = music_data['genre']
#决策树
model = DecisionTreeClassifier()
model.fit(X, y)#这个地方是用了所有样本做预测
predictions = model.predict([[21, 1], [22, 0]])#用了两个sample验证""
'''
'''part2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
music_data = pd.read_csv('music.csv')
#print(music_data.describe())下面是import data
X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)#80来训练20%用来testing
#创建模型部分
model = DecisionTreeClassifier()
#训练模型部分
model.fit(X_train, y_train)
#让它做出预测
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)#会返回一个0到1的值
print(score)
'''
'''part3
#训练模型是十分耗时的，模型的泛化性就十分重要，把训练好的model保存起来
import joblib #教程中为from sklearn.externals import joblib

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'music-recommender.joblib')
'''
'''part4
#在第三部分已经有了训练好的模型，直接可以拿来做预测
import joblib
model = joblib.load('music-recommender.joblib')
predictions = model.predict([[21, 1], [22, 0]])
print(predictions)
'''
#part5 可视化

from sklearn import tree
import graphviz

music_data = pd.read_csv('music.csv')

X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model, out_file='music-recommender.dot', #model,输出的文件教程使用的是out_file='music-recommender.dot'
                     feature_names=['age', 'gender'],#设置成两个字符串数组，age和gender是特征列，会显示rules在输出里
                     class_names=sorted(y.unique()),#class会显示类，y里面包括jazz之类的，sorted function是排序
                     label='all',#每个节点都有可读的标签
                     rounded=True,#方框会有圆角
                     filled=True)#filled为真表示每个节点有特定的颜色

#安装graphviz.msi后在cmd输入下列指令
# dot -Tpdf C:\Users\kimmko\PycharmProjects\guangtou\music-recommender.dot -o C:\Users\kimmko\PycharmProjects\guangtou\music-recommender.pdf
