# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GP2c2KY9Ax6pss08XqCnZxq8q-39jO2M
"""

import streamlit as st
import pandas as pd

def get_website_link():
    website_link = "https://courses.cs.washington.edu/courses/cse163/20wi/files/lectures/L04/bee-movie.txt"

    user_input = input("Do you want the link to a website? (yes/no): ").strip().lower()

    if user_input == "yes" or user_input == "no":
        print(f"Here is the link: {website_link}")
    else:
        print("Invalid input. Here's the link anyway: " + website_link)

get_website_link()