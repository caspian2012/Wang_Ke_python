""" Question 6"""

# Construct function add_number.
def add_number(in_file_name, out_file_name):
    
    # Open file for reading and open file for writing.
    in_file = open(in_file_name,'r')
    out_file = open(out_file_name,'w')
    
    # Set initial line number to 1.
    line_num = 1
    
    # Write the file with adding a line number for each line recursively.
    for line in in_file:
        out_file.write('{}: {}'.format(line_num, line))
        line_num = line_num + 1

# Output the result when given an input.
add_number('sample_input.txt','sample_output.txt')
