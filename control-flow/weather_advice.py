
# Ask the user to input the current weather 

weather_like = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_like == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_like == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_like == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

