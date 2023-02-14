def volume(radius):
    p = 3.14
    vol = float(4/3 * p *radius*radius*radius)
    return vol
radius = int(input())
print(volume(radius)) 