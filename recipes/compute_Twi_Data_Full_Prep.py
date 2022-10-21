# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_prepared_with_visual_recipe = dataiku.Dataset("Twi_Data_prepared_with_visual_recipe")
Twi_Data_prepared_with_visual_recipe_df = Twi_Data_prepared_with_visual_recipe.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_Full_Prep_df = Twi_Data_prepared_with_visual_recipe_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Full_Prep = dataiku.Dataset("Twi_Data_Full_Prep")
Twi_Data_Full_Prep.write_with_schema(Twi_Data_Full_Prep_df)
