# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_place_tweet_text = dataiku.Dataset("Twi_Data_place_tweet_text")
Twi_Data_place_tweet_text_df = Twi_Data_place_tweet_text.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
place_names = Twi_Data_place_tweet_text_df['place_name']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
stripped_place_names = []
for place in place_names:
    place = place.replace('"','').replace("'","")
    if place.endswith(','):
        place = place[:-1]
    stripped_place_names.append(place)
stripped_place_names

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import codecs
decoded_places = []
for place in stripped_place_names:
    place = codecs.unicode_escape_decode(place)[0]
    decoded_places.append(place)
decoded_places

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
cleaned_decoded = []
for place in decoded_places:
    if 'Ø' in place:
        cleaned_decoded.append('nu')
    else:
        cleaned_decoded.append(place)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_place_tweet_text_df['place_name'] = cleaned_decoded

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_Place_Name_Clean_df = Twi_Data_place_tweet_text_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Place_Name_Clean = dataiku.Dataset("Twi_Data_Place_Name_Clean")
Twi_Data_Place_Name_Clean.write_with_schema(Twi_Data_Place_Name_Clean_df)