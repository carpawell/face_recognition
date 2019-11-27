from signs import *
from sorting import set_num_of_standarts

import matplotlib

methods = ["hist", "dft", "dct", "scale", "gradient"]

visualize = True
show_images = True

set_num_of_standarts(6)

# for method in methods:
#     search(method, visualize=visualize)

search_optimal(visualize, show_images)
