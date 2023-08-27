import csv
from faker import Faker

num_customers = 100

with open('customers.csv', 'w') as f:
  
  f.write('first_name,last_name,email\n')
  
  fake = Faker()

  for i in range(num_customers):  
    f.write(fake.first_name()+','+fake.last_name()+','+fake.email()+'\n')
      
print("Sample customer data generated")