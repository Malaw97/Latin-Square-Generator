import random
import time

final=[]
dimension=9
fail_threshold=dimension**2

def random_gen():
    row=[]
    i=0
    fail_count=0
    while i<dimension:
        entry=random.randint(1,dimension)
        if entry not in row and check_entry(i,entry)==True:
            i+=1
            row.append(entry)
        else:
            fail_count+=1
            if fail_count>fail_threshold:
                fail_count, i, row=0, 0, []
    final.append(row)

def check_entry(i, entry):
    index_list=[]
    for list_item in final:
        index_list.append(list_item[i])
    if entry in index_list:
        return False
    else:
        return True


if __name__ == "__main__":
    time1=time.time()
    for i in range(dimension):
        random_gen()
    print("Operation took "+ str(time.time()-time1) + " seconds")
    for i in final:
        print(i)