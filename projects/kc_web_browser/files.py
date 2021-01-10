f = open('graphics lesson.txt')
print(f.read())

with open('graphics lesson.txt') as d:
    print(d.readline(3))
#
# R: The default mode. This opens a file for reading.
# W: The write mode. This opens a file for writing, creates a new file if the file does not exist, and overwrites the content if the file already exists.
# X: This creates a new file. The operation fails if the file exists.
# A: This opens a file in append mode, and creates a new file if a file does not exist.
# B: This opens a file in binary mode.
