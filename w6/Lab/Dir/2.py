import os
print('Exist:', os.access('c:\\py\\pyForgit', os.F_OK))
print('Readable:', os.access('c:\\py\\pyForgit', os.R_OK))
print('Writable:', os.access('c:\\py\\pyForgit', os.W_OK))
print('Executable:', os.access('c:\\py\\pyForgit', os.X_OK))