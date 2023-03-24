from thefuzz import fuzz, process
from sklearn import feature_extraction, metrics
from typing import List, Any
import pandas as pd

def ratiofunction(test_data,res):
        ratio = process.extractOne(test_data,res)
        #ratio = fuzz.partial_ratio(data,test_data)
        print(ratio)
        return ratio
        # if(ratio[1]>50):
        #     output.append(ratio[0])
        #     print("The correct company name is " + test_data + str(ratio[1]) + "/n")
        #     ind = False
        #     if(ratio[0] == ab[i-1]):
        #           check.append('True') 
        #     else:
        #            check.append('False')
        # if ind:
        #         output.append('Not Found')
        #         check.append('False')
        #         print("Not Found") 

def nlpfunction(table_val,test_data,res):
    threshold: float = 0.3
    vectorizer = feature_extraction.text.CountVectorizer()
    vectors = vectorizer.fit_transform([test_data]+ res ).toarray()

    cosine_sim = metrics.pairwise.cosine_similarity(list(vectors))

    scores = cosine_sim[0][1:]

    scores_df = pd.DataFrame({"score": scores}, index=res)
    df = scores_df.sort_values(by="score", ascending=False)
    df = df.head(1)
    if(df.values >= threshold):
        return df
    else:
         df = pd.DataFrame()
         return df
    # df = scores_df["score"] >= threshold
    # if not len(df.index):
    #         return None
    # else:
    #     df = scores_df.sort_values(by="score", ascending=False)
        
        # print(df)
    # table_df = pd.DataFrame(table_val, index=res)
    # df = table_df.join(scores_df)

    # df = df[df["score"] >= threshold]
    # if not len(df.index):
    #         return "No matches found"
    # else:
    # # Sort by score.
    #     df = df.sort_values(by="score", ascending=False)
    #     df = df.head(1)
    #     return df
    

i = 0
table1 = pd.read_excel("Dummy.xlsx")
table_val = table1.values.tolist()
table2 = pd.read_excel("test_data.xlsx")
input = table2.iloc[:,0].tolist()
# for columns in table2.columns:
#     table2[columns] = table2[columns].str.lower() 
a= table2.iloc[:,0].tolist()
ab = table2.iloc[:,1].tolist()
b = table1.iloc[:,0].tolist()
st = table1[table1['Account Name'].isin(['United Health Group'])]
st_list = []
print(st['ST'].to_string(header=None, index=None))
columns = ['Input', 'Output','Valid Indicator','ST']
output = []
check = []
# value = input("Enter the word\n")
for test_data in a:
        df1 = pd.DataFrame()
        i+=1
        #print(a)
        ind = True
        res = [idx for idx in b if idx[0].lower() == test_data[0].lower()]
        # print (res)
                #print(b)
        df1 = nlpfunction(table_val,test_data,res)
        if not len(df1.index):
            df1 = ratiofunction(test_data,res)
            df1 = df1[0]
            # df1 = df1[0]
        else:
            df1 = df1.index[0]
        # print(df1)
        output.append(df1)
        if(df1 == ab[i-1]):
            check.append('True') 
        else:
            check.append('False')
for data in output:
    st = table1[table1['Account Name'].isin([data])]
    st_list.append(st['ST'].to_string(header=None, index=None))
#print(st_list)
df = pd.DataFrame(list(zip(input,output,check,st_list)), columns=columns)
df.to_excel('Final.xlsx')
        # val = input("Do u want to continue (Y/N) \n")
        # if val== 'Y' or val =='y':
        #      i = True
        # elif val == 'N' or val== 'n':
        #      i = False