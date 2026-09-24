den = "pondělí"

match den:
    case "pondělí":
        print("Začátek týdne")
    case "pátek":
        print("Už je víkend")
    case _:
        print("Běžný den")
