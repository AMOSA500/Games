names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
