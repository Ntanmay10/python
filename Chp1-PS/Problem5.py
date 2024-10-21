# Comment the problem4 appropriatly

import os

# Specify the directory path
directory = '/'  # For entire D drive
# directory = '/BCA' For entire BCA folder in D drive

# List all files and directories in the specified directory
contents = os.listdir(directory)

# Print each item in the directory
print(contents)
