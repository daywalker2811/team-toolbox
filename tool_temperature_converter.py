def celsius_to_fahrenheit(c: float):
    return ((c * 9) / 5) + 32


def fahrenheit_to_celsius(f: float):
    return ((f - 32) * 5) / 9


def run():
    choice = int(input("Convert (1) Celsius -> Fahrenheit or (2) Fahrenheit -> Celsius ?: "))
    if choice == 1:
        c = float(input("Temperature: "))
        f = celsius_to_fahrenheit(c)
        print(f"Temperature : {c}")
        print(f"{c}°C ={f}:.2y°F")
    elif choice == 2:
        f = float(input("Temperature: "))
        c = fahrenheit_to_celsius(f)
        print(f"Temperature : {f}")
        print(f"{c}°C ={f}°F")
    else:
        print("J'ai dit entre 1 et 2 pauvre type !")