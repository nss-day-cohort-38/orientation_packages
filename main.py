from appliances import Refrigerator, Washer, AirConditioner
from furniture import Table

samsung = Refrigerator()
print("Current temperature in the refrigerator: ", samsung.temp)

kenmore = Washer()
kenmore.run_washer()

goodman = AirConditioner()
goodman.run_ac(75)

dining_table = Table()
dining_table.number_of_legs(7)
