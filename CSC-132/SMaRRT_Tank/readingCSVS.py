import csv

with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t The time is{row[0]}. The temperature is {row[1]} with a salinithy of {row[2]} and a pH of {row[3]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
