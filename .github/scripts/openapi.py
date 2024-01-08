import os
import yaml

# Path to the nelmio_api_doc.yaml file
nelmio = '../../config/packages/nelmio_api_doc.yaml'

# Path to the new file
destination_path = '../../../openapi-redoc.yaml'

# Load the nelmio_api_doc.yaml file
try:
    with open(nelmio, 'r') as file:
        data = yaml.full_load(file)

    # Check if the file contains a nelmio_api_doc key
    if 'nelmio_api_doc' in data and 'documentation' in data['nelmio_api_doc']:
        # Write the documentation key in the new file
        with open(destination_path, 'w') as new_file:
            yaml.dump(data['nelmio_api_doc']['documentation'], new_file, sort_keys=False)
    else:
        print("The provided file does not contain a valid nelmio_api_doc key.")
except FileNotFoundError:
    print(f"File {nelmio} not found.")
