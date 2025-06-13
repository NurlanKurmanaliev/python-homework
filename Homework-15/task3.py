country_capitals={"USA" : "Washington, D.C.", "France" : "Paris", "Germany" : "Berlin", "Japan" : "Tokyo", "UK" : "London"}

country=input("Enter a country name: ")
if country == "USA":  #in country_capitals:
    print(f"{country_capitals[country]}")
elif country == "France":
     print(f"{country_capitals[country]}")
elif country == "Germany":
     print(f"{country_capitals[country]}")
elif country == "Japan":
     print(f"{country_capitals[country]}")
elif country == "UK":
     print(f"{country_capitals[country]}")
else:
    print("Type correct country")


