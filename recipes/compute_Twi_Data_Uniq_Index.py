# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_Cleaned_Cols_Parsed = dataiku.Dataset("Twi_Data_Cleaned_Cols_Parsed")
Twi_Data_Cleaned_Cols_Parsed_df = Twi_Data_Cleaned_Cols_Parsed.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_Uniq_Index_df = Twi_Data_Cleaned_Cols_Parsed_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Uniq_Index = dataiku.Dataset("Twi_Data_Uniq_Index")
Twi_Data_Uniq_Index.write_with_schema(Twi_Data_Uniq_Index_df)
