from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from openpyxl.workbook import Workbook

df = pd.read_excel('zhairusdata.xlsx')


def remov_punct(withpunct):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    without_punct = ""
    char = 'nan'
    for char in withpunct:
        if char not in punctuations:
            without_punct = without_punct + char
    return without_punct


list = []
for s in range(len(df)):
    list.append(remov_punct(df['text'][s]).lower())
df = pd.DataFrame({"text": list, "sent": df['sent']})


cv = CountVectorizer()
cv.fit(df['text'])

X = cv.transform(df['text'])

y = df['sent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

X_train_1, X_val, y_train_1, y_val = train_test_split(
    X_train, y_train, train_size = 0.7
)

for c in [0.01, 0.05, 0.25, 0.5, 1]:
    lr = LogisticRegression(C=c)
    lr.fit(X_train_1, y_train_1)
    print("Accuracy for C=%s: %s"
          % (c, accuracy_score(y_val, lr.predict(X_val))))

final_model = LogisticRegression(C=0.05)
final_model.fit(X_train, y_train)
print("Final Accuracy: %s"
       % accuracy_score(y_test, final_model.predict(X_test)))


test_df = pd.DataFrame()

test_df['predict'] = final_model.predict(X_test)

list2 = []
for s in range(len(test_df)):
    list2.append(test_df['predict'][s])
print(list2)


# for additional test data

final_test = pd.read_excel('zhairusdata.xlsx')

cv2 = CountVectorizer()
cv2.fit(final_test['text'])

X_final = cv.transform(final_test['text'])

final_predict = pd.DataFrame()
final_predict['predict'] = final_model.predict(X_final)

list_final = []
for s in range(len(final_predict)):
    list_final.append(final_predict['predict'][s])
print(list_final)

final_test['prediction'] = list_final

final_test.to_excel('final_test.xlsx')