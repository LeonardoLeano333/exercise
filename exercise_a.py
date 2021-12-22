def find_all_duplicates(items:list):
    duplicates = []
    for item in items:
        if items.count(item) != 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates