from copy import deepcopy
from math import floor
# 100/5, 150/7, 70/3
# 20, 21.428571428571427, 23.333333333333332 

def get_carrots_max_value(carrot_types: list[dict], capacity=36):
    # maximum rate price/weight
    carrot_types_with_rate = []
    for carrot_type in carrot_types:
        carrot_type_with_rate = deepcopy(carrot_type)
        carrot_type_with_rate.update({"rate": carrot_type_with_rate["price"]/carrot_type_with_rate["kg"]})
        carrot_types_with_rate.append(carrot_type_with_rate)

    # get the max rate index
    rate_values = list(map(lambda car: car["rate"], carrot_types_with_rate))
    max_rate_index = rate_values.index(max(rate_values))

    # calculate many max rate carrots
    many_max_rate_carrot = floor(capacity/carrot_types_with_rate[max_rate_index]["kg"])
    weight_remain = capacity - many_max_rate_carrot*carrot_types_with_rate[max_rate_index]["kg"]

    # put best rated carrots in bag
    carrots_in_bag = deepcopy(carrot_types_with_rate)
    carrots_in_bag[max_rate_index]["quantity"] = many_max_rate_carrot

    if weight_remain > 0:
        # get carrot with less weight to complete
        weights = list(map(lambda car: car["kg"], carrot_types_with_rate))
        less_weight = min(weights)
        less_weighted_index = weights.index(less_weight)
        less_weighted_quantity = 0
        while weight_remain > 0:
            weight_remain = weight_remain - less_weight
            less_weighted_quantity+=1

        # put less weighted carrots in bag
        carrots_in_bag[less_weighted_index]["quantity"] = less_weighted_quantity

    # put quantity in the others that there is no value
    for carrot_in_bag in carrots_in_bag:
        if not carrot_in_bag.get("quantity"):
            carrot_in_bag["quantity"] = 0

    return carrots_in_bag


if __name__ == "__main__":
    carrot_types = [{"kg": 5, "price": 100}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]
    res = get_carrots_max_value(carrot_types, capacity=36)
    print(res)
    # res = \
    # [{'kg': 5, 'price': 100, 'rate': 20.0, 'quantity': 0}, 
    # {'kg': 7, 'price': 150, 'rate': 21.428571428571427, 'quantity': 0},
    # {'kg': 3, 'price': 70, 'rate': 23.333333333333332, 'quantity': 12}]
    carrot_types = [{"kg": 1, "price": 10}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]
    res = get_carrots_max_value(carrot_types, capacity=37)
    print(res)
    # res = \
    # [{'kg': 1, 'price': 10, 'rate': 10.0, 'quantity': 1},
    # {'kg': 7, 'price': 150, 'rate': 21.428571428571427, 'quantity': 0},
    # {'kg': 3, 'price': 70, 'rate': 23.333333333333332, 'quantity': 12}]


# It is realy not optimized, I was studing some sort of algorithms:
# my first approaches for this kind of problems were:
# LSM, but i could not fegure it out how to adapt it
# anotter approach was Dijkstra for path optimization, but I could not adapt for this problem.
# So instead of tring and failing to optimize I tackle it as the better sell price and add for
# the vacant weight the lighter to fit.