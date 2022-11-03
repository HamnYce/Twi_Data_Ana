# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_no_links = dataiku.Dataset("Twi_Data_no_links")
Twi_Data_no_links_df = Twi_Data_no_links.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_place_name_cleaned_df = Twi_Data_no_links_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_place_name_cleaned = dataiku.Dataset("Twi_Data_place_name_cleaned")
Twi_Data_place_name_cleaned.write_with_schema(Twi_Data_place_name_cleaned_df)
