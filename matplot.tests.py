import matplotlib.pyplot as plt
import matplotlib
plt.figure()
plt.plot([1,2], [1,2])


# Option 2
# TkAgg backend
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# Option 3
# WX backend
manager = plt.get_current_fig_manager()
manager.frame.Maximize(True)
"""
print(matplotlib.get_backend())

#plt.show()
#plt.savefig('processed_images/matplot.tests.png')
