import json
import csv

districts = []

with open("join_taft.js", "r") as file:
    for i, line_local in enumerate(file):
        line = line_local.replace(f"{i} ", "")

        district_object = json.loads(line)

        print(district_object)

        districts.append(district_object)

print(districts)

print(json.dumps(districts[0]))

# Serializing json
json_object = json.dumps(districts[0], indent=4)

# Writing to sample.json
with open("join_taft.json", "w") as outfile:
    outfile.write(json_object)

with open("Join Texas AFT_links by school district.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, ["id", "union_id", "label", "link"])

    writer.writeheader()
    writer.writerows(districts[0])

