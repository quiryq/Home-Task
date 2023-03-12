import os
print("Test a path exists or not:")
path = r'c:\\py\\pyForgit'
print(os.path.exists(path))
path = r'c:\\py\\pyForgit'
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))