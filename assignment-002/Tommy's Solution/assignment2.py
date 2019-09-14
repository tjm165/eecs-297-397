import sys

def get_line_width(line):
    keyword = "width"
    line = line[line.index(keyword) + len(keyword):]
    return int(''.join(filter(str.isdigit, line)))

def get_total_width_of_schema(schema_file_name):
    schema_file = open(schema_file_name, 'r')
    total_width = 0
    for line in schema_file:
        total_width += get_line_width(line) if line[0] != "#" else 0
    
    schema_file.close()
    return total_width

def read_data(data_file_name, line_width):
    data_file = open(data_file_name, 'r')
    num_lines_with_line_width = 0
    num_lines_without_line_width = 0

    for line in data_file:
        if len(line) == line_width - 1:
            num_lines_with_line_width += 1
        else:
            num_lines_without_line_width += 1
        print(len(line))
    return num_lines_with_line_width, num_lines_without_line_width

total_width = get_total_width_of_schema("assignment-002\example-002\schema.txt")
print(read_data("assignment-002\example-002\data.txt", total_width))





