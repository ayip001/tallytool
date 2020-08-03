import json

# convert category_mapping.json to python dict
f = open("category_mapping.json")
category_dict = json.loads(f.read())
# import the list file
f = open("list.txt")

# dict to store the final tally
result_dict = {}
# dict to store line details
details_dict = {}

# read each line of the input file
for line in f:
    # only loop through if current line has more than 1 space
    # to ignore empty lines and lines with only 1 number, usually the day of month
    linesplit = line.strip().split(" ")
    if len(linesplit) == 1:
        continue
    # check if current line has keywords indicated in categories dict
    # then categorize that line ("others" if not listed)
    category = [val for key,val in category_dict.items() if key in line]
    category.append("others")
    category = category[0]
    # check if final tally has at least one entry of current category to prevent error
    if category not in result_dict:
        result_dict[category] = 0;
        details_dict[category] = [];
    # add cost of current category to result tally
    result_dict[category] += int(linesplit[0])
    details_dict[category].append(line)

for key in result_dict:
    print (f"\n{key} total: {result_dict[key]}\n")
    print (f"{key} details:")
    for item in details_dict[key]:
        print(item)

print(f"\ntotal: {sum([result_dict[key] for key in result_dict])}")
f.close()
