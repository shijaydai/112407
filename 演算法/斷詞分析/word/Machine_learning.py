from sklearn.datasets import load_iris,load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score , precision_score , accuracy_score , classification_report , roc_auc_score , recall_score
from sklearn.model_selection import train_test_split
import pandas as pd


# X, y = load_iris(return_X_y=True)
X, y = load_wine(return_X_y=True)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)


clf = LogisticRegression().fit(X_train, y_train)

y_pred = clf.predict(X_test)
# print(f"預測：{y_pred}")
y_pred_proba = clf.predict_proba(X_test)# 使用模型進行預測，得到每個類別的機率
# print(F"預測機率表：\n{y_pred_proba}")

print(f"\nModel 原先分數(score)：{clf.score(X, y).round(2)}")
print(f"Accuracy score：{accuracy_score(y_test, y_pred).round(2)}")
print(f"F1 score：{f1_score(y_test, y_pred,average = 'weighted').round(2)}")
print(f"Precision score：{precision_score(y_test, y_pred,average = 'weighted').round(2)}")
print(f"Recall score：{recall_score(y_test, y_pred,average = 'weighted').round(2)}")
'''
OvR通常更適用於多類別問題，因為每個分類器只需處理一個類別和其餘的所有類別，減少了建立分類器的次數。
OvO通常在二元分類器的性能較差時使用，因為對每一對類別都要建立一個分類器，這可能更耗時，但在某些情況下能夠更好地捕捉類別之間的微妙差異。
'''
print(f"AUC-ROC score：{roc_auc_score(y_test, y_pred_proba,multi_class='ovr').round(3)}")
print(f"Classification_Report：\n{classification_report(y_test, y_pred)}")

'''
Accuracy
F1-score
Precision
Recall
AUC-ROC
'''

print("-"*90)

from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
X, y = load_digits(return_X_y=True)
clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X, y)
print(f"{clf.score(X, y)}")

