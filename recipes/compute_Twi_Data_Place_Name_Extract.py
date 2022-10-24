# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_prepared = dataiku.Dataset("Twi_Data_prepared")
Twi_Data_prepared_df = Twi_Data_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# make new column that says place_name
place_names = []
# TODO: loop through text and extract 1 or 2 words after "I'm at"
for text in Twi_Data_prepared_df['tweet_text_clean']:
    split_text = text.lower().split()
    if split_text[0] == "i'm" and split_text[1] == 'at':
        place_names.append(''.join(split_text[2:4]))
    else:
        place_names.append(text)
    # TODO: split text
    # TODO: if first 2 elements are I'm and at then grab the next 2 words
    # TODO: work from there

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_Place_Name_Extract_df = Twi_Data_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Place_Name_Extract = dataiku.Dataset("Twi_Data_Place_Name_Extract")
Twi_Data_Place_Name_Extract.write_with_schema(Twi_Data_Place_Name_Extract_df)