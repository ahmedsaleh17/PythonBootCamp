from faker import Faker 
from faker.providers import bank, credit_card, date_time, profile,currency, user_agent
import random 
import pandas as pd 
from collections import defaultdict 
import os 


def generate_data():
    fake = Faker()
    fake.add_provider(currency)

    fake_data = defaultdict(list)  #key 'string' , value list
  
    for _ in range(1000):
        fake_data['cart_id'].append(random.randint(0, 10))
        fake_data['customer_id'].append(random.randint(0, 10))
        fake_data['product_id'].append(random.randint(0, 10))
        fake_data['product_amount'].append(random.randint(1, 20))
        fake_data['product_price'].append(fake.pricetag())

    df_fake_data = pd.DataFrame(fake_data)
    print(df_fake_data.head())

    # print(fake_data)

if __name__ == "__main__":

    # generate_data()
    print(os.path.basename(__file__))


