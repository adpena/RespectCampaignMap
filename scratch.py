import csv

header_row = ["District"]

for i in range(1, 455):
    header_row.append(f"S.D. {i} Name")
    header_row.append(f"({i})% in Lege Dist.")

with open("scratch.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(header_row)