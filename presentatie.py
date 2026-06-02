def presenteer(invoer, totaal):
    for key, value in invoer.items():
        print(key, ":", value, "euro")
    print("=" * 25)
    print("Totaal", ":", totaal, "euro")