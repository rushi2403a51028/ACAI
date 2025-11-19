def check_item(items, target):
    found = False
    for i in items:
        if i == target:
            found = True
            break
    return "Found" if found else "Not Found"

# Example usage
items = [10, 20, 30, 40, 50]
target = 30

result = check_item(items, target)
print(result)
