
from .Models import Zones
all_zones =[]

def add_new_area(area_name, codenates):
    new_area = codenates +""+area_name
    return new_area

def add_new_zone(zone_id, new_area):
    new_zone = Zones(zone_id,new_area)
    all_zones.append(new_zone)
    return True


def submit():
    area_name = input("Enter your business location:")
    if area_name== new_zone:
        print("That location isn't in our database")
        continue
        codenates = input("Enter your business GPS coordinates separated by a comma:")
        else:
             break
    
    while True
    massages = input("What do you want to broadcast?")
    print("Your broadcast has been sent to residents of"+":"+new_zone)


if __name__ == '__main__':
    submit()


    
    