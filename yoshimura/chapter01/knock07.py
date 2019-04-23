
def template(x: int, y: str, z: float) -> str:
    return f"{x}時の{y}は{z}"


if __name__ == "__main__":
    print(template(12, "気温", 22.4))
