# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
twi_data_18_19_prepared = dataiku.Dataset("twi_data_18_19_prepared")
twi_data_18_19_prepared_df = twi_data_18_19_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# #### loading data

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
tweet_text = twi_data_18_19_prepared_df['tweet_text']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# #### first clean

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import codecs

clean_tweet_text = []
for text in tweet_text:
    # removing u from beginning of some text
    clean_text = text[1:] if text.startswith('u') else text
    # replace pair of single quotations with one single quotation
    clean_text = clean_text.replace("''","'")
    # removing quotations from around text
    clean_text = clean_text[1:-2] if clean_text.startswith("'") else clean_text
    # removing common from end of text
    clean_text = clean_text[:-1] if clean_text.endswith(",") else clean_text
    # unicode escaping lower case u (\u) characters
    try:
        clean_text = codecs.unicode_escape_decode(clean_text)[0] if clean_text.find('\\u') > -1 else clean_text
    except:
        pass
    # appending to list for next part
    clean_tweet_text.append(clean_text)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# #### second clean

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
good_enc_text = []
for t in clean_tweet_text:
    # changing all characters to unicode to unify
    s = codecs.unicode_escape_encode(t)[0]
    # removing the python added "b'" at the beginning generated from previous statement
    s = str(s)[2:]
    # removing double or triple backslash from some unicode characters
    # (this one took a while to find a solution for)
    s = s.replace('\\\\','\\').replace('\\\\','\\')
    # re-encoding text back into normal characters
    try:
        s = codecs.unicode_escape_decode(s)[0]
    except:
        pass
    # appending to list to re-import back into table
    good_enc_text.append(s)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
twi_data_18_19_prepared_df['tweet_text'] = good_enc_text

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_tweet_text_cleaned_df = twi_data_18_19_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_tweet_text_cleaned = dataiku.Dataset("Twi_Data_tweet_text_cleaned")
Twi_Data_tweet_text_cleaned.write_with_schema(Twi_Data_tweet_text_cleaned_df)