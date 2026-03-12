# lambda function 
multiple = lambda x: x*2
# print(multiple(2))

add = lambda x, y : x + y

# print(add(2, 3))

# --------------------------

# lambda with map 

price = ['$45.5', "$9.99", "$100.00"]

func = lambda x: float(x.replace('$',''))

price_float = list(map(func, price))
# print(price_float)


# p = "$5"
# print(float(p.replace('$',"")))



# -------------------------------------

# lambda with filter 

prices = [10, 80 , 58, 35, 120]
# remove all prices lower than 40

prices_lower_than_40 = list(filter(lambda x : x > 40, prices))
# print(prices_lower_than_40)



students = [['maria', 85],
            ['kumar', 10],
            ['max', 60]]


# task : keep only students with scores higer than 70
# print(list(filter(lambda row : row[1] >70, students)))

# challenge keep only students with names starting with 'm'

filtered_studs = list(filter(lambda row: row[0].lower().startswith("m"), students))

# print(filtered_studs)
# name = 'maria'
# print(name.startswith("m"))



# ---------------------------------------------

# lambda with sorted
# sort by the values not by the names 
students_sorted = sorted(students, key= lambda row:row[1])
# print(students_sorted)


# -----------------------------------------------------



# list comprehension 

# loop + transformation + filtering in one line 




prices = [80, 20, 100]
# task : multiple only hig prices > 50
high_prices = [ p*2 for p in prices if p>50 ]
# print(high_prices)



domains = [
    "www.google.com",
    "openai.com",
    "localhost",
    "WWW.DATAWITHBARA.COM"
]

# TASK Normalize the domains into standard format 
domains_normalized = [domain.lower().replace('www.',"") # data transformation 
                      for domain in domains   # loop 
                      if '.' in domain       # filter
                    ]



domains_cleaned = [

    domain.lower() if domain.lower().startswith('www.')
    else "www."+domain
    for domain in domains
    if "." in domain
]
# print(domains_normalized)
# print(domains_cleaned)



# --------------------------------- 
# Real Data Engineering Use cases 


"""
1️⃣ Use Case: Cleaning & Normalizing Raw Data During ETL

Imagine you extract names from an ERP system with inconsistent formatting
During the transform phase, you want to:
 - Remove whitespace
 - Drop nulls
 - Capitalize the names
"""
raw_names = ["  ahmed  ", "Mona ", " Salma", None, "Ali"]
names_cleaned = [name.strip().capitalize() for name in raw_names if name] 

# print(names_cleaned)



"""
2️⃣ Use Case: Filtering Invalid Records from Staging

Your staging layer has product prices, but you only want valid positive integers:
"""


prices = ["100", "-40", "N/A", "250", "0", "invalid"]
prices_cleaned = [int(p) for p in prices if p.isdigit()]
valid_prices = [int(p) for p in prices if p.isdigit() and int(p) > 0]
# print(prices_cleaned)
# print(valid_prices)



"""
3️⃣ Use Case: Generating Columns for a Dataframe

You downloaded JSON logs:
"""
events = [
    {"event": "click", "user": 101},
    {"event": "view",  "user": 102},
]

# You want a quick list of user IDs:
users_ids = [event['user']  for event in events]
# print(users_ids)

"""
4️⃣ Use Case: Converting Raw CSV Rows into Dict Objects

CSV returns lines like:
"""

rows = [
    "102,TV,1200",
    "103,Laptop,6000"
]


products = [
    {'id': int(r[0]), 'product': r[1], 'price': int(r[2])} 
    for r in  (row.split(',') for row in rows)
    
]
print(products)
