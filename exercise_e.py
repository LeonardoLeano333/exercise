# # Question:
# 5) A building has 100 floors. One of the floors is the highest floor an egg can be dropped
# from without breaking. If an egg is dropped from above that floor, it will break. If it is
# dropped from that floor or below, it will be completely undamaged and you can drop the
# egg again. Given two eggs, find the highest floor an egg can be dropped from without
# breaking, with as few drops as possible on the worst-case scenario.

# # answer:

# we admit that 100 100% of chance the egg will break;
# bi section algorithm with the eggs that can be cracked limitation
# first shot two shots: from de first flor 1 and the second one from the 50 (100/2 in the middle)
# if the none of than break the second shot will be in the upper part (100 -100/4) flor 75
# and so on util some of than break if any break i will shot the last egg one flor at a time


# vary 30, 60, 100

def find_egg_break_height(eggs=2, max_floor=100, break_flor=60):
    botton_flor = 0
    delta_floor = ""
    pass