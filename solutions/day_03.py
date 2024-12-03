def main():
    with open("../data/day_03.txt", "r") as f:
        data = f.read()
        data = data.split("mul(")
        for d in data:
            mul = d.split(")")[0].split(",")
            print(mul)
    print(data)


if __name__ == "__main__":
    main()
