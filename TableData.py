table_data = [['apples', 'oranges', 'cherries', 'banana', 'pears'],
              ['Alice', 'Bob', 'Carol', 'David', 'Mike'],
              ['dogs', 'cats', 'moose', 'goose', 'squirrel']]


def get_col_widths(name_of_table):
    col_widths = [0] * len(name_of_table)
    col_number = 0
    for internal_list in name_of_table:
        longest_string = 0
        for element in internal_list:
            if longest_string < len(element):
                longest_string = len(element)
        col_widths[col_number] = longest_string + 2
        col_number += 1
    return (col_widths)

def print_table(list_of_lists, left_width, right_widths):
    for element in range(len(list_of_lists[0])):
        for internal_list in list_of_lists:
            print(internal_list[element].rjust(right_widths[list_of_lists.index(internal_list)]), end ='')
        print('')


print_table(table_data, 0, get_col_widths(table_data))
