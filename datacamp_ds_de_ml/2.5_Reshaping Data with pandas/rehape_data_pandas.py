# Introduction to Data Reshaping -----------------------------------------------------------------

'''
fifa_players

                name  age  height  weight nationality                 club
0       Lionel Messi   32     170      72   Argentina         FC Barcelona
1  Cristiano Ronaldo   34     187      83    Portugal             Juventus
2    Neymar da Silva   27     175      68      Brazil  Paris Saint-Germain
3          Jan Oblak   26     188      87    Slovenia      Atlético Madrid
4        Eden Hazard   28     175      74     Belgium          Real Madrid
'''

# Change the DataFrame so rows become columns and vice versa
fifa_transpose = fifa_players.set_index('name')[['height', 'weight']].transpose()

# Print fifa_transpose
print(fifa_transpose)

'''
name    Lionel Messi  Cristiano Ronaldo  Neymar da Silva  Jan Oblak  Eden Hazard
height           170                187              175        188          175
weight            72                 83               68         87           74
'''


'''
fifa_players

                name   movement  overall  attacking
0           L. Messi   shooting       92         70
1  Cristiano Ronaldo   shooting       93         89
2           L. Messi    passing       92         92
3  Cristiano Ronaldo    passing       82         83
4           L. Messi  dribbling       96         88
5  Cristiano Ronaldo  dribbling       89         84
'''

# Use the pivot method to get overall scores indexed by movement and identified by name
fifa_names = fifa_players.pivot(index= 'movement', columns= 'name', values= 'overall')

# Print fifa_names
print(fifa_names)

'''
name       Cristiano Ronaldo  L. Messi
movement                              
dribbling                 89        96
passing                   82        92
shooting                  93        92
'''

# Pivot fifa_players to get overall and attacking scores indexed by name and identified by movement
fifa_over_attack = fifa_players.pivot(index='name', 
                                     columns='movement', 
                                     values=['overall', 'attacking'])

# Print fifa_over_attack
print(fifa_over_attack)

'''
                    overall                  attacking                 
movement          dribbling passing shooting dribbling passing shooting
name                                                                   
Cristiano Ronaldo        89      82       93        84      83       89
L. Messi                 96      92       92        88      92       70
'''

# Drop the fifth row to delete all repeated rows
fifa_no_rep = fifa_players.drop(4, axis= 0)

# Print fifa_pivot
print(fifa_no_rep)

'''
                name   movement  overall  attacking
0           L. Messi   shooting       92         70
1  Cristiano Ronaldo   shooting       93         89
2           L. Messi    passing       92         92
3  Cristiano Ronaldo    passing       82         83
5  Cristiano Ronaldo  dribbling       89         84
'''


# default is mean for aggfunc
# Discard the fifth row to delete all repeated rows
fifa_drop = fifa_players.drop(4, axis= 0)

# Use pivot method to get all scores by name and movement
fifa_pivot = fifa_drop.pivot(index= 'name', columns= 'movement') 

# Print fifa_pivot
print(fifa_pivot)  

# Use pivot table to get all scores by name and movement
fifa_pivot_table = fifa_players.pivot_table(index='name', columns='movement', aggfunc='mean')
# Print fifa_pivot_table
print(fifa_pivot_table)

'''
                    overall                  attacking                 
movement          dribbling passing shooting dribbling passing shooting
name                                                                   
Cristiano Ronaldo        89      82       93        84      83       89
L. Messi                 88      92       92        97      92       70
                  attacking                    overall                 
movement          dribbling passing shooting dribbling passing shooting
name                                                                   
Cristiano Ronaldo      84.0    83.0     89.0        89      82       93
L. Messi               92.5    92.0     70.0        92      92       92
'''


# Use pivot table to show the count of players by club and nationality and the total count
players_country = fifa_players.pivot_table(index='nationality', 
                                    columns='club', 
                                    values='name', 
                                    aggfunc='count', 
                                    margins=True)

# Print players_country
print(players_country)

'''
club         FC Barcelona  Real Madrid  All
nationality                                
Brazil                  3            6    9
Croatia                 1            1    2
France                  5            3    8
Germany                 1            1    2
Uruguay                 1            1    2
All                    11           12   23
'''


'''
fifa_players

           club nationality  year  height  weight
0  FC Barcelona     Germany  2000     187      85
1  FC Barcelona     Germany  2010     189      87
2   Real Madrid     Croatia  2000     172      66
3   Real Madrid     Croatia  2010     173      68
4   Real Madrid     Germany  2000     183      76
5   Real Madrid     Germany  2010     185      77
6  FC Barcelona     Croatia  2000     184      78
7  FC Barcelona     Croatia  2010     185      76
'''

# Set the argument to get the maximum for each row and column
fifa_mean = fifa_players.pivot_table(index=['nationality', 'club'], 
                                     columns='year', 
                                     aggfunc='max', 
                                     margins=True)

# Print fifa_mean
print(fifa_mean)

'''
                         height           weight         
year                       2000 2010  All   2000 2010 All
nationality club                                         
Croatia     FC Barcelona    184  185  185     78   76  78
            Real Madrid     172  173  173     66   68  68
Germany     FC Barcelona    187  189  189     85   87  87
            Real Madrid     183  185  185     76   77  77
All                         187  189  189     85   87  87
'''

# Converting Between Wide and Long Format -----------------------------------------------------------------

'''
books_gothic

                        title       authors  num_pages  rating_count  rating          publisher
0           Wuthering Heights  Emily Bronte        322          2155    3.85      Penguin Books
1                Frankenstein  Mary Shelley        189          2452    4.31  Kaplan Publishing
2  The Picture of Dorian Gray   Oscar Wilde        187          3342    4.15            Pearson
'''

# Melt books_gothic using the title column as identifier 
gothic_melted = books_gothic.melt(id_vars='title')

# Print gothic_melted
print(gothic_melted)

'''
                         title      variable              value
0            Wuthering Heights       authors       Emily Bronte
1                 Frankenstein       authors       Mary Shelley
2   The Picture of Dorian Gray       authors        Oscar Wilde
3            Wuthering Heights     num_pages                322
4                 Frankenstein     num_pages                189
5   The Picture of Dorian Gray     num_pages                187
6            Wuthering Heights  rating_count               2155
7                 Frankenstein  rating_count               2452
8   The Picture of Dorian Gray  rating_count               3342
9            Wuthering Heights        rating               3.85
10                Frankenstein        rating               4.31
11  The Picture of Dorian Gray        rating               4.15
12           Wuthering Heights     publisher      Penguin Books
13                Frankenstein     publisher  Kaplan Publishing
14  The Picture of Dorian Gray     publisher            Pearson
'''


# Melt books_gothic using the title, authors, and publisher columns as identifier
gothic_melted_new = books_gothic.melt(id_vars=['title', 'authors', 'publisher'])

# Print gothic_melted_new
print(gothic_melted_new)

'''
                        title       authors          publisher      variable    value
0           Wuthering Heights  Emily Bronte      Penguin Books     num_pages   322.00
1                Frankenstein  Mary Shelley  Kaplan Publishing     num_pages   189.00
2  The Picture of Dorian Gray   Oscar Wilde            Pearson     num_pages   187.00
3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00
6           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
7                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31
8  The Picture of Dorian Gray   Oscar Wilde            Pearson        rating     4.15
'''

# Melt publisher column using title and authors as identifiers
publisher_melted = books_gothic.melt(id_vars=['title', 'authors'], value_vars='publisher')

# Print publisher_melted
print(publisher_melted)

'''
                        title       authors   variable              value
0           Wuthering Heights  Emily Bronte  publisher      Penguin Books
1                Frankenstein  Mary Shelley  publisher  Kaplan Publishing
2  The Picture of Dorian Gray   Oscar Wilde  publisher            Pearson
'''

# Melt rating and rating_count columns using title and authors as identifier
books_melted = books_gothic.melt(id_vars=['title', 'authors'], 
                                 value_vars=['rating', 'rating_count'])

# Print books_melted
print(books_melted)

'''
                        title       authors      variable    value
0           Wuthering Heights  Emily Bronte        rating     3.85
1                Frankenstein  Mary Shelley        rating     4.31
2  The Picture of Dorian Gray   Oscar Wilde        rating     4.15
3           Wuthering Heights  Emily Bronte  rating_count  2155.00
4                Frankenstein  Mary Shelley  rating_count  2452.00
5  The Picture of Dorian Gray   Oscar Wilde  rating_count  3342.00
'''


# Assign the name number to the new column containing the values
books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], 
                                  value_vars=['rating', 'rating_count'], 
                                  var_name='feature', 
                                  value_name='number')

# Print books_ratings
print(books_ratings)

'''
                        title       authors          publisher       feature    number
0           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
1                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31
2  The Picture of Dorian Gray   Oscar Wilde            Pearson        rating     4.15
3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00
'''



'''
golden_age

               title              authors         isbn13      isbn10  prefix13  prefix10
0   The Great Gatsby  F. Scott Fitzgerald  9780060098919  1572702567       978         1
1  The Short Stories     Ernest Hemingway  9780684837864   684837862       978         0
2  To the Lighthouse       Virginia Woolf  9780156030472   156030470       978         0
'''

# Reshape wide to long using title as index and version as new name, and extracting isbn prefix 
isbn_long = pd.wide_to_long(golden_age, 
                    stubnames='isbn', 
                    i='title', 
                    j='version')

# Print isbn_long
print(isbn_long)

'''
                           prefix13  prefix10              authors           isbn
title             version                                                        
The Great Gatsby  13            978         1  F. Scott Fitzgerald  9780060098919
The Short Stories 13            978         0     Ernest Hemingway  9780684837864
To the Lighthouse 13            978         0       Virginia Woolf  9780156030472
The Great Gatsby  10            978         1  F. Scott Fitzgerald     1572702567
The Short Stories 10            978         0     Ernest Hemingway      684837862
To the Lighthouse 10            978         0       Virginia Woolf      156030470
'''


# Reshape wide to long using title and authors as index and version as new name, and prefix and isbn as wide column prefixes
all_long = pd.wide_to_long(golden_age, 
                   stubnames=['isbn', 'prefix'], 
                   i=['title', 'authors'], 
                   j='version')

# Print all_long
print(all_long)

'''
                                                        isbn  prefix
title             authors             version                       
The Great Gatsby  F. Scott Fitzgerald 13       9780060098919     978
                                      10          1572702567       1
The Short Stories Ernest Hemingway    13       9780684837864     978
                                      10           684837862       0
To the Lighthouse Virginia Woolf      13       9780156030472     978
                                      10           156030470       0
'''


'''
books_brown

                  title     author  language_code language_name  publisher_code publisher_name
0     The Da Vinci Code  Dan Brown              0       english              12   Random House
1       Angels & Demons  Dan Brown              0       english              34   Pocket Books
2  La fortaleza digital  Dan Brown             84       spanish              43        Umbriel
'''

# Specify that wide columns have a suffix containing words
the_code_long = pd.wide_to_long(books_brown, 
                                stubnames=['language', 'publisher'], 
                                i=['author', 'title'], 
                                j='codes_names', 
                                sep='_', 
                                suffix='\w+')
# Print the_code_long
print(the_code_long)

'''
                                           language     publisher
author    title                codes_names                       
Dan Brown The Da Vinci Code    code               0            12
                               name         english  Random House
          Angels & Demons      code               0            34
                               name         english  Pocket Books
          La fortaleza digital code              84            43
                               name         spanish       Umbriel
'''



'''
books_hunger

                       language publication date  publication number  page number
title                                                                            
Los Juegos del Hambre   Spanish        5/25/2010                   2          374
Catching Fire           English        5/25/2012                   6          391
Il canto della rivolta  Italian         6/8/2015                   4          390
'''

books_hunger.reset_index(drop= False, inplace= True)

'''
                    title language publication date  publication number  page number
0   Los Juegos del Hambre  Spanish        5/25/2010                   2          374
1           Catching Fire  English        5/25/2012                   6          391
2  Il canto della rivolta  Italian         6/8/2015                   4          390
'''

# Reshape using title and language as index, feature as new name, publication and page as prefix separated by space and ending in a word
publication_features = pd.wide_to_long(books_hunger, 
                                       stubnames=['publication', 'page'], 
                                       i=['title', 'language'], 
                                       j='feature', 
                                       sep=' ', 
                                       suffix='\w+')

# Print publication_features
print(publication_features)

'''
                                         index publication   page
title                  language feature                          
Los Juegos del Hambre  Spanish  date         0   5/25/2010    NaN
                                number       0           2  374.0
Catching Fire          English  date         1   5/25/2012    NaN
                                number       1           6  391.0
Il canto della rivolta Italian  date         2    6/8/2015    NaN
                                number       2           4  390.0
'''



'''
books_dys

                      year  num_pages  average_rating  ratings_count
title                                                               
Fahrenheit 451-1953   1953        186            4.10          23244
1984-1949             1949        268            4.31          14353
Brave New World-1932  1932        123            4.30          23535
'''

# Split the index of books_dys by the hyphen 
books_dys.index = books_dys.index.str.split('-')

# Print books_dys
print(books_dys)

'''
                         year  num_pages  average_rating  ratings_count
title                                                                  
[Fahrenheit 451, 1953]   1953        186            4.10          23244
[1984, 1949]             1949        268            4.31          14353
[Brave New World, 1932]  1932        123            4.30          23535
'''

# Get the first element after splitting the index of books_dys
books_dys.index = books_dys.index.str.split('-').str.get(0)

'''
                 year  num_pages  average_rating  ratings_count
title                                                          
Fahrenheit 451   1953        186            4.10          23244
1984             1949        268            4.31          14353
Brave New World  1932        123            4.30          23535
'''

books_dys.index = books_dys.index.str.cat(author_list, sep='-')
print(books_dys.index)

'''
author_list
['Ray Bradbury', 'George Orwell', 'Aldous Huxley']

Index(['Fahrenheit 451-1953-Ray Bradbury', '1984-1949-George Orwell', 'Brave New World-1932-Aldous Huxley'], dtype='object', name='title')
'''


# Concatenate the title and subtitle separated by "and" surrounded by spaces
hp_books['full_title'] = hp_books['title'].str.cat(hp_books['subtitle'], sep =' and ') 

# Print hp_books
print(hp_books)

'''
          title                   subtitle                     authors  goodreads  amazon                                  full_title
0  Harry Potter     the Half-Blood Prince   J.K. Rowling/Mary GrandPré       4.57    4.52     Harry Potter and the Half-Blood Prince 
1  Harry Potter  the Order of the Phoenix   J.K. Rowling/Mary GrandPré       4.49    4.44  Harry Potter and the Order of the Phoenix 
2  Harry Potter    the Chamber of Secrets                 J.K. Rowling       4.42    4.37    Harry Potter and the Chamber of Secrets 
3  Harry Potter   the Prisoner of Azkaban   J.K. Rowling/Mary GrandPré       4.56    4.51   Harry Potter and the Prisoner of Azkaban 
4  Harry Potter        The Deathly Hallows  J.K. Rowling/Mary GrandPré       4.42    4.37        Harry Potter and The Deathly Hallows
5  Harry Potter      the Sorcerer's Stone   J.K. Rowling/Mary GrandPré       4.47    4.42      Harry Potter and the Sorcerer's Stone 
6  Harry Potter        the Goblet of Fire                 J.K. Rowling       4.56    4.51        Harry Potter and the Goblet of Fire 
'''

# Split the authors into writer and illustrator columns
hp_books[['writer', 'illustrator']] = hp_books['authors'].str.split('/', expand=True) 

# Print hp_books
print(hp_books)

'''
          title                   subtitle                     authors  goodreads  amazon                                  full_title        writer    illustrator
0  Harry Potter     the Half-Blood Prince   J.K. Rowling/Mary GrandPré       4.57    4.52     Harry Potter and the Half-Blood Prince   J.K. Rowling  Mary GrandPré
1  Harry Potter  the Order of the Phoenix   J.K. Rowling/Mary GrandPré       4.49    4.44  Harry Potter and the Order of the Phoenix   J.K. Rowling  Mary GrandPré
2  Harry Potter    the Chamber of Secrets                 J.K. Rowling       4.42    4.37    Harry Potter and the Chamber of Secrets   J.K. Rowling           None
...


hp_books['authors'].str.split('/')

0    [J.K. Rowling, Mary GrandPré]
1    [J.K. Rowling, Mary GrandPré]
2                   [J.K. Rowling]
3    [J.K. Rowling, Mary GrandPré]
4    [J.K. Rowling, Mary GrandPré]
5    [J.K. Rowling, Mary GrandPré]
6                   [J.K. Rowling]
Name: authors, dtype: object

'''

# Melt goodreads and amazon columns into a single column
hp_melt = hp_books.melt(id_vars=['full_title', 'writer'], 
                        var_name='source', 
                        value_vars=['goodreads', 'amazon'], 
                        value_name='rating')

# Print hp_melt
print(hp_melt)

'''
                                    full_title        writer     source  rating
0      Harry Potter and the Half-Blood Prince   J.K. Rowling  goodreads    4.57
1   Harry Potter and the Order of the Phoenix   J.K. Rowling  goodreads    4.49
...
7      Harry Potter and the Half-Blood Prince   J.K. Rowling     amazon    4.52
8   Harry Potter and the Order of the Phoenix   J.K. Rowling     amazon    4.44
...
'''


'''
books_sh

                               main_title version  number_pages  number_ratings
0    Sherlock Holmes: The Complete Novels   Vol I          1059           24087
1    Sherlock Holmes: The Complete Novels  Vol II           709           26794
2  Adventures of Sherlock Holmes: Memoirs   Vol I           334            2184
3  Adventures of Sherlock Holmes: Memoirs  Vol II           238            1884
'''

# Split main_title by a colon and assign it to two columns named title and subtitle 
books_sh[['title', 'subtitle']] = books_sh['main_title'].str.split(':', expand=True)

# Split version by a space and assign the second element to the column named volume
books_sh['volume'] = books_sh['version'].str.split(' ').str.get(1)

# Drop the main_title and version columns modifying books_sh
books_sh.drop(['main_title', 'version'], axis=1, inplace=True)

# Print books_sh
print(books_sh)

'''
   number_pages  number_ratings                          title              subtitle volume
0          1059           24087                Sherlock Holmes   The Complete Novels      I
1           709           26794                Sherlock Holmes   The Complete Novels     II
2           334            2184  Adventures of Sherlock Holmes               Memoirs      I
3           238            1884  Adventures of Sherlock Holmes               Memoirs     II
'''

# Reshape using title, subtitle and volume as index, name feature the new variable from columns starting with number, separated by undescore and ending in words 
sh_long = pd.wide_to_long(books_sh, stubnames='number', i=['title', 'subtitle', 'volume'], 
                  j='feature', sep='_', suffix='\w+')

# Print sh_long 
print(sh_long)

'''
                                                                   number
title                         subtitle             volume feature        
Sherlock Holmes                The Complete Novels I      pages      1059
                                                          ratings   24087
                                                   II     pages       709
                                                          ratings   26794
Adventures of Sherlock Holmes  Memoirs             I      pages       334
                                                          ratings    2184
                                                   II     pages       238
                                                          ratings    1884
'''

# Stacking and Unstacking DataFrames -----------------------------------------------------------------

'''
churn

   Area code  total_day_calls  total_day_minutes
0        408              116                204
1        408              109                287
2        415               84                 84
3        510               67                 50
'''

# Predefined list to use as index
new_index = [['California', 'California', 'New York', 'Ohio'], 
             ['Los Angeles', 'San Francisco', 'New York', 'Cleveland']]

# Create a multi-level index using predefined new_index
churn_new = pd.MultiIndex.from_arrays(new_index, names=['state', 'city'])

# Assign the new index to the churn index
churn.index = churn_new

# Print churn
print(churn)

'''
                          Area code  total_day_calls  total_day_minutes
state      city                                                        
California Los Angeles          408              116                204
           San Francisco        408              109                287
New York   New York             415               84                 84
Ohio       Cleveland            510               67                 50
'''

# Reshape by stacking churn DataFrame
churn_stack = churn.stack()

# Print churn_stack
print(churn_stack)

'''
state       city                            
California  Los Angeles    Area code            408
                           total_day_calls      116
                           total_day_minutes    204
            San Francisco  Area code            408
                           total_day_calls      109
                           total_day_minutes    287
New York    New York       Area code            415
                           total_day_calls       84
                           total_day_minutes     84
Ohio        Cleveland      Area code            510
                           total_day_calls       67
                           total_day_minutes     50
dtype: int64
'''


'''
churn

        state           city       night                       day              
                             total calls total minutes total calls total minutes
0  California    Los Angeles         116           204          85           107
1  California  San Francisco         109           287          90           167
2    New York       New York          84            84          75            90
3        Ohio      Cleveland          67            50          67           110
'''

# Set state and city as index modifying the DataFrame
churn.set_index(['state', 'city'], inplace=True)

# Print churn
print(churn)

'''
                               night                       day              
                         total calls total minutes total calls total minutes
state      city                                                             
California Los Angeles           116           204          85           107
           San Francisco         109           287          90           167
New York   New York               84            84          75            90
Ohio       Cleveland              67            50          67           110
'''

# level shows column level, (day, night = level 0, totals = level 1)
# Reshape by stacking
churn_stack = churn.stack(level=0)

# Print churn_stack
print(churn_stack)

'''
                                total calls  total minutes
state      city                                           
California Los Angeles   day             85            107
                         night          116            204
           San Francisco day             90            167
                         night          109            287
New York   New York      day             75             90
                         night           84             84
Ohio       Cleveland     day             67            110
                         night           67             50
'''

# Reshape by stacking the second level
churn_stack = churn.stack(level=1)

# Print churn_stack
print(churn_stack)

'''
                                        day  night
state      city                                   
California Los Angeles   total calls     85    116
                         total minutes  107    204
           San Francisco total calls     90    109
                         total minutes  167    287
New York   New York      total calls     75     84
                         total minutes   90     84
Ohio       Cleveland     total calls     67     67
                         total minutes  110     50
'''


'''
churn

time                               day                  night         
feature                  text messages total GB text messages total GB
state      city                                                       
California Los Angeles              20        5            30       10
           San Francisco            40        5           100        5
New York   New York                 50        2            20        9
Ohio       Cleveland               100        3            40        6
'''

# Stack churn by the feature column level
churn_feature = churn.stack(level='feature')

# Print churn_feature
print(churn_feature)

'''
time                                    day  night
state      city          feature                  
California Los Angeles   text messages   20     30
                         total GB         5     10
           San Francisco text messages   40    100
                         total GB         5      5
New York   New York      text messages   50     20
                         total GB         2      9
Ohio       Cleveland     text messages  100     40
                         total GB         3      6
'''

# Reshape the churn DataFrame by unstacking
churn_unstack = churn.unstack()

# Print churn_unstack
print(churn_unstack)

# Reshape churn by unstacking the second row level
churn_second = churn.unstack(level=1)

# Print churn_second
print(churn_second)



'''

churn

                              minutes  calls  charge
time  type          exited                          
day   International churn       184.5     97   31.37
      National      churn       129.1    137   21.95
night International churn       332.9     67   56.59
      National      no churn    110.4    103   18.77
eve   International no churn    119.3    117   20.28
      National      no churn    137.1     88   23.31
'''

# Reshape churn by unstacking the first row level
churn_first = churn.unstack(level=0)

# Print churn_zero
print(churn_first)

'''
                       minutes                calls               charge              
time                       day    eve  night    day    eve  night    day    eve  night
type          exited                                                                  
International churn      184.5    NaN  332.9   97.0    NaN   67.0  31.37    NaN  56.59
              no churn     NaN  119.3    NaN    NaN  117.0    NaN    NaN  20.28    NaN
National      churn      129.1    NaN    NaN  137.0    NaN    NaN  21.95    NaN    NaN
              no churn     NaN  137.1  110.4    NaN   88.0  103.0    NaN  23.31  18.77
'''

# Reshape churn by unstacking the second row level
churn_second = churn.unstack(level=1)

# Print churn_second
print(churn_second)

'''
                     minutes                  calls                 charge         
type           International National International National International National
time  exited                                                                       
day   churn            184.5    129.1          97.0    137.0         31.37    21.95
eve   no churn         119.3    137.1         117.0     88.0         20.28    23.31
night churn            332.9      NaN          67.0      NaN         56.59      NaN
      no churn           NaN    110.4           NaN    103.0           NaN    18.77
'''


'''
churn

year                               2019                   2020               
plan                            minutes voicemail data minutes voicemail data
exited   state      city                                                     
churn    California Los Angeles       0         1    2       1         1    5
no_churn California Los Angeles       0         1    3       1         0    2
churn    New York   New York          1         0    5       0         1    2
no_churn New York   New York          1         0    4       1         0    6
'''

# Switch the first and third row index levels in churn
churn_swap = churn.swaplevel(0, 2)

'''
year                               2019                   2020               
plan                            minutes voicemail data minutes voicemail data
city        state      exited                                                
Los Angeles California churn          0         1    2       1         1    5
                       no_churn       0         1    3       1         0    2
New York    New York   churn          1         0    5       0         1    2
                       no_churn       1         0    4       1         0    6
'''

# we can unstack index level from right side
# Reshape by unstacking the last row level 
churn_unstack = churn_swap.unstack()

# Print churn_unstack
print(churn_unstack)

'''
year                      2019                                               2020                                           
plan                   minutes          voicemail           data          minutes          voicemail           data         
exited                   churn no_churn     churn no_churn churn no_churn   churn no_churn     churn no_churn churn no_churn
city        state                                                                                                           
Los Angeles California       0        0         1        1     2        3       1        1         1        0     5        2
New York    New York         1        1         0        0     5        4       0        1         1        0     2        6
'''

# Unstack the first and second row level of churn
churn_unstack = churn.unstack(level=[0, 1])

# Stack the resulting DataFrame using plan and year
churn_py = churn_unstack.stack(['plan', 'year'])

# Switch the first and second column levels
churn_switch = churn_py.swaplevel(0, 1, axis=1)

# Print churn_switch
print(churn_switch)

'''
exited                          churn            no_churn         
state                      California New York California New York
...


state                      California New York California New York
exited                          churn    churn   no_churn no_churn
...
'''

# fill_value=0 when unstacking
# Unstack churn level and fill missing values with zero
churn = churn.unstack(level='churn', fill_value=0)

# Sort by descending voice mail plan and ascending international plan
churn_sorted = churn.sort_index(level=["voice_mail_plan", "international_plan"], 
                                ascending=[False, True])

# Print final DataFrame and observe pattern
print(churn_sorted)

'''
                                         total_day_calls        total_night_calls       
churn                                              False   True             False   True
state international_plan voice_mail_plan                                                
LA    No                 Yes                     100.000    0.0            84.250    0.0
NY    No                 Yes                     115.000    0.0           121.000    0.0
LA    Yes                Yes                      71.000    0.0           101.000    0.0
NY    Yes                Yes                     120.000    0.0            78.000    0.0
LA    No                 No                      106.818  100.0            96.909  119.0
NY    No                 No                       90.900   95.0           100.800  101.5
LA    Yes                No                       78.000   69.0            90.000  104.0
NY    Yes                No                      109.000   87.0            99.000  113.0
'''


# when stacking, it drops null automatically, otherwise use dropna
# Stack the level scope without dropping rows with missing values
churn_stack = churn.stack(level='scope', dropna=False)

# Fill the resulting missing values with zero
churn_fill = churn_stack.fillna(0)

# Print churn_fill
print(churn_fill)

'''
type              total_day_calls  total_night_calls
   scope                                            
LA international             23.0               30.0
   national                   0.0                0.0
NY international              8.0               34.0
   national                   0.0               24.0
CA international              8.0               34.0
   national                   0.0               24.0
'''

# Advanced Reshaping -----------------------------------------------------------------

'''
obesity

                               perc_obesity
country   biological_sex year              
Argentina Male           2005          21.5
          Female         2005          24.2
          Male           2015          26.8
          Female         2015          28.5
Japan     Male           2005           2.5
          Female         2005           2.6
          Male           2015           4.6
          Female         2015           3.6
Norway    Male           2005          17.6
          Female         2005          18.6
          Male           2015          23.0
          Female         2015          22.2
'''

# Unstack the first level and calculate the mean of the columns
obesity_general = obesity.unstack(level=0).mean(axis=1)

# Print obesity_general
print(obesity_general)

'''
biological_sex  year
Female          2005    15.133
                2015    18.100
Male            2005    13.867
                2015    18.133
dtype: float64
'''

# Unstack the third level and calculate the difference between columns
obesity_variation = obesity.unstack(level=2).diff(axis=1)

# Print obesity_variation
print(obesity_variation)

'''
obesity.unstack(level=2)

                         perc_obesity      
year                             2005  2015
country   biological_sex                   
Argentina Female                 24.2  28.5
          Male                   21.5  26.8
Japan     Female                  2.6   3.6
          Male                    2.5   4.6
Norway    Female                 18.6  22.2
          Male                   17.6  23.0


                         perc_obesity     
year                             2005 2015
country   biological_sex                  
Argentina Female                  NaN  4.3
          Male                    NaN  5.3
Japan     Female                  NaN  1.0
          Male                    NaN  2.1
Norway    Female                  NaN  3.6
          Male                    NaN  5.4
'''


'''
obesity

year                           1995                   2005                   2015          
                       perc_obesity variation perc_obesity variation perc_obesity variation
country biological_sex                                                                     
France  Female                 15.3       7.7         18.1       8.2         20.8      11.3
        Male                   12.8       7.6         16.9       8.4         21.5      11.8
Germany Female                 14.4       4.6         17.2       5.2         20.1       8.4
        Male                   14.4       5.1         18.7       5.9         23.6       9.8


obesity.stack()
Out[3]:

year                                 1995  2005  2015
country biological_sex                               
France  Female         perc_obesity  15.3  18.1  20.8
                       variation      7.7   8.2  11.3
        Male           perc_obesity  12.8  16.9  21.5
                       variation      7.6   8.4  11.8
Germany Female         perc_obesity  14.4  17.2  20.1
                       variation      4.6   5.2   8.4
        Male           perc_obesity  14.4  18.7  23.6
                       variation      5.1   5.9   9.8


obesity.stack().median(axis=1)

country  biological_sex              
France   Female          perc_obesity    18.1
                         variation        8.2
         Male            perc_obesity    16.9
                         variation        8.4
Germany  Female          perc_obesity    17.2
                         variation        5.2
         Male            perc_obesity    18.7
                         variation        5.9


obesity.stack().median(axis=1).unstack()

                        perc_obesity  variation
country biological_sex                         
France  Female                  18.1        8.2
        Male                    16.9        8.4
Germany Female                  17.2        5.2
        Male                    18.7        5.9
'''

# Stack the first level, get sum, and unstack the second level
obesity_sum = obesity.stack(level=0).sum(axis=1).unstack(level=1)

# Print obesity_max
print(obesity_sum)

'''
biological_sex  Female  Male
country year                
France  1995      23.0  20.4
        2005      26.3  25.3
        2015      32.1  33.3
Germany 1995      19.0  19.5
        2005      22.4  24.6
        2015      28.5  33.4
'''

# Stack country level, group by country and get the mean
obesity_mean = obesity.stack(level='country').groupby('country').mean()

# Print obesity_mean
print(obesity_mean)

'''
           perc_obesity
country                
Argentina        23.000
Brazil           16.733
France           17.567
'''


'''
obesity

     country  perc_obesity        bounds
0  Argentina          21.5  [15.4, 31.5]
1    Germany          22.3  [16.2, 32.4]
2      Japan           2.5    [1.1, 3.5]
3     Norway          23.0  [13.1, 33.0]
'''

# Explode the values of bounds to a separate row
obesity_bounds = obesity['bounds'].explode()

'''
0    15.4
0    31.5
1    16.2
...
3    33.0
Name: bounds, dtype: object
'''

# Merge obesity_bounds with country and perc_obesity columns of obesity using the indexes
obesity_final = obesity[['country', 'perc_obesity']].merge(obesity_bounds, right_index=True, left_index=True)

# Print obesity_final
print(obesity_final)

'''
     country  perc_obesity bounds
0  Argentina          21.5   15.4
0  Argentina          21.5   31.5
1    Germany          22.3   16.2
1    Germany          22.3   32.4
2      Japan           2.5    1.1
2      Japan           2.5    3.5
3     Norway          23.0   13.1
3     Norway          23.0   33.0
'''

# Transform the list-like column named bounds  
obesity_explode = obesity.explode('bounds')

'''
     country  perc_obesity bounds
0  Argentina          21.5   15.4
0  Argentina          21.5   31.5
1    Germany          22.3   16.2
1    Germany          22.3   32.4
2      Japan           2.5    1.1
2      Japan           2.5    3.5
3     Norway          23.0   13.1
3     Norway          23.0   33.0
'''

# Modify obesity_explode by resetting the index 
obesity_explode.reset_index(drop=True, inplace=True)

# Print obesity_explode
print(obesity_explode)

'''
inplace=False
     country  perc_obesity bounds
0  Argentina          21.5   15.4
0  Argentina          21.5   31.5
1    Germany          22.3   16.2
1    Germany          22.3   32.4
2      Japan           2.5    1.1
2      Japan           2.5    3.5
3     Norway          23.0   13.1
3     Norway          23.0   33.0

inplace=True
     country  perc_obesity bounds
0  Argentina          21.5   15.4
1  Argentina          21.5   31.5
2    Germany          22.3   16.2
3    Germany          22.3   32.4
4      Japan           2.5    1.1
5      Japan           2.5    3.5
6     Norway          23.0   13.1
7     Norway          23.0   33.0
'''


'''
obesity

        country  perc_obesity     bounds
0        France          14.5  11.4-25.5
1        Mexico          25.3  16.2-32.4
2         Spain          12.5   8.1-16.5
3  South Africa          11.3   9.1-20.1
'''

# Split the columns bounds using a hyphen as delimiter
obesity_split = obesity['bounds'].str.split('-')

'''
0    [11.4, 25.5]
1    [16.2, 32.4]
2     [8.1, 16.5]
3     [9.1, 20.1]
Name: bounds, dtype: object
'''

# Assign the result of the split to the bounds column
obesity_split = obesity.assign(bounds=obesity['bounds'].str.split('-'))

# Print obesity
print(obesity_split)

'''
        country  perc_obesity        bounds
0        France          14.5  [11.4, 25.5]
1        Mexico          25.3  [16.2, 32.4]
2         Spain          12.5   [8.1, 16.5]
3  South Africa          11.3   [9.1, 20.1]
'''

# Transform the column bounds in the obesity DataFrame
obesity_split = obesity.assign(bounds=obesity['bounds'].str.split('-')).explode('bounds')

# Print obesity_split
print(obesity_split)

'''
        country  perc_obesity bounds
0        France          14.5   11.4
0        France          14.5   25.5
1        Mexico          25.3   16.2
1        Mexico          25.3   32.4
2         Spain          12.5    8.1
2         Spain          12.5   16.5
3  South Africa          11.3    9.1
3  South Africa          11.3   20.1
'''


# Import the json_normalize function
from pandas import json_normalize

# Normalize movies and separate the new columns with an underscore 
movies_norm = json_normalize(movies, sep='_')
print(movies)
print(movies_norm)
# Reshape using director and producer as index, create movies from column starting from features
movies_long = pd.wide_to_long(movies_norm, stubnames='features', i=['director', 'producer'], j='movies', sep='_', suffix='\w+')

# Print movies_long
print(movies_long)

'''
[{'director': 'Woody Allen',
  'producer': 'Letty Aronson',
  'features': {'title': 'Magic in the Moonlight', 'year': 2014}},
 {'director': 'Niki Caro',
  'producer': 'Jason Reed',
  'features': {'title': 'Mulan', 'year': 2020}}]

      director       producer          features_title  features_year
0  Woody Allen  Letty Aronson  Magic in the Moonlight           2014
1    Niki Caro     Jason Reed                   Mulan           2020

                                                features
director    producer      movies                        
Woody Allen Letty Aronson title   Magic in the Moonlight
                          year                      2014
Niki Caro   Jason Reed    title                    Mulan
                          year                      2020
'''


# Normalize the JSON contained in movies
normalize_movies = json_normalize(movies)

'''
      director       producer                                           features
0  Woody Allen  Letty Aronson  [{'title': 'Magic in the Moonlight', 'year': 2...
1    Niki Caro     Jason Reed                 [{'title': 'Mulan', 'year': 2020}]
'''

# Specify the features column as the list of records 
normalize_movies = json_normalize(movies, record_path='features')

'''
                      title  year
0    Magic in the Moonlight  2014
1  Vicky Cristina Barcelona  2008
2         Midnight in Paris  2011
3                     Mulan  2020
'''

normalize_movies = json_normalize(movies, 
                                  record_path='features', 
                                  meta=['director', 'producer'])

'''
                      title  year     director       producer
0    Magic in the Moonlight  2014  Woody Allen  Letty Aronson
1  Vicky Cristina Barcelona  2008  Woody Allen  Letty Aronson
2         Midnight in Paris  2011  Woody Allen  Letty Aronson
3                     Mulan  2020    Niki Caro     Jason Reed
'''


# Define birds reading names and bird_facts lists into names and bird_facts columns 
birds = pd.DataFrame(dict(names=names, bird_facts=bird_facts))

# Print birds
print(birds)

'''
              names                                         bird_facts
0          Killdeer  {"Size" : "Large", "Color": "Golden brown", "B...
1  Chipping Sparrow  {"Size":"Small", "Color": "Gray-white", "Behav...
2     Cedar Waxwing  {"Size":"Small", "Color": "Gray-brown", "Behav...
'''

# Apply the function json.loads function to the bird_facts column
data_split = birds['bird_facts'].apply(json.loads).apply(pd.Series)

'''
    Size         Color                       Behavior         Habitat
0  Large  Golden brown      Runs swiftly along ground     Rocky areas
1  Small    Gray-white                Often in flocks  Open woodlands
2  Small    Gray-brown  Catch insects over open water           Parks
'''

# Remove the bird_facts column from birds
birds = birds.drop(columns='bird_facts')

# Concatenate the columns of birds and data_split
birds = pd.concat([birds, data_split], axis=1)

# Print birds
print(birds)

'''
              names   Size         Color                       Behavior         Habitat
0          Killdeer  Large  Golden brown      Runs swiftly along ground     Rocky areas
1  Chipping Sparrow  Small    Gray-white                Often in flocks  Open woodlands
2     Cedar Waxwing  Small    Gray-brown  Catch insects over open water           Parks
'''


# speed up process by converting to json then df
birds['bird_facts'].apply(json.loads).to_list()

'''
[{'Size': 'Large',
  'Color': 'Golden brown',
  'Behavior': 'Runs swiftly along ground',
  'Habitat': 'Rocky areas'},
 {'Size': 'Small',
  'Color': 'Gray-white',
  'Behavior': 'Often in flocks',
  'Habitat': 'Open woodlands'},
 {'Size': 'Small',
  'Color': 'Gray-brown',
  'Behavior': 'Catch insects over open water',
  'Habitat': 'Parks'}]
'''

# Convert birds_facts into a JSON 
birds_dump = json.dumps(birds_facts)

'''
[{"Size": "Large", "Color": "Golden brown", "Behavior": "Runs swiftly along ground", "Habitat": "Rocky areas"}, {"Size": "Small", "Color": "Gray-white", "Behavior": "Often in flocks", "Habitat": "Open woodlands"}, {"Size": "Small", "Color": "Gray-brown", "Behavior": "Catch insects over open water", "Habitat": "Parks"}]
'''

# Read the JSON birds_dump into a DataFrame 
birds_df = pd.read_json(birds_dump)

'''
    Size         Color                       Behavior         Habitat
0  Large  Golden brown      Runs swiftly along ground     Rocky areas
1  Small    Gray-white                Often in flocks  Open woodlands
2  Small    Gray-brown  Catch insects over open water           Parks
'''

# Concatenate the 'names' column of birds with birds_df 
birds_final = pd.concat([birds['names'], birds_df], axis=1)

'''
              names   Size         Color                       Behavior         Habitat
0          Killdeer  Large  Golden brown      Runs swiftly along ground     Rocky areas
1  Chipping Sparrow  Small    Gray-white                Often in flocks  Open woodlands
2     Cedar Waxwing  Small    Gray-brown  Catch insects over open water           Parks
'''