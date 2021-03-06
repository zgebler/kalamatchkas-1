"""
kalamatchkas.config
saba pilots
description:  configuration file for kalamatchkas program
"""


# file of foods to load
FOOD_PATH = "C:/Users/Lucas/Documents/GitHub/kalamatchkas/sample/ingredient_doron v20.xlsx"

# file to output recipes
OUT_DIREC = "C:/Users/Lucas/Documents/GitHub/kalamatchkas/output"

# file for food list
FOOD_LIST = "C:/Users/Lucas/Documents/GitHub/kalamatchkas/sample/food_list.csv"

# string used to begin each printed line
LINE_BEGIN = ">*~@~*> "

# basic fields to compare/display for any diet
BASE_FIELDS = ["protein_cal_%","carb_cal_%","fat_cal_%","total_cal"]

# fields to update in recipe making file
FIELDS_DONT_UPDATE = ['food_id','serving_size','max_grams_meal','max_grams_day']

# api key for searching usda database
API_KEY = ""

# debug mode
DEBUG = False
