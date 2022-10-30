# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_no_links = dataiku.Dataset("Twi_Data_no_links")
Twi_Data_no_links_df = Twi_Data_no_links.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# #### cleaning text_tweets

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# make new column that says place_name
place_names = []
# TODO: loop through text and extract 1 or 2 words after "I'm at"
for text in Twi_Data_no_links_df['tweet_text_clean']:
    split_text = text.split()
    if len(split_text) == 1:
        place_names.append(split_text[0])
    elif split_text[0] == "i'm" and split_text[1] == 'at':
        index = 4
        if 'in' in split_text:
            index = split_text.index('in')
        place_names.append(' '.join(split_text[2:index]))
    else:
        place_names.append("nu")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_no_links_df['place_text_name'] = place_names

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# #### Getting app name from the HTML

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
apps = Twi_Data_no_links_df['app']
clean_apps = []
try:
    for app in apps:
        app = apps[0].split(',')
        app_com_index = app.index('"com"')
        app = app[app_com_index - 1].strip('"')
        clean_apps.append(app)
except:
    print(app)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_no_links_df['app'] = clean_apps

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_Place_Name_From_Text_df = Twi_Data_no_links_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Place_Name_From_Text = dataiku.Dataset("Twi_Data_Place_Name_From_Text")
Twi_Data_Place_Name_From_Text.write_with_schema(Twi_Data_Place_Name_From_Text_df)