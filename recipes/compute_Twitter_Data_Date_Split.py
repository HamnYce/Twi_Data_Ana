# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twitter_Data_Proper = dataiku.Dataset("Twitter_Data_Proper")
Twitter_Data_Proper_df = Twitter_Data_Proper.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.
Twitter_Data_Proper_df['date'] = 
Twitter_Data_Date_Split_df = Twitter_Data_Proper_df # For this sample code, simply copy input to output


# Write recipe outputs
Twitter_Data_Date_Split = dataiku.Dataset("Twitter_Data_Date_Split")
Twitter_Data_Date_Split.write_with_schema(Twitter_Data_Date_Split_df)
