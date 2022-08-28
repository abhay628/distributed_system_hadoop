#!/usr/bin/env python
import csv

if __name__=='__main__':
    courseList=[]
    jobList=[]
    with open('coursea_data-1.csv', 'r') as file:
        csvReader = csv.reader(file)
        header = next(csvReader)
        for eachItem in csvReader:
            courseList.append(eachItem)         

    with open('data_job_posts.csv', 'r') as file:
        csvReader = csv.reader(file)
        header = next(csvReader)
        for eachItem in csvReader:
            eachItem[0] = eachItem[0].replace("\n", " ").replace("\t", " ").replace("\r", " ")
            jobList.append(eachItem)        
 
    coursesArray=[]
    for job in jobList:
        for eachCourse in courseList:
            courseItem = eachCourse[1].split(" ")
            if ([item for item in courseItem if(item in job[0])]) :
                coursesArray.append([job[0], eachCourse[1], eachCourse[4] ])  
 
    with open('recommendationFile.data','w+') as f:
        for course in coursesArray:
            f.write(course[0]+'\t'+course[1]+'\t'+course[2]+'\n')