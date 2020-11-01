import json
import random
import sys

for i in range(int(sys.argv[1])):
  # print(json.dumps({"id": random.randint(1,10), "temp": random.randint(0,30)}))
  print(json.dumps({"id": i // (int(sys.argv[1]) // 10), "temp": random.randint(0,30)}))