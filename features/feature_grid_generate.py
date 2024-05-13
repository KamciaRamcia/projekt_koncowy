import math

def calculateRowsQuantity(your_dictionary):
    elements_quanity = len(your_dictionary)*2
    row_quantity = math.ceil(math.sqrt(elements_quanity))
    if elements_quanity>36:  # maksymalnie jest 6 kolumn
        addtional_rows = math.ceil((elements_quanity -36)/6)
        row_quantity = row_quantity+addtional_rows
    return (row_quantity)


