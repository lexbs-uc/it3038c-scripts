print("This is the status of your C: drive memory.")

import shutil

total, used, free = shutil.disk_usage("/")

print ("Total space: %d GB" % (total // (2**30)))

print ("Used space: %d GB" % (used // (2**30)))

print ("Remaining space: %d GB" % (free // (2**30)))
