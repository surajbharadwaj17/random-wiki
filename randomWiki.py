##################
# Author : Sooraj Bharadwaj
# Date: 04/13/2022
#################

# IMPORTS
import wikipedia as wk
import random
from util import *


if __name__ == "__main__":

    page_obj = randomPageGenerator()

    # Create a GUI window
    gui(page_obj)