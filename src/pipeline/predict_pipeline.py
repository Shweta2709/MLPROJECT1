import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class predictpipeline:
    def __init__(self):
        pass


    class CustomData:
        def __init__( self,
            gender: str,
            race_eyhnicity: int,
            parental_level_of_education: int,
            lunch: str,
            test_prepration_course: str,
            reading_score: int,
            writing_score: int,)