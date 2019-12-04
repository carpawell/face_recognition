from signs import *
from sorting import set_num_of_standards

methods = ["hist", "dft", "dct", "scale", "gradient"]  # methods for LAB №3

visualize = True  # show graphs
show_images = True  # show images in optimal search

num_of_standards = 6  # set num of standards(training dataset) before executable cycle

set_num_of_standards(num_of_standards)

#  ======== LAB №3 ==========
# for method in methods:
#     search(method, visualize=visualize)


#  ======== LAB №4 ==========
search_optimal(visualize, show_images)
