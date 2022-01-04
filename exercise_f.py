# 6) Write the code that animates “Zeno's Paradox of Achilles and the Tortoise” on an
# interface(terminal for python)(we would like to see the paradox demonstrated).
# draw a lines into finite half close to one line with maplotlib or pyplot
# 0 to 1

def zenos_achilles_n_tortoise(achilles_step=10, tortoise_step=1, max_iter=1000):
    achilles_position = 0
    tortoise_position = 100
    # for i in range(iterations):
    achilles_positions = []
    tortoise_positions = []
    i=0
    while(achilles_position< tortoise_position):
        achilles_position += achilles_step
        tortoise_position += tortoise_step
        achilles_positions.append(achilles_position)
        tortoise_positions.append(tortoise_position)
        if i >= 1000:
            break

    return (achilles_position, tortoise_position, achilles_positions, tortoise_positions)

# I tried to deliver it the fastes as I could I'm sorry for not make it visual;
# would use some kind of library as matplolib or plotly to make it;