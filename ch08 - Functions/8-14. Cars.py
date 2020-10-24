"""
Write a function that stores information about a car in a dictionary.
Make sure all the information was stored correctly
"""


def make_car(manufacturer, model, **car_info):
    """ Create a dictionary describing a car."""
    car_dict = {'manufacturer': manufacturer.title(), 'model': model.title()}
    # Order the dictionary
    for key, value in car_info.items():
        car_dict[key] = value
    return car_dict


build_car = make_car('ford', 'transit',
                     color='blue', doors='two',
                     weight='1200kg', height='1.9m')
print(build_car)
