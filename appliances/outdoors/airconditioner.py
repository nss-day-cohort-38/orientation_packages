class AirConditioner:

    def __init__(self):
        self.set_temp = 68

# A function that calls itself is called a recursive function. See https://www.programiz.com/python-programming/recursion for more.
    def run_ac(self, current_temp):
        if current_temp > self.set_temp:
            current_temp -= 1 # current_temp = current_temp - 1
            print(f"Cooling... current temperature is {current_temp}")
            self.run_ac(current_temp)
