from copy import deepcopy

def find_all_duplicates(items:list):
    inner_list = deepcopy(items)
    duplicates = []
    check_list = set()
    for item in items:
        if item in check_list and item not in duplicates:
            duplicates.append(item)
        else:
            check_list.add(item)

    # for item in items:
    #     if items.count(item) != 1 and item not in duplicates:
    #         duplicates.append(item)
    return duplicates

# Can you decrease the operational complexity of your code?
# R: yes I did it by thinking only in the tools that I had in mind
# could decrease the list length under the execution and check if the value has already extracted,
# turning the comparison or count less expensive

if __name__ == "__main__":

    print(find_all_duplicates([1,1,2]))
    print(find_all_duplicates([1,1,1,2]))
    print(find_all_duplicates(["a","a","a","b"]))
    
