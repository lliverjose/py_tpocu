
inches_str = input('Enter rain fall = ')
area_str = input('Enter area covered in acre = ')

inches_float = float(inches_str)
area_float = float(area_str)

acre = 43560.0
cubit_f = 7.48051945

volume = (inches_float/12) * acre * area_float
gallons = volume * cubit_f

print('gallons = ', gallons)