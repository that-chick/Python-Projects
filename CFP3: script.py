#Shipping Program

weight = 33

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20
  print( " Ground Shipping $ ", cost_ground)

# Ground Shipping Premium

cost_ground_premium = 120.00
print(" Ground Shipping Premium $ ", cost_ground_premium)

#Drone Shipping (duh)

if weight <= 2:
  cost_drone_shipping = weight * 4.50 + 0
elif weight <= 6:
  cost_drone_shipping = weight * 9.00 + 0
elif weight <= 10:
  cost_drone_shipping = weight * 12.00 + 0
else: 
  cost_drone_shipping = weight * 14.25 + 0
print(" Drone Shipping $", cost_drone_shipping)
