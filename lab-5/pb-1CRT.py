resources =[
    [101,"laptop", "Electronics", 8],
    [102,"mouse", "Electronics", 5],
    [103,"keyboard", "Electronics", 10],
    [104,"chair", "Furniture", 15],
    [105,"table", "Furniture", 20],
    [106,"pen", "Stationery", 50],
    [107,"notebook", "Stationery", 30]
]

def display_resources(resources):
    if not resources:
        print("No resources available.")
        return
    for resource in resources:
        print(
            "ID:", resource[0],
            "Name:", resource[1],
            "Category:", resource[2],
            "Quantity:", resource[3]
        )

def search_by_category(resources, category):
    found = False
    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True
    if not found:
        print("No resources found in the category:", category)

def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True
    if not found:
        print("All resources are available.")

print("All Resources:")
display_resources(resources)

print("\nSearching for Electronics:")
search_by_category(resources, "Electronics")

print("\nSearching for unavailable resources:")
find_unavailable(resources)