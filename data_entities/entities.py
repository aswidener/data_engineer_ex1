'''defines key support for dictionary data entity'''

from enum import Enum

class MapKeys(Enum):
    '''keys for dictionary passed through mapped routines'''
    STUDENTFNAME = "studentFirstName"
    STUDENTLNAME = "studentLastName"
    TEACHERFNAME = "teacherFirstName"
    TEACHERLNAME = "teacherLastName"
    CLASSID = "classId"
