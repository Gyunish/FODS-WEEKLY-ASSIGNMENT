import csv
file=input("Enter file name")   #taking user input

try:
    file=open(file, mode='r', newline='', encoding='utf-8')     #opening file in read mode
    reader=csv.reader(file)
    rows=list(reader)
    file.close()

    if not rows:
        print("The CSV file is empty.")

    #determines max width of each column
    num_columns=len(rows[0])
    col_widths=[0]*num_columns
    for row in rows:
        for i in range(num_columns):
            col_widths[i]=max(col_widths[i],len(row[i]))

    #prints header and separator
    header=rows[0]
    separator='+'.join('-'*(w + 2) for w in col_widths)
    print(separator)
    print('| '+' | '.join(header[i].ljust(col_widths[i]) for i in range(num_columns)) + ' |')
    print(separator)

    #prints data rows
    for row in rows[1:]:
        print('| ' + ' | '.join(row[i].ljust(col_widths[i]) for i in range(num_columns)) + ' |')
    print(separator)
except FileNotFoundError:
    print("File not found")