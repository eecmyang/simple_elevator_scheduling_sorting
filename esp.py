import os



# relative path to the input file
directory = os.path.dirname(__file__)
file_name = os.path.join(directory, "input_file.txt")
print(file_name)


# reading input file and parsing the file
def reading_parsing_file(filename):
    unsort_list = []
    with open(filename, "r") as f:
        print("\nReading input file: ")
        for lines in f:
            replace_next_line = lines.replace("\n", "")
            print(replace_next_line)
            split_comma = replace_next_line.split(",")
            unsort_list.extend(split_comma)
            while "" in unsort_list:
                unsort_list.remove("")
    print(f"\nParsed input file:\n{unsort_list}\n")  
    
    return unsort_list


# extract the needed number values from the parsed data
def initial_ls_split(ls):    
    ls_1 = ls[1:15]
    ls_10 = ls[16:28]
    ls_5_up = ls[29:41]
    
    print("split lists:\n"\
          f"list_1 = {ls_1}\n"\
          f"list_10 = {ls_10}\n"\
          f"list_5_up = {ls_5_up}\n")
    
    return ls_1, ls_10, ls_5_up


#  converting/mappting the string list to integer list
def convert_list_str_to_int(map_1, map_10, map_5_up):
    mapping_1 = map(int, map_1)
    int_map_1 = list(mapping_1)
    
    mapping_10 = map(int, map_10)
    int_map_10 = list(mapping_10)

    mapping_5_up = map(int, map_5_up)
    int_map_5_up = list(mapping_5_up)

    print("converted into int list:\n"\
          f"list_1_int = {int_map_1}\n"\
          f"list_10_int = {int_map_10}\n"\
          f"list_5_up_int = {int_map_5_up}\n")

    return int_map_1, int_map_10, int_map_5_up


# extract floor numbers to new lists
def sort_for_floors(sorted_ls_1, sorted_ls_10, sorted_ls_5_up):
    init_1_flrs = []
    init_10_flrs = []
    init_5_up_flrs = []

    for floors in sorted_ls_1:
        if floors <= 10:
            init_1_flrs.append(floors)
    
    for floor in sorted_ls_10:
        if floor <= 10:
            init_10_flrs.append(floor)
    
    for floo in sorted_ls_5_up:
        if floo <= 10:
            init_5_up_flrs.append(floo)

    print("floors only:\n"\
          f"initial = 1 floors: {init_1_flrs}\n"\
          f"initial = 10 floors: {init_10_flrs}\n"\
          f"initial = 5 up floors: {init_5_up_flrs}\n")
    
    return init_1_flrs, init_10_flrs, init_5_up_flrs


# final sort
def final_sort(f_sort_1, f_sort_10, f_sort_5_up):
    init_1_sorted = f_sort_1[0:4] + \
                    sorted(f_sort_1[4:], reverse=True)

    descending_init_10 = sorted(f_sort_10, reverse=True)
    init_10_sorted = descending_init_10[0:2] + \
                     descending_init_10[4:6] + \
                     sorted(descending_init_10[2:4])

    descending_init_5_up = sorted(f_sort_5_up, reverse=True)
    init_5_up_sorted = descending_init_5_up[2:3] + \
                       sorted(descending_init_5_up[0:2], reverse=True) + \
                       sorted(descending_init_5_up[3:5]) + \
                       descending_init_5_up[5:6]
    init_5_up_sorted_f = init_5_up_sorted[0:4] + \
                         sorted(init_5_up_sorted[4:6])
    
    print("floor numbers of each initial:\n"\
          f"inital = 1: {init_1_sorted}\n"\
          f"inital = 10: {init_10_sorted}\n"\
          f"inital = 5 up: {init_5_up_sorted_f}\n")


    return init_1_sorted, init_10_sorted, init_5_up_sorted_f


# converting list to string
def ls_to_str(str_ls_1, str_ls_10, str_ls_5_up):
    init_1_str = ",".join(str(floors_1) for floors_1 in str_ls_1)
    init_10_str = ",".join(str(floors_10) for floors_10 in str_ls_10)
    init_5_up_str = ",".join(str(floors_5_up) for floors_5_up in str_ls_5_up)

    print("converted strings:\n"\
          f"initial_1_str: {init_1_str}\n"\
          f"initial_10_str: {init_10_str}\n"\
          f"initial_5_up_str: {init_5_up_str}\n")

    return init_1_str, init_10_str, init_5_up_str


# output result to txt file
def output_results(result_1, result_10, result_5_up):
    with open("output_results.txt", "w") as out:
        out.write("Output results:\n\n")
        out.write(f"Result_1 initial=1F：   {result_1}\n"\
                  f"Result_2 initial=10F：  {result_10}\n"\
                  f"Result_3 initial=5F up： {result_5_up}")

    print("Generated output_results.txt !\n")


if __name__ == "__main__":
    read_file = reading_parsing_file(file_name)
    into_lists = initial_ls_split(read_file)

    converting_lists = convert_list_str_to_int(into_lists[0],
                                               into_lists[1], 
                                               into_lists[2])

    floor_numbers = sort_for_floors(converting_lists[0],
                                    converting_lists[1],
                                    converting_lists[2])
    
    sorted_finally = final_sort(floor_numbers[0],
                                floor_numbers[1],
                                floor_numbers[2])

    convert_ls_to_str = ls_to_str(sorted_finally[0],
                                  sorted_finally[1],
                                  sorted_finally[2])
    
    output_results(convert_ls_to_str[0],
                   convert_ls_to_str[1],
                   convert_ls_to_str[2])
