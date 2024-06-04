from triang import Triangle

def main():
    t = Triangle(3, 4, 5, 30, 60, 90)
    print(t)
    print(t.area())
    print(t.perimeter())
    print(t.heights())
    print(t.kind())
    print(Triangle.get_counter())

if __name__ == "__main__":
    main()