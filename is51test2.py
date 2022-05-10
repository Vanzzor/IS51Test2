"""
Program opens a file that has the grades, named final.txt
reads the number of lines and prints out grades count
reads the total grades and divides by number of grades to obtain average
prints out average,
if the value is > average, sends to list , divide count of list on original grades count

"""
"""
file=open final.txt
grades=[]
grades.append(int(line.strip))
print="number of grades" len(grades)
avg=0
for grade in grades add avg to grades
average /= len(grade)
print average, avg

def calculate_percent_above_average()
count=0
if grade > avg add to count
return count*100/len(grades)

"""


def calculate_percent_above_average(grades, avg):
    count=0
    for grade in grades:
        if grade > avg:
            count +=1
    return(count*100)/len(grades)



def main():
    f=open("Final.txt", "r")
    grades=[]
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    avg=0
    for grade in grades:
        avg += grade
    avg /=len(grades)
    print("Average grade:", avg)
    print("Percentage of grades above average: {:.2f}%".format(
        calculate_percent_above_average(grades, avg)))
    f.close()




main()