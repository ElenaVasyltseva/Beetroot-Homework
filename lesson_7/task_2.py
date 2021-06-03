#  Creating a dictionary.
#  Create a function called make_country, which takes in a country’s name
#  and capital as parameters. Then create a dictionary from those two,
#  with ‘name’ as a key and ‘capital’ as a parameter.
#  Make the function print out the values of the dictionary
#  to make sure that it works as intended.

info_capitals_of_country = {}


def make_country(country_name, capital, dict_func=info_capitals_of_country):
    dict_func[country_name] = capital
    return dict_func


print(make_country('Ukraine', 'Kiev'))
print(make_country('France', 'Paris'))
