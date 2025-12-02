temperatura = float(input("Introduce a temperatura actual en °C: "))

match temperatura:
    case t if t > 30:
        print(f"{t}°C é demasiada calor.")
    case t if t < 10:
        print(f"{t}°C vai moito frío.")
    case t:
        print(f"{t}°C é unha temperatura agradable.")