'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''

filename = input("Enter the filename: ").strip()
output_filename = f"{filename}_out.csv"

with open(filename) as student_data, open(output_filename, "w") as student_output:
    # skip header line (example files have a header)
    next(student_data)

    for line in student_data:
        line = line.strip()
        if not line:
            continue

        parts = [p.strip() for p in line.split(",")]
        if not parts or parts[0] == "":
            continue

        student_id = parts[0]

        # accumulate grades using your style (explicit loop)
        total_grade_points = 0.0
        module_count = 0
        for value in parts[1:]:
            if value != "":
                total_grade_points += float(value)
                module_count += 1

        # compute average (handle zero modules defensively)
        if module_count == 0:
            average_grade = 0.0
        else:
            average_grade = total_grade_points / module_count

        average_str = f"{average_grade:.2f}"

        # classification logic (no extra function, as requested)
        if average_grade >= 70:
            classification = "1"
        elif average_grade >= 60:
            classification = "2:1"
        elif average_grade >= 50:
            classification = "2:2"
        elif average_grade >= 40:
            classification = "3"
        else:
            classification = "F"

        student_output.write(f"{student_id},{average_str},{classification}\n")

