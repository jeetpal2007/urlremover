def remove_duplicate_links(input_file, output_file):
  """
  Reads links from an input file, removes duplicates, and saves them to an output file.

  Args:
      input_file: The path to the file containing the links.
      output_file: The path to the file where the unique links will be saved.
  """
  links_seen = set()
  unique_links = []

  with open(input_file, "r") as f:
    for line in f:
      link = line.strip()
      if link not in links_seen:
        links_seen.add(link)
        unique_links.append(link)

  with open(output_file, "w") as f:
    for link in unique_links:
      f.write(f"{link}\n")

# Get user input for file paths
input_file = input("Enter the path to the file containing duplicate links: ")
output_file = input("Enter the path to save the unique links: ")

# Remove and save unique links
remove_duplicate_links(input_file, output_file)

print(f"Successfully saved unique links to: {output_file}")
