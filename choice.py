names = ['Sumran','Raj','Jassi','Sahil']
import random
from time import time
random.seed(time())
eliminated = random.choice(names)
print(eliminated)
