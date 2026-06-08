def beer_countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")


def main():
    bottles = int(input("Enter number of bottles: "))
    beer_countdown(bottles)
    print("Time to buy more bottles of beer.")


main()