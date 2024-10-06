import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.set_index('student_id')
    print(students.loc[101,['name','age']])
    return students.loc[101,['name','age']].to_frame().T
    