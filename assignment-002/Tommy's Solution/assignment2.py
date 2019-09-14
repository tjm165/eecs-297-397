import sys

def get_line_width(line):
    keyword = "width"
    line = line.strip()
    line = line[line.index(keyword) + len(keyword):]
    return int(''.join(filter(str.isdigit, line)))

def get_total_width_of_schema(schema_file_name):
    schema_file = open(schema_file_name, 'r')
    total_width = 0
    for line in schema_file:
        total_width += get_line_width(line) if line[0] != "#" else 0
    
    schema_file.close()
    return total_width

data_file_name = "assignment-002\example-002\data.txt"

print(get_total_width_of_schema("assignment-002\example-002\schema.txt"))






