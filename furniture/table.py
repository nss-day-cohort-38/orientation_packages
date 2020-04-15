class Table:
    def __init__(self):
        self.material = "wood"

    def number_of_legs(self, legs):
        self.leg_number = legs
        print(f"The table has {self.leg_number} legs.")
