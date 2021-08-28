'''Entry point and orchestration for the solution'''

import csv
import json
import data_entities.entities
import teacher_provider.teacher_reader

def map_student(row):
    '''Takes a tuple from the .csv and maps to a dictionary'''
    lstud = row[0].split("_")
    mapped = {data_entities.entities.MapKeys.STUDENTFNAME.value: lstud[1],
              data_entities.entities.MapKeys.STUDENTLNAME.value: lstud[2],
              data_entities.entities.MapKeys.TEACHERFNAME.value: '',
              data_entities.entities.MapKeys.TEACHERLNAME.value: '',
              data_entities.entities.MapKeys.CLASSID.value: lstud[6]}
    return mapped

def orchestrate():
    '''Iterating over .csv file in accordance with memory requirements'''
    outputfile = 'results.json'
    #initialize file:
    with open(outputfile, mode='w', encoding='utf-8'):
        pass
    with open('Data/students.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            student = map_student(row)
            teacher_provider.teacher_reader.map_teacher(
                'data/teachers.parquet', student)
            with open(outputfile, mode='a', encoding='utf-8') as file1:
                file1.write(json.dumps(student))

def main():
    '''entry point'''
    orchestrate()
    print ('Processing completed.')

if __name__ == "__main__":
    main()
