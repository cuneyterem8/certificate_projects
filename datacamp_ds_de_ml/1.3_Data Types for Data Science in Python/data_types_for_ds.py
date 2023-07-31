# Fundamental Sequence Data Types -----------------------------------------------------------------

# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Find the position of 'Rowen': position
position = baby_names.index('Rowen')

# Remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

'''
['Ximena', 'Aliza', 'Ayden', 'Calvin', 'Sandeep']
'''

'''
records
[['2014', 'F', '20799', 'Emma'],
 ['2014', 'F', '19674', 'Olivia'],
 ['2014', 'F', '18490', 'Sophia'],
 ...
 ['2014', 'F', '6767', 'Brooklyn']]
'''

# Create the list comprehension: baby_names
baby_names = [row[3] for row in records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))

'''
['Abigail', 'Addison', 'Amelia', ... 'Victoria', 'Zoey']
'''


# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')

'''
Rank 1: Jada and Josiah
Rank 2: Emily and Ethan
Rank 3: Ava and David
Rank 4: Serenity and Jayden
Rank 5: Claire and Mason
'''


'''
top_ten_girl_names
[(1, 'Jada'),
 (2, 'Emily'),
 (3, 'Ava'),
 (4, 'Serenity'),
 (5, 'Claire'),
 (6, 'Sophia'),
 (7, 'Sarah'),
 (8, 'Ashley'),
 (9, 'Chaya'),
 (10, 'Abigail')]
'''

'''
Rank #: 1 - Jada
Rank #: 2 - Emily
Rank #: 3 - Ava
Rank #: 4 - Serenity
Rank #: 5 - Claire
Rank #: 6 - Sophia
Rank #: 7 - Sarah
Rank #: 8 - Ashley
Rank #: 9 - Chaya
Rank #: 10 - Abigail
'''


# The top ten boy names are:  as preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = ', and'

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")

'''
The top ten boy names are: Josiah, Ethan, David, Jayden, Mason, Ryan, Christian, Isaiah, Jayden, and Michael.
'''


# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)

'''
['Serenity', 'Sophia', 'Sarah', 'Sophia', 'Savannah', 'Serenity']
['Angela']
'''

# Dictionaries - The Root of Python -----------------------------------------------------------------

'''
squirrels
[('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
 ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')),
 ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
 ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
 ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
 ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
 ('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
 ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]
'''

'''
squirrels_by_park
{'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None),
 'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'),
 'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'),
 'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'),
 'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'),
 'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'),
 'Union Square Park': ('Gray', 'Black', 'Climbing', None),
 'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')}
'''

# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the names_by_rank alphabetically dict by park
for park in sorted(squirrels_by_park):
    # Print each park and it's value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')

'''
City Hall Park: ('Gray', 'Cinnamon', 'Eating', 'Approaches')
Highbridge Park: ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')
J. Hood Wright Park: ('Gray', 'White', 'Running', 'Indifferent')
Madison Square Park: ('Gray', None, 'Foraging', 'Indifferent')
Marcus Garvey Park: ('Black', 'Cinnamon', 'Cleaning', None)
Seward Park: ('Gray', 'Cinnamon', 'Eating', 'Indifferent')
Tompkins Square Park: ('Gray', 'Gray', 'Lounging', 'Approaches')
Union Square Park: ('Gray', 'Black', 'Climbing', None)
'''


# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))

'''
('Gray', 'Black', 'Climbing', None)
<class 'NoneType'>
Not Found
'''

'''
squirrels_madison
[{'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Sitting',
  'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': 'Cinnamon',
  'activities': 'Foraging',
  'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Climbing, Foraging',
  'interactions_with_humans': 'Indifferent'}]
'''

'''
squirrels_union
Out[4]:

('Union Square Park',
 [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Cinnamon',
   'activities': 'Climbing, Eating',
   'interactions_with_humans': None},
   ...
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None}])
'''

# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update the 'Union Square Park' key with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

'''
squirrels_by_park
{'Union Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Cinnamon',
   'activities': 'Climbing, Eating',
   'interactions_with_humans': None},
   ...
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Climbing, Foraging',
   'interactions_with_humans': 'Indifferent'}]}
'''

# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of all primary_fur_colors for squirrels in the park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])

'''
Union Square Park ['Gray', 'Gray', 'Cinnamon', 'Gray', 'Gray', 'Gray', 'Gray']
Madison Square Park ['Gray', 'Gray', 'Gray']
'''

# Remove "Madison Square Park" from squirrels_by_park and store it
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
print(squirrels_by_park)

'''
{'Tompkins Square Park': [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Approaches'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Climbing (down tree)', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}, {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Gray', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'}]}
'''

'''
squirrels_by_park
Out[2]:

{'Madison Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Sitting',
   'interactions_with_humans': 'Indifferent'}],
 'Union Square Park': [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Cinnamon',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Digging',
   'interactions_with_humans': 'Indifferent'}]}
'''

# Iterate over the first squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
    print(field, value)

'''
	primary_fur_color Gray
    highlights_in_fur_color None
    activities Foraging
    interactions_with_humans Indifferent
    -------------
    primary_fur_color Cinnamon
    highlights_in_fur_color None
    activities Foraging
    interactions_with_humans None
'''

# Check to see if Tompkins Square Park is in squirrels_by_park
if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
    print('Found Tompkins Square Park')

'''
Found Tompkins Square Park
'''

# Print a list of keys from the squirrels_by_park dictionary
print(squirrels_by_park.keys())

# Print the keys from the squirrels_by_park dictionary for 'Union Square Park'
print(squirrels_by_park['Union Square Park'].keys())

# Loop over the dictionary
for park_name in squirrels_by_park:
    # Safely print the park_name and the highlights_in_fur_color or 'N/A'
    print(park_name, squirrels_by_park[park_name].get('highlights_in_fur_color', 'N/A'))

'''
dict_keys(['J. Hood Wright Park', 'Stuyvesant Square Park', 'Highbridge Park', 'Tompkins Square Park', 'Union Square Park', 'City Hall Park', 'Msgr. McGolrick Park', 'John V. Lindsay East River Park'])
dict_keys(['primary_fur_color', 'activities', 'interactions_with_humans'])

J. Hood Wright Park Cinnamon
Stuyvesant Square Park Cinnamon
Highbridge Park White
Tompkins Square Park Gray
Union Square Park N/A
City Hall Park White
Msgr. McGolrick Park Cinnamon
John V. Lindsay East River Park Gray
'''

'''
squirrels_by_park['Union Square Park']['activities']
'Eating, Foraging'

squirrels_by_park['Union Square Park'].get('activities')
'Eating, Foraging'
'''

'''
squirrels_by_park["Union Square Park"]

[{'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Eating, Foraging',
  'interactions_with_humans': None},
 {'primary_fur_color': 'Cinnamon',
  'highlights_in_fur_color': None,
  'activities': 'Foraging',
  'interactions_with_humans': None},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Eating, Foraging',
  'interactions_with_humans': None},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Digging',
  'interactions_with_humans': 'Indifferent'}]
'''

# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if "Cinnamon" in squirrel["primary_fur_color"]])

'''
[{'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None, 'activities': 'Foraging', 'interactions_with_humans': None}]
'''

# Numeric Data Types, Booleans, and Sets -----------------------------------------------------------------

print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")

'''
1e-07
0.000010
0.000000
0.0000001
'''

'''
penguins
Out[1]:

[{'species': 'Adlie',
  'flipper_length': 190.0,
  'body_mass': 3050.0,
  'sex': 'FEMALE'},
 {'species': 'Adlie',
  'flipper_length': 184.0,
  'body_mass': 3325.0,
  'sex': 'FEMALE'},
  ...
 {'species': 'Gentoo',
  'flipper_length': 220.0,
  'body_mass': 6000.0,
  'sex': 'MALE'}]
'''

# Use a for loop to iterate over the penguins list
for penguin in penguins:
  # Check the penguin entry for a body mass of more than 3300 grams
  if penguin["body_mass"] > 3300:
  	# Print the species and sex of the penguin if true
    print(f"{penguin['species']} - {penguin['sex']}")

'''
Adlie - FEMALE
Gentoo - FEMALE
Adlie - MALE
'''

# Use a list comprehension to iterate over each penguin in penguins saved as female_species_list
# If the the sex of the penguin is 'FEMALE', return the species value
female_species_list = [penguin["species"] for penguin in penguins if penguin["sex"] == 'FEMALE']

# Create a set using the female_species_list as female_penguin_species.
female_penguin_species = set(female_species_list)

# Find the difference between female_penguin_species and male_penguin_species. Store the result as differences
differences = female_penguin_species.difference(male_penguin_species)

# Print the differences
print(differences)

'''
female_penguin_species
{'Adlie', 'Chinstrap', 'Gentoo'}

print(differences)
{'Chinstrap'}
'''

# Find the union: all_species
all_species = female_penguin_species.union(male_penguin_species)

# Print the count of names in all_species
print(len(all_species))

# Find the intersection: overlapping_species
overlapping_species = female_penguin_species.intersection(male_penguin_species)

# Print the count of species in overlapping_species
print(len(overlapping_species))

'''
3
2
'''

# Advanced Data Types -----------------------------------------------------------------

# Import the Counter object
from collections import Counter

# Create a Counter of the penguins sex using a list comp
penguins_sex_counts = Counter([penguin['Sex'] for penguin in penguins])

# Print the penguins_sex_counts
print(penguins_sex_counts)

'''
Counter({'MALE': 15, 'FEMALE': 5})
'''

penguins_species_counts = Counter([penguin['Species'] for penguin in penguins])

# Find the 3 most common species counts
print(penguins_species_counts.most_common(3))

'''
[('Chinstrap', 7), ('Adlie', 7), ('Gentoo', 6)]
'''

# Create an empty dictionary: female_penguin_weights
female_penguin_weights = {}

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Check to see if species is already in the dictionary
    if species not in female_penguin_weights:
        # Create an empty list for any missing species
        female_penguin_weights[species] = []
    # Append the sex and body_mass as a tuple to the species keys list
    female_penguin_weights[species].append((sex, body_mass))
    
# Print the weights for 'Adlie'
print(female_penguin_weights)

'''
{'Chinstrap': [('FEMALE', 3800.0)],
 'Adlie': [('FEMALE', 3450.0), ('FEMALE', 3550.0), ('FEMALE', 3175.0)],
 'Gentoo': [('FEMALE', 4300.0)]}
'''

# Import dataclass
from dataclasses import dataclass

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    flipper_length: int
    body_mass: int
    sex: str
        
    # Define a property that returns the body_mass / flipper_length
    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length


# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, flipper_length, body_mass, sex in weight_log:
    # Append a new WeightEntry instance to labeled_entries
    labeled_entries.append(WeightEntry(species, sex, body_mass, flipper_length))
    
# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])

'''
[23.91304347826087, 25.32751091703057, 24.0, 23.972602739726028, 20.476190476190474]
'''