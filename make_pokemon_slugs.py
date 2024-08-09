import json
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Extract Pokemon slugs from JSON and save to a new file.")
parser.add_argument('input_file', type=str, help='The input JSON file containing the sprite locations.')
parser.add_argument('output_file', type=str, help='The output JSON file to save the Pokemon slugs.')

args = parser.parse_args()

# Load the original JSON data from the specified input file
with open(args.input_file, 'r') as file:
    data = json.load(file)

# Extract the sprite names from the "spriteLocations" dictionary
pokemon_slugs = list(data['spriteLocations'].keys())

# Write the extracted slugs to the specified output file
with open(args.output_file, 'w') as outfile:
    json.dump(pokemon_slugs, outfile, indent=4)

print(f"Pokemon slugs have been written to {args.output_file}.")
