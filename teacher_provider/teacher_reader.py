'''Parses parquet file seeks match for provided student'''

import fastparquet
import data_entities.entities

def map_teacher(input_file, student):
    '''Parses parquet file seeks match for provided student'''
    p_f = fastparquet.ParquetFile(input_file)
    for d_f in p_f.iter_row_groups():
        teacher = d_f.loc[d_f['cid'] == student[data_entities.entities.MapKeys.CLASSID.value]]
        if teacher.empty is False:
            student[data_entities.entities.MapKeys.TEACHERFNAME.value] = teacher.iloc[0].fname
            student[data_entities.entities.MapKeys.TEACHERLNAME.value] = teacher.iloc[0].lname
            return
