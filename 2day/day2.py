def is_ascending(report):
    for i in range(len(report)-1):
        if report[i]>report[i+1]:
            return False
    return True

def is_descending(report):
    for i in range(len(report)-1):
        if report[i]<report[i+1]:
            return False
    return True

def check_ascending_descending_safety(report):
    is_safe=True
    safety=0
    #check fully ascending or descending
    if is_ascending(report):
        for i in range(len(report)-1):
            difference = report[i+1]-report[i]
            if difference < 1 or difference > 3:
                is_safe = False
                break
    elif is_descending(report):
        for i in range(len(report)-1):
            difference = report[i]-report[i+1]
            if difference < 1 or difference > 3:
                is_safe = False
                break
    else:
        is_safe = False
    
    if is_safe:
        #print("Report:", report," is Safe")
        safety+=1
    else:
        #print("Report:", report," is Unsafe")
        print("")

    return safety

#loading input into list_of_reports
file = open('input', 'r')
list_of_reports = []
for line in file:
    array = [int(value) for value in line.split()]
    list_of_reports.append(array)

#print("full list:", list_of_reports)
total_safety = 0
updated_safety=0

for report in list_of_reports:
    
    if check_ascending_descending_safety(report)==0:
        temp_report=report.copy()
        for i in range(len(report)):
            temp_report.pop(i)
            if check_ascending_descending_safety(temp_report)==1:
                updated_safety+=1
                break
            temp_report=report.copy()
        
    total_safety += check_ascending_descending_safety(report)

print("Total Safety:",total_safety)
print("Updated Safety:", updated_safety)
print("Grand Total", total_safety+updated_safety)