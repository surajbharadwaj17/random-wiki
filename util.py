##################
# Author : Sooraj Bharadwaj
# Date: 04/13/2022
#################
# IMPORTS
import wikipedia as wk
import json
import tkinter as tk

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


    # Get meta info about the page
    page_meta = {
        'title' : title,
        'categories' : page.categories
    }

    # Prepare return object
    ret = {
        'page' : page,
        'meta' : page_meta
    }

    return ret
    

def gui(page_obj):
    root = tk.Tk()
    root.title("Random Wikipedia Page")

    # Display the page title
    title_label = tk.Label(root, text=page_obj['meta']['title'])
    title_label.pack()
    

    root.geometry("400x400")
    root.mainloop()

    