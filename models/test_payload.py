
import logging
import pandas as pd
logger = logging.getLogger("Uknitee-py")

def Model_Object_Function(Input_Data: pd.DataFrame, **kwargs) -> pd.DataFrame:
    df = Input_Data.copy()
    df['OUTPUT'] = df["TagA"] - df["TagB"]
    return df[["TAGDATE", "OUTPUT"]]
