from signs import *
from sorting import set_num_of_standards

methods = ["hist", "dft", "dct", "scale", "gradient"]

visualize = True
show_images = True

set_num_of_standards(6)

# for method in methods:
#     search(method, visualize=visualize)

search_optimal(visualize, show_images)
