# 4. Calculate the cost of painting the following building’s walls (both interior andexterior).
#  You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
#        2. It is upper view of building.)


area = int(input("Enter the area : "))
interior_cost = int(input("Enter the interior cost : "))
exterior_cost = int(input("Enter the exterior cost : "))

inte_area = 8 * area
exte_area = 7 * area

inte_cost = inte_area * interior_cost
exte_cost = exte_area *  exterior_cost

total_cost = inte_cost + exte_cost

print(f"Cost of painting is : {total_cost}")
