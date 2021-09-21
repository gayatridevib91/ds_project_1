# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:55:12 2021

@author: Gayatri Devi
"""


import pandas as pan
from datetime import date 
date=date.today()
yr = int(date.year)
df = pan.read_csv("glassdoor_jobs.csv")
df = df[df['Salary Estimate']!= '-1']
#to find out columns that are hourly paid
df['hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
#to find out columns that has emp provided sal in them
df['Emp_Provided_Salary:']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

Salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_minus_k_and_dollar = Salary.apply(lambda x: x.replace('K','').replace('$',''))
Salary_numbers = salary_minus_k_and_dollar.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary']=Salary_numbers.apply(lambda x: int(x.split('-')[0]))

df['max_salary']=Salary_numbers.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']= (df.min_salary+df.max_salary)/2
#having only company name as text in the field
df['companyName_text']=df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1 )
df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0 ,axis=1)

df['age_Cmpny']=df.Founded.apply(lambda x: x if x<1 else yr - x)
#parsing job description
#for tools like python,R,spark,AWS,excel 

#fro python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#for R
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' or 'r_studio' in x.lower() else 0)
df.R_yn.value_counts()

#for spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

#for AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#for excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.excel_yn.value_counts()

#dropping unnmaed columns
df.columns

df_out=df.drop('Unnamed: 0',axis =1)

d#f_out.to_csv('Salary_Data_cleansed.csv',index=False)
