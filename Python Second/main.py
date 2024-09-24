import os


main_dir = "ecommerce_data"
os.makedirs(main_dir, exist_ok=True)


subdirs = ["products", "customers", "orders"]
for subdir in subdirs:
    subdir_path = os.path.join(main_dir, subdir)
    os.makedirs(subdir_path, exist_ok=True)

print("Directories created successfully!")


def create_file_with_data(directory, filename, data):
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(directory, filename)

    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Write the data to the file
        file.write(data)

# Example usage
directory = "ecommerce_data/products"
filename = "product_list.txt"
data = "Cricket Ball , Football , Volleyball , Basetball"

create_file_with_data(directory, filename, data)