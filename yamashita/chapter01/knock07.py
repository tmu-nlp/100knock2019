from string import Template


def make_template(x, y, z):
    s = Template("$hour時の$targetは$value")
    return s.substitute(hour=x, target=y, value=z)


if __name__ == "__main__":
    print(make_template(12, "気温", 22.4))
