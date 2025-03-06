import pandas as pd
df=pd.read_excel("Music.xlsx")
#x=df.info
#print(x)
import matplotlib.pyplot as plt

df['Genre'].value_counts().plot(kind='bar', color='purple')
plt.title("Genre Preferences")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

import seaborn as sns
sns.boxplot(x='Genre', y='Age', data=df)
plt.title("Age Distribution by Genre")
plt.xticks(rotation=45)
plt.show()

from sklearn.model_selection import train_test_split
X = df[['Age', 'Gender']]
y = df['Genre']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score ,confusion_matrix
a=accuracy_score(y_test,y_pred)
print(a)

