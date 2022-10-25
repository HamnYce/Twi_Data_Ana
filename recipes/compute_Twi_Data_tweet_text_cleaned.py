# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
twi_data_18_19_prepared = dataiku.Dataset("twi_data_18_19_prepared")
twi_data_18_19_prepared_df = twi_data_18_19_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_tweet_text_cleaned_df = twi_data_18_19_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_tweet_text_cleaned = dataiku.Dataset("Twi_Data_tweet_text_cleaned")
Twi_Data_tweet_text_cleaned.write_with_schema(Twi_Data_tweet_text_cleaned_df)
