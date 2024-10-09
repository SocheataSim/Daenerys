def schoolSelection(ages):
    grade_level = {
        'Kindergarden' : 0,
        '1st grade' : 0,
        '2nd grade' : 0,
        '3rd grade' : 0,
        '4th grade' : 0,
        }
    for age in ages:
        if age == 5 :
            grade_level['Kindergarden'] += 1
        elif age == 6 :
            grade_level['1st grade'] += 1
        elif age == 7 :
            grade_level['2nd grade'] += 1
        elif age == 8 :
            grade_level['3rd grade'] += 1
        elif age == 9 :
            grade_level['4th grade'] += 1
    return grade_level
ages = [5, 7, 4, 9, 10, 5, 15, 9, 5]
result = schoolSelection(ages)
print(result)
        