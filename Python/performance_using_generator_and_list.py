#performance improvement using generator

import random
import time
names=['sunny','bunny','punny','hunny']
subjects=['Python','Java','R']


def people_list(num):
    result=[]
    for i in range(num):
        person={'id':i,
                'name':random.choice(names),
                'subject':random.choice(subjects)
                
                }
        result.append(person)
    return result

def people_generator(num):
    
    for i in range(num):
        person={'id':i,
                'name':random.choice(names),
                'subject':random.choice(subjects)
                
                }
        
    yield person

t1=time.process_time()
people=people_list(100000)
t2=time.process_time()
print("Time taken for list is:",t2-t1)
#print(people)

t1=time.process_time()
people=people_generator(100000)
t2=time.process_time()
print("Time taken for generator is:",t2-t1)
