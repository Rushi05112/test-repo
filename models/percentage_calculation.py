import logging
import pandas as pd

logger = logging.getLogger("Uknitee-py")

def Model_Object_Function(Input_Data: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    percentage between two tags
    """
    logger.info("Starting model execution")

    inputCols = ["TAGDATE", "114HC066.PV", "114F036C.PV"]
    outputCols = ["TAGDATE", "PERCENTAGE"]

    missingInputs = set(inputCols) - set(Input_Data.columns)
    if missingInputs:
        raise ValueError(f"Input_Data is missing the following columns: {missingInputs}")

    df = Input_Data.copy()
    df["PERCENTAGE"] = (df["114HC066.PV"]/df["114F036C.PV"]) * 100

    logger.info("Model execution completed successfully")
    return df[outputCols]
