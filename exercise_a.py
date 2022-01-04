def find_all_duplicates(items:list):
    duplicates = []
    for item in items:
        if items.count(item) != 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Can you decrease the operational complexity of your code?
# R: yes I did it by thinking only in the tools that I had in mind
# could decrease the list length under the execution and check if the value has already extracted,
# turning the comparison or count less expensive
 