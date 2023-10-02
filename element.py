class BiologicalBody:
    def __init__(self):
        self.elements = []

    def insert_element(self, element):
        self.elements.append(element)
        print(f"Inserted {element} into the biological body.")

# Define a class for an element that can be inserted
class Element:
    def __init__(self, name):
        self.name = name

# Create an instance of a biological body
human_body = BiologicalBody()

# Create some elements
adderall = Element("Dextroamphetamine")
oxygen = Element("Oxygen")
water = Element("Water")

# Insert elements into the biological body
human_body.insert_element(adderall)
human_body.insert_element(oxygen)
human_body.insert_element(water)

# Print the elements in the biological body
print("Elements in the biological body:")
for element in human_body.elements:
    print(element.name)

    # 609 754 4667 - TLF - 2021-09-22 - 11:00 - 11:30 - 30 min All American Inn -
    # fhjfhfjhfjhfjhfjfhjfhfjhfjhfjhfjfhjfhjfh