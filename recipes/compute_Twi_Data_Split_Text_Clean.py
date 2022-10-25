# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_cols_parsed = dataiku.Dataset("Twi_Data_cols_parsed")
Twi_Data_cols_parsed_df = Twi_Data_cols_parsed.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_Split_Text_Clean_df = Twi_Data_cols_parsed_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Split_Text_Clean = dataiku.Dataset("Twi_Data_Split_Text_Clean")
Twi_Data_Split_Text_Clean.write_with_schema(Twi_Data_Split_Text_Clean_df)
