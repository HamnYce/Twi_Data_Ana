# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_cols_parsed = dataiku.Dataset("Twi_Data_cols_parsed")
Twi_Data_cols_parsed_df = Twi_Data_cols_parsed.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
tweet_text = Twi_Data_cols_parsed_df['text']
first_link = Twi_Data_cols_parsed_df['text_first_link']
second_link = Twi_Data_cols_parsed_df['text_second_link']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
tweet_text_clean = []
for text in tweet_text:
    clean_text = text
    if text[0] == "'" or text[0] == '"':
        clean_text = text[1:]
    if text[-1] == "'" or text[-1] == '"':
        clean_text = text[:-1]
    tweet_text_clean.append(clean_text)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
first_link_clean = []
for text in first_link:
    clean_text = text
    if type(clean_text) == str:
        if text[0] == "'" or text[0] == '"':
            clean_text = text[1:]
        if text[-1] == "'" or text[-1] == '"':
            clean_text = text[:-1]
    first_link_clean.append(clean_text)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
second_link_clean = []
for text in second_link:
    clean_text = text
    if type(clean_text) == str:
        if text[0] == "'" or text[0] == '"':
            clean_text = text[1:]
        if text[-1] == "'" or text[-1] == '"':
            clean_text = text[:-1]
    second_link_clean.append(clean_text)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_cols_parsed_df['text'] = tweet_text_clean
Twi_Data_cols_parsed_df['text_first_link'] = first_link_clean
Twi_Data_cols_parsed_df['text_second_link'] = second_link_clean

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_Split_Text_Clean_df = Twi_Data_cols_parsed_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Split_Text_Clean = dataiku.Dataset("Twi_Data_Split_Text_Clean")
Twi_Data_Split_Text_Clean.write_with_schema(Twi_Data_Split_Text_Clean_df)