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
    upper_flor = max_floor
    current_flor = (upper_flor - botton_flor)//2 # 50
    flor_that_do_not_break = botton_flor
    while True:
        if eggs > 1:
            if current_flor >= break_flor:
                eggs -= 1 #break the egg
                print("egg breaked")
                current_flor = botton_flor
            else: #calculate
                botton_flor = current_flor
                upper_flor = current_flor + (upper_flor - current_flor)//2
                current_flor = upper_flor
        else:
            current_flor+=1
            if current_flor >= break_flor:
                eggs -= 1 #break the egg
                print("egg breaked")
            if eggs < 1:
                return current_flor -1


if __name__ == "__main__":
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=50)) # 49
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=60)) # 59
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=1)) # 0 
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=0)) # 0
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=5)) # 4
    print(find_egg_break_height(eggs=2, max_floor=100, break_flor=70)) # 69

# re ansering I had miss understood the question, in the question for me the 
# question asked for the higher that the egg does not break if the egg breaks
# at 50 the higher is not at 49 one level under 50? 
# and yes, it is the worst case
# Then, you have to try one by one from the first floor to 49th. That would make your worst case 50 drops.