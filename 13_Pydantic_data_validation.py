"""
Pydantic for Data Validation — Practical Python Example
Pydantic is a Python library that validates incoming data against a defined schema. It checks types, required fields, constraints, and custom rules, 
making it useful for ETL pipelines, API ingestion, and data quality checks.

"""


""" Build your ETL validation script
       orders.csv
           |
           v
     EXTRACT (Pandas)
           |
           v
    TRANSFORM / VALIDATE
       (Pydantic)
           |
      +----+----+
      |         |
      v         v
   Valid      Invalid
   Records    Records
      |         |
      v         v
 validated   rejected
 orders.csv  orders.json
      |
      v
 SQL Server Staging
      |
      v
 Data Warehouse

"""

import logging 
from pathlib import Path 
import pandas as pd

from pydantic import BaseModel, Field, ConfigDict, ValidationError
from decimal import Decimal 
from typing import Literal 






# --------------------------------------------------
# 1. Configuration
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent 
DATA_DIR = BASE_DIR / "data"
FILE_DATA = DATA_DIR / "orders.csv"

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok= True)


logging.basicConfig(
    level=logging.INFO, 
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# 2. Define validation schema
# --------------------------------------------------

class Order(BaseModel): 
    model_config = ConfigDict(extra="forbid")

    order_id: int = Field(gt=0)
    customer_id: int = Field(gt= 0)
    product_name: str = Field(min_length=1)
    quantity: int = Field(ge=1)
    unit_price: Decimal = Field(gt=Decimal("0"))
    status: Literal["pending", "shipped", "cancelled"]


# --------------------------------------------------
# 3. Extract
# --------------------------------------------------

def extract_data(): 

    logger.info("Extracting orders from csv")

    df = pd.read_csv(FILE_DATA)

    logger.info("Extracted %s records", len(df))

    return df 



# --------------------------------------------------
# 4. Transform and Validate
# --------------------------------------------------
def validate_data(df):
    valid_records = []
    rejected_records = []

    for row_num, row in enumerate(df.to_dict(orient="records"),start=2):

        try: 
            order = Order.model_validate(row)
            valid_records.append(order.model_dump(mode='json'))


        except ValidationError as exc:

            rejected_records.append({
                "row_number": row_num,
                "record": row,
                "errors": exc.errors(include_url=False)
            })

            logger.warning(
                "Rejected row %s: %s",
                row_num,
                exc.error_count()
            )

    return valid_records, rejected_records

# --------------------------------------------------
# 5. Load
# --------------------------------------------------


def load_data(valid_orders, rejected_orders):

    valid_df = pd.DataFrame(valid_orders)

    valid_df.to_csv(OUTPUT_DIR / "validated_orders.csv", index= False)

    rejected_df = pd.DataFrame(rejected_orders)
    rejected_df.to_json(
        OUTPUT_DIR / "rejected_orders.json",
        orient= "records", 
        indent= 4, 
        default_handler= str
    )

    logger.info("Valid records: %s", len(valid_orders))
    logger.info("Rejected records: %s", len(rejected_orders))






# --------------------------------------------------
# 6. Pipeline execution
# --------------------------------------------------


def main():
    logger.info("Starting ETL pipeline")

    df = extract_data()
    
    vaild_orders, rejected_orders = validate_data(df)

    load_data(vaild_orders, rejected_orders)

    logger.info('ETL pipeline completed successfully')

if __name__ == "__main__":
    main()



