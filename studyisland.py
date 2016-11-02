import os
import glob
import pandas as pd

# combine csv files math, english, science, social studies, and keystone into one file called subjects
def concatenate(indir='C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\subjects',
                outfile = 'C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\subjects.csv'):
    os.chdir(indir)
    fileList=glob.glob('*.csv')
    dfList = []
    colnames =["Student Status", "Official Enrollment Date","SIS Primary Key",	"State ID",	"LastName",	"FirstName", "gradelevel",
               "Grade Level Start Date",	"Teachers Name",	"Teachers Email",	"Students Course Start Date",
               "Students Course Scheduled Date",	"Department",	"Section Name",	"Section Code",	"Course Enrollment Status",
               "CurrentAssignment",	"TotalAssignments",	"CreditsEarned",	"CurrentGrade",	"FinalGrade",	"GradingScaleLetter",
               "Term1Grade",	"Term2Grade",	"Term3Grade",	"Term4Grade",	"AcademicAdvisor",	"AcademicAdvisorSpecialEd",	"IEP_Writer",]
    for filename in fileList:
        print(filename)
        df = pd.read_csv(filename)
        dfList.append(df)
    concatDf = pd.concat(dfList,axis=0)
    concatDf.columns=colnames
    concatDf.to_csv(outfile,index=None)
concatenate()

# add passwords from students file into subjects file
subjects = pd.read_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\subjects.csv' , low_memory=False)
students = pd.read_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\students.csv' , low_memory=False)

students_passwords = students[['Student Login', 'Student Password']]
subjects = pd.merge(subjects, students_passwords, how='inner', left_on='SIS Primary Key', right_on='Student Login')

subjects['course_name'] = subjects['Section Name']
subjects['course_name'] = [i.rsplit(' Section')[0] for i in subjects['course_name']]

subjects['Teachers First'] = subjects['Teachers Name']
subjects['Teachers First'] = [i.rsplit(' ')[0] for i in subjects['Teachers First']]
subjects['Teachers Last'] = subjects['Teachers Name']
subjects['Teachers Last'] = [i.rsplit(' ')[1] for i in subjects['Teachers Last']]

subjects['homeroom'] = subjects['Section Name']
subjects['homeroom'] = ["16-17_" + row["Section Name"] + "_" + row["Teachers Last"] for index, row in subjects.iterrows()]
print subjects['homeroom'][0:5]

subjects['homeroom'] = subjects['homeroom'].replace('Keystone Algebra', 'Keystone Alg')
subjects['homeroom'] = subjects['homeroom'].replace('Keystone English Literature', 'Keystone Eng Lit')
subjects['homeroom'] = subjects['homeroom'].replace('College in High School Principles of Biology', 'College in HS Princip of Bio')
subjects['homeroom'] = subjects['homeroom'].replace('Section', 'Sec')

subjects = subjects[subjects["homeroom"].isin ({"Social Studies 5", "Social Studies 6", "Social Studies 6 LS",
"Social Studies 7", "Social Studies 7 LS", "Social Studies 8", "Social Studies 8 LS"
"Algebra I", "Algebra I LS", "CR Algebra I", "Mathematics 3", "Mathematics 3 LS",
"Mathematics 4", "Mathematics 4 LS", "Mathematics 5", "Mathematics 5 LS", "Mathematics 6", "Mathematics 6 LS",
"Mathematics 7", "Mathematics 7 LS", "Mathematics 8", "Mathematics 8 LS"
"English 10", "English 10 LS", "English 7", "English 7 LS", "English 8",
"English 8 LS", "English 9", "English 9 LS", "Language Arts 3",
"Language Arts 3 LS", "Language Arts 4", "Language Arts 4 LS", "Language Arts 5",
"Language Arts 5 LS", "Language Arts 6", "Language Arts 6 LS", "Reading 3",
"Reading 4", "Reading 5"
"AP Biology", "Biology", "Biology LS", "CR Biology", "College in High School Principles of Biology",
"Science 3", "Science 4", "Science 5", "Science 6", "Science 6 LS", "Science 7",
"Science 7 LS", "Science 8"
"Keystone Algebra I Fall 2016", "Keystone Algebra I Spring 2017",
"Keystone Biology Fall 2016", "Keystone Biology Spring 2017",
"Keystone English Literature Fall 2016", "Keystone English Literature Spring 2017"})]

Mathematics = subjects[subjects["Department"] == 'Mathematics']
Mathematics.to_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\Mathematics.csv', sep='\t', encoding='utf-8')

English = subjects[subjects["Department"] == 'Language Arts/English']
English.to_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\Language Arts/English.csv', sep='\t', encoding='utf-8')

Science = subjects[subjects["Department"] == 'Science']
Science.to_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\Science.csv', sep='\t', encoding='utf-8')

Social_Studies = subjects[subjects["Department"] == 'Social Studies']
Social_Studies.to_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\Social Studies.csv', sep='\t', encoding='utf-8')

keystone = subjects[subjects["Department"] == 'Elective']
keystone.to_csv('C:\Users\lbarry\Desktop\All folders\Study Island\Study Island 2016-2017\study island import\keystone.csv', sep='\t', encoding='utf-8')


'''
# alternative idea to divide files - filter by department and then sort by student ID then run the if then
files = []

for index, row in subjects[subjects["department"] == "Math"].iterrows():
    if subjects["Student"] == laststudent: files += 1
    else: file = 1
    if file > len(files): open_new_file()
    write_line_to_this_file()
    laststudent = subjects["Student"]
'''





