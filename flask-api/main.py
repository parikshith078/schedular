# Strictly for 3rd, 5th and 7th semester CSE
from SEM3CSEA import ttCSE3A
from SEM3CSEB import ttCSE3B
from SEM5CSEA import tt5CSA
from SEM5CSEB import tt5CSB, teachers


timetable = { 'CSE3A' : ttCSE3A,
              'CSE3B' : ttCSE3B,
              'CSE5A' : tt5CSA,
              'CSE5B' : tt5CSB
}

#for _ in timetable:
# print(timetable) s
def returnTable():
    print('done')
    return timetable
