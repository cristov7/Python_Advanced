def forecast(*locations_with_weather_tuple):
    output_list = []

    def add_locations(current_weather):
        locations_list = []
        for location, weather in locations_with_weather_tuple:
            if weather == current_weather:
                locations_list.append(location)
        locations_list.sort()
        for current_location in locations_list:
            output = f"{current_location} - {current_weather}"
            output_list.append(output)

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")
    return "\n".join(output_list)


# def forecast(*locations_with_weather_tuple):
#     def sorting_function():
#         current_sorted_dict = {}
#         locations_with_sunny_weather_list.sort()
#         locations_with_cloudy_weather_list.sort()
#         locations_with_rainy_weather_list.sort()
#         for current_location in locations_with_sunny_weather_list:
#             current_sorted_dict[current_location] = "Sunny"
#         for current_location in locations_with_cloudy_weather_list:
#             current_sorted_dict[current_location] = "Cloudy"
#         for current_location in locations_with_rainy_weather_list:
#             current_sorted_dict[current_location] = "Rainy"
#         return current_sorted_dict
#
#     def output_function():
#         current_output_list = []
#         for current_location, current_weather in sorted_dict.items():
#             current_output = f"{current_location} - {current_weather}"
#             current_output_list.append(current_output)
#         return current_output_list
#
#     locations_with_sunny_weather_list = []
#     locations_with_cloudy_weather_list = []
#     locations_with_rainy_weather_list = []
#     for info_tuple in locations_with_weather_tuple:
#         location = info_tuple[0]
#         weather = info_tuple[1]
#         if weather == "Sunny":
#             locations_with_sunny_weather_list.append(location)
#         elif weather == "Cloudy":
#             locations_with_cloudy_weather_list.append(location)
#         else:   # elif weather == "Rainy":
#             locations_with_rainy_weather_list.append(location)
#     sorted_dict = sorting_function()
#     output_list = output_function()
#     return "\n".join(output_list)


# def forecast(*locations_with_weather_tuple):
#     def sorting_function():
#         sorted_locations_with_sunny_weather_dict = dict(sorted(locations_with_sunny_weather_dict.items()))
#         sorted_locations_with_cloudy_weather_dict = dict(sorted(locations_with_cloudy_weather_dict.items()))
#         sorted_locations_with_rainy_weather_dict = dict(sorted(locations_with_rainy_weather_dict.items()))
#         sorted_locations_with_sunny_weather_dict.update(sorted_locations_with_cloudy_weather_dict)
#         sorted_locations_with_sunny_weather_dict.update(sorted_locations_with_rainy_weather_dict)
#         return sorted_locations_with_sunny_weather_dict
#
#     def output_function():
#         current_output_list = []
#         for current_location, current_weather in sorting_dict.items():
#             current_output = f"{current_location} - {current_weather}"
#             current_output_list.append(current_output)
#         return current_output_list
#
#     locations_with_sunny_weather_dict = {}
#     locations_with_cloudy_weather_dict = {}
#     locations_with_rainy_weather_dict = {}
#     for info_tuple in locations_with_weather_tuple:
#         location = info_tuple[0]
#         weather = info_tuple[1]
#         if weather == "Sunny":
#             locations_with_sunny_weather_dict[location] = weather
#         elif weather == "Cloudy":
#             locations_with_cloudy_weather_dict[location] = weather
#         else:   # elif weather == "Rainy":
#             locations_with_rainy_weather_dict[location] = weather
#     sorting_dict = sorting_function()
#     output_list = output_function()
#     return "\n".join(output_list)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))


# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))


# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
