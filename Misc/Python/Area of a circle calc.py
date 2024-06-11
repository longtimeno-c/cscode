#calcuclaiton for area of a circle
#currently not working....

import time 

PI=3.14159

radius = int(input("Enter the radius of the circle in cm: "))

time.sleep(2)

print("Do you want to calculate the area or circumferance of the circle?")

time.sleep(1)

Q1 = input("Answer in Area or Circumferance")
print()
if Q1 == "Area":
    def circle_area(radius_in):
        area_out = PI * radius_in**2
        area = circle_area(radius)
        print("The area of the circle is", area)
        

elif Q1 == "area":
    def circle_area(radius_in):
        area_out = PI * radius_in**2
        area = circle_area(radius)
        print("The area of the circle is", area)


elif Q1 == "Circumferance":
    def circle_circum(radius_in):
        circum_out = PI * (radius_in + radius_in)
        circum = circle_circum(radius)
        print("The circumferance of the circle is", circum)


elif Q1 == "circumferance":
    def circle_circum(radius_in):
        circum_out = PI * (radius_in + radius_in)
        circum = circle_circum(radius)
        print("The circumferance of the circle is", circum)


else:
    def circle_circum(radius_in):
        circum_out = PI * (radius_in + radius_in)
        circum = circle_circum(radius)
        print("The circumferance of the circle is", circum)

