##################
# Author : Sooraj Bharadwaj
# Date: 04/13/2022
#################
# IMPORTS
import wikipedia as wk
import json
import tkinter as tk
from tkhtmlview import HTMLLabel

def randomPageGenerator():

    """
    This function generates a random page from the wikipedia. 
    @param: None
    @return: json object with page and page.metadata
    """

    # wikipedia random title generator
    title = wk.random(pages=1)

    # search for the page
    page = wk.page(title)
    print(f"categories: {page.categories}")

    # Get meta info about the page
    try:
        page_meta = {
            'title' : title,
            'categories' : page.categories
        }
    except:
        raise ValueError("[ERROR] FAILURE IN RETRIEVING PAGE META INFO FROM WIKI..More exception handling to be developed")

    # Prepare return object
    ret = {
        'page' : page,
        'meta' : page_meta
    }

    return ret
    
def getCenterPoints(root, window_dim):
    """:
    This function returns the center points of the window
    @param: root, (window.len, window.width)
    @return: center_x, center_y
    """
    x_center = int(root.winfo_screenwidth()/2 - window_dim[0]/2)
    y_center = int(root.winfo_screenheight()/2 - window_dim[1]/2)

    return (x_center, y_center)


def displayPage(root, page_obj):
    """
        Display the rendered HTML page
    """


    html_label = HTMLLabel(root, html=page_obj['page'].html())
    html_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Above method works, but html is page is not rendered.
    # Try PyQT


def gui(page_obj):
    root = tk.Tk()
    root.title("Random Wikipedia Page")
    root.resizable(True, True)

    # Display the page title
    title_label = tk.Label(root, text=page_obj['meta']['title'])
    title_label.pack()

    # Determine window placement (center)
    centr = getCenterPoints(root, (800, 800))

    # Display the page
    #root.geometry(f"{centr[0]}x{centr[1]}+{centr[0]}+{centr[1]}")

    print(page_obj['page'].html())
    displayPage(root, page_obj)

    # # Create Read More button
    # read_more_btn = tk.Button(
    #                     root, 
    #                     text="Show this article",
    #                     command = displayPage(root, page_obj)
    #                 )

    # # Display Read More button
    # read_more_btn.pack(
    #                 side=tk.BOTTOM,
    #                 fill=tk.X,
    #                 expand=True
    #             )


    root.geometry(f"800x800+{centr[0]}+{centr[1]}")
    root.mainloop()


    