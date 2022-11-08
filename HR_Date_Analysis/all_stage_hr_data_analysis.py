######################################### Stage 1/5: Load the data and modify the indexes #####################

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    dffa = pd.read_xml('https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1')
    dffb = pd.read_xml('https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1')
    dffh = pd.read_xml('https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1')

    dffa.index = [f"A{i}" for i in dffa['employee_office_id']]
    dffb.index = [f"B{i}" for i in dffb['employee_office_id']]
    dffh.set_index('employee_id', inplace=True, drop=False)

    print(dffa.index.tolist())
    print(dffb.index.tolist())
    print(dffh.index.tolist())


############################# Stage 2/5: Merge everything ###############################

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    dffa = pd.read_xml('A_office_data.xml')
    dffb = pd.read_xml('B_office_data.xml')
    dffh = pd.read_xml('hr_data.xml')

    dffa.index = [f"A{i}" for i in dffa['employee_office_id']]
    dffb.index = [f"B{i}" for i in dffb['employee_office_id']]
    dffh.set_index('employee_id', inplace=True, drop=False)

    res = pd.concat([dffa, dffb])

    res1 = pd.merge(res, dffh, left_index=True, right_index=True, indicator=True, sort=True).drop(['employee_office_id', 'employee_id', "_merge"], axis=1)

    print(res1.index.tolist())
    print(res1.columns.tolist())


##############################  Stage 3/5: Get the insights ########################

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    dffa = pd.read_xml('A_office_data.xml')
    dffb = pd.read_xml('B_office_data.xml')
    dffh = pd.read_xml('hr_data.xml')

    dffa.index = [f"A{i}" for i in dffa['employee_office_id']]
    dffb.index = [f"B{i}" for i in dffb['employee_office_id']]
    dffh.set_index('employee_id', inplace=True, drop=False)

    res = pd.concat([dffa, dffb])

    res1 = pd.merge(res, dffh, left_index=True, right_index=True, indicator=True, sort=True).drop(['employee_office_id', 'employee_id', "_merge"], axis=1)

    print(res1.sort_values(by=['average_monthly_hours'], ascending=False).head(10).Department.tolist())

    print(sum(res1[(res1.salary == 'low') &  (res1.Department == 'IT')].number_project.tolist()))

    res2 = res1.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']]

    li = [[i for i in res2.iloc[ 0 , 0:]], [i for i in res2.iloc[ 1 , 0:]], [i for i in res2.iloc[ 2 , 0:]]]

    print(li)


    ########################################### Stage 4/5: Aggregate the data ##################

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    dffa = pd.read_xml('A_office_data.xml')
    dffb = pd.read_xml('B_office_data.xml')
    dffh = pd.read_xml('hr_data.xml')

    dffa.index = [f"A{i}" for i in dffa['employee_office_id']]
    dffb.index = [f"B{i}" for i in dffb['employee_office_id']]
    dffh.set_index('employee_id', inplace=True, drop=False)

    res = pd.concat([dffa, dffb])

    res1 = pd.merge(res, dffh, left_index=True, right_index=True, indicator=True, sort=True).drop(['employee_office_id', 'employee_id', "_merge"], axis=1)

    # print(res1.sort_values(by=['average_monthly_hours'], ascending=False).head(10).Department.tolist())
    #
    # print(sum(res1[(res1.salary == 'low') &  (res1.Department == 'IT')].number_project.tolist()))
    #
    # res2 = res1.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']]
    #
    # li = [[i for i in res2.iloc[ 0 , 0:]], [i for i in res2.iloc[ 1 , 0:]], [i for i in res2.iloc[ 2 , 0:]]]
    #
    # print(li)
    # print(res1)
    # country_grp = res1.groupby(['time_spend_company'])
    # print(country_grp.get_group('time_spend_company'))

    def count_bigger_5(series):
        return (series>5).sum()

    res2 = res1.groupby(['left']).agg({'number_project':['median', count_bigger_5],
                            'time_spend_company':['mean', 'median'],
                            'Work_accident':['mean'],
                            'last_evaluation':['mean', 'std']})

    print(res2.round(2))
    print(res2.round(2).to_dict())



################################# Draw up pivot tables ########################

import pandas as pd
import numpy as np
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    dffa = pd.read_xml('A_office_data.xml')
    dffb = pd.read_xml('B_office_data.xml')
    dffh = pd.read_xml('hr_data.xml')

    dffa.index = [f"A{i}" for i in dffa['employee_office_id']]
    dffb.index = [f"B{i}" for i in dffb['employee_office_id']]
    dffh.set_index('employee_id', inplace=True, drop=False)

    res = pd.concat([dffa, dffb])

    res1 = pd.merge(res, dffh, left_index=True, right_index=True, indicator=True, sort=True).drop(['employee_office_id', 'employee_id', "_merge"], axis=1)

    # print(res1.sort_values(by=['average_monthly_hours'], ascending=False).head(10).Department.tolist())
    #
    # print(sum(res1[(res1.salary == 'low') &  (res1.Department == 'IT')].number_project.tolist()))
    #
    # res2 = res1.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']]
    #
    # li = [[i for i in res2.iloc[ 0 , 0:]], [i for i in res2.iloc[ 1 , 0:]], [i for i in res2.iloc[ 2 , 0:]]]
    #
    # print(li)
    # print(res1)
    # country_grp = res1.groupby(['time_spend_company'])
    # print(country_grp.get_group('time_spend_company'))

    # def count_bigger_5(series):
    #     return (series>5).sum()
    #
    # res2 = res1.groupby(['left']).agg({'number_project':['median', count_bigger_5],
    #                         'time_spend_company':['mean', 'median'],
    #                         'Work_accident':['mean'],
    #                         'last_evaluation':['mean', 'std']})
    #
    # print(res2.round(2))
    # print(res2.round(2).to_dict())

    res3 = res1.pivot_table(columns=['left', 'salary'], index=res1["Department"], values='average_monthly_hours', aggfunc=np.median).round(2)
    res4 = res3.loc[["IT", "management"]]
    print(res4.to_dict())



    res5 = res1.pivot_table(index='time_spend_company', columns='promotion_last_5years', values=['last_evaluation', 'satisfaction_level'], aggfunc=['max','mean','min']).round(2)
    res6 = res5[res5['mean']['last_evaluation'][0] > res5['mean']['last_evaluation'][1]]
    print(res6.to_dict())
