# write your code here

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 8)
######################### stage 1 ############################
# general_df = pd.read_csv('general.csv')
# prenatal_df = pd.read_csv('prenatal.csv')
# sports_df = pd.read_csv('sports.csv')

# print(general_df.head(20))
# print(prenatal_df.head(20))
# print(sports_df.head(20))
##############################################################

###################### stage 2 ###############################
# general_df = pd.read_csv('general.csv')
# prenatal_df = pd.read_csv('prenatal.csv', header=0, names=general_df.columns)
# sports_df = pd.read_csv('sports.csv', header=0, names=general_df.columns)
#
# # print(general_df.head(20))
# # print(prenatal_df.head(20))
# # print(sports_df.head(20))
#
# merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True).drop(columns=['Unnamed: 0'])
# print(merged_df.sample(n=20, random_state=30))
############################################################

################### stage 3 ###############################
# general_df = pd.read_csv('general.csv')
# prenatal_df = pd.read_csv('prenatal.csv', header=0, names=general_df.columns)
# sports_df = pd.read_csv('sports.csv', header=0, names=general_df.columns)
#
# merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True).drop(columns=['Unnamed: 0'])
#
# merged_df.dropna(axis=0, how="all", inplace=True)
#
# merged_df.loc[merged_df.gender == "female", 'gender'] = "f"
# merged_df.loc[merged_df.gender == "woman", 'gender'] = "f"
# merged_df.loc[merged_df.gender == "male", 'gender'] = "m"
# merged_df.loc[merged_df.gender == "man", 'gender'] = "m"
#
# merged_df.loc[merged_df['hospital'] == "prenatal", "gender"] = "f"
#
# merged_df.fillna(0, inplace=True)
#
# print(merged_df.shape)
# print(merged_df.sample(n=20, random_state=30))
###################################################################

################## stage 4 #######################################
#
# general_df = pd.read_csv('general.csv')
# prenatal_df = pd.read_csv('prenatal.csv', header=0, names=general_df.columns)
# sports_df = pd.read_csv('sports.csv', header=0, names=general_df.columns)
#
# merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True).drop(columns=['Unnamed: 0'])
#
# merged_df.dropna(axis=0, how="all", inplace=True)
#
# merged_df.loc[merged_df.gender == "female", 'gender'] = "f"
# merged_df.loc[merged_df.gender == "woman", 'gender'] = "f"
# merged_df.loc[merged_df.gender == "male", 'gender'] = "m"
# merged_df.loc[merged_df.gender == "man", 'gender'] = "m"
#
# merged_df.loc[merged_df['hospital'] == "prenatal", "gender"] = "f"
#
# merged_df.fillna(0, inplace=True)
# merged_df.hospital.value_counts()
# merged_df.loc[merged_df['hospital'] == 'general', 'diagnosis'].count()
# merged_df.loc[merged_df['hospital'] == 'general', 'diagnosis'].value_counts()
# # print(round(150/461, 3))
#
# merged_df.loc[merged_df['hospital'] == 'sports', 'diagnosis'].count()
# merged_df.loc[merged_df['hospital'] == 'sports', 'diagnosis'].value_counts()
# # print(round(61/214, 3))
#
# merged_df.loc[merged_df['hospital'] == 'general', 'age'].median()
# merged_df.loc[merged_df['hospital'] == 'sports', 'age'].median()
#
# merged_df.loc[merged_df['hospital'] == 'general', 'blood_test'].value_counts()
# merged_df.loc[merged_df['hospital'] == 'prenatal', 'blood_test'].value_counts()
#
# print('''
# The answer to the 1st question is general
# The answer to the 2nd question is 0.325
# The answer to the 3rd question is 0.285
# The answer to the 4th question is 19
# The answer to the 5th question is prenatal, 325 blood tests''')
##################################################################################

#################################### stage 5 ####################################
general_df = pd.read_csv('general.csv')
prenatal_df = pd.read_csv('prenatal.csv', header=0, names=general_df.columns)
sports_df = pd.read_csv('sports.csv', header=0, names=general_df.columns)

merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True).drop(columns=['Unnamed: 0'])

merged_df.dropna(axis=0, how="all", inplace=True)

merged_df.loc[merged_df.gender == "female", 'gender'] = "f"
merged_df.loc[merged_df.gender == "woman", 'gender'] = "f"
merged_df.loc[merged_df.gender == "male", 'gender'] = "m"
merged_df.loc[merged_df.gender == "man", 'gender'] = "m"

merged_df.loc[merged_df['hospital'] == "prenatal", "gender"] = "f"

merged_df.fillna(0, inplace=True)
stage5 = merged_df
merged_df.hospital.value_counts()
merged_df.loc[merged_df['hospital'] == 'general', 'diagnosis'].count()
merged_df.loc[merged_df['hospital'] == 'general', 'diagnosis'].value_counts()
# print(round(150/461, 3))

merged_df.loc[merged_df['hospital'] == 'sports', 'diagnosis'].count()
merged_df.loc[merged_df['hospital'] == 'sports', 'diagnosis'].value_counts()
# print(round(61/214, 3))

merged_df.loc[merged_df['hospital'] == 'general', 'age'].median()
merged_df.loc[merged_df['hospital'] == 'sports', 'age'].median()

merged_df.loc[merged_df['hospital'] == 'general', 'blood_test'].value_counts()
merged_df.loc[merged_df['hospital'] == 'prenatal', 'blood_test'].value_counts()

# print('''
# The answer to the 1st question is general
# The answer to the 2nd question is 0.325
# The answer to the 3rd question is 0.285
# The answer to the 4th question is 19
# The answer to the 5th question is prenatal, 325 blood tests''')

mydict = stage5.age.value_counts().to_dict()
mylist = [key for key, val in mydict.items() for _ in range(val)]
bins = [0, 15, 35, 55, 70, 80]
plt.hist(mylist, bins=bins, color="orange", edgecolor="white")
plt.title("Age")
plt.ylabel("Number of people")
plt.xlabel("Age")
plt.show()

data = stage5.diagnosis.value_counts().to_dict().values()
labels = stage5.diagnosis.value_counts().to_dict().keys()

plt.pie(data, labels=labels)
plt.show()

plt.pie(data)
plt.show()

print('''
The answer to the 1st question: 15-35
The answer to the 2nd question: pregnancy
The answer to the 3rd question: It's because It's probably because of different meassure size (feet, meter)''')