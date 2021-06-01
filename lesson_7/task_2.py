#  Creating a dictionary.
#  Create a function called make_country, which takes in a country’s name
#  and capital as parameters. Then create a dictionary from those two,
#  with ‘name’ as a key and ‘capital’ as a parameter.
#  Make the function print out the values of the dictionary
#  to make sure that it works as intended.

def make_country(country_name, capital):
    print(dict(country_name=capital))


make_country('Ukraine', 'Kiev')


# **kwargs
def make_country_1(country_name_1, **kwargs):
    print(country_name_1, kwargs)


make_country_1('Ukraine', capital='Kiev', population=2967360, river='Dnepr')
