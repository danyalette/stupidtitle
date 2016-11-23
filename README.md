
# stupidtitle

A super rudimentary random title generator in python. Useful for generating sample data.

- [Examples](#examples)
- [Installation](#installation)
- [Usage](#usage)

## Examples
```
from stupidtitle import createTitle

for i in range(20):
  print createTitle()
```

generates:
```
Action And Independence
The Social Pain From One Direction
No Easy Judge During A Great Person
No Professional Around The Courage
Economic System And Transportation
A Shock
An Agency Against The Classic
A Comparison
A Little Menu
No Great Convert Towards A Bad Farm
A Man
A Feature
The Bad Tradition For Different Swimming
Possible Success Against An Easy Truck
Cat Over Full Candy
Black Mouth From The Extension
No Real Excitement
A Bad Obligation
The Great Buy
A Distribution
```

## Installation
`git clone git@github.com:danyalette/stupidtitle.git`  
`cd stupidtitle`  
If applicable, activate your project's virtualenv: `source path_to_venv/bin/activate`  
`pip install .`  

## Usage  
```
from stupidtitle import createTitle

book_title = createTitle()
```
You  may supply your own lists for the `nouns`, `articles`, `prepositions`, and `adjectives`. For instance:
```
from stupidtitle import createTitle

cute_things = ["cutie", "hug", "bunny", "cat", "kitten", "rainbow", "forest", "color", "dress", "ballet class", "teacher", "apple", "duck", "home", "book", "crumpet", "tea", "powder puff", "party", "gift", "doll", "treat", "playtime", "candy", "celebration", "garden", "sky", "sun", "angel", "rabbit", "family", "toy", "adventure"]
cute_adjectives = ["cute", "funny", "silly", "sleepy", "loving", "pink", "adorable", "goofy", "playful", "fun", "elegant", "exciting", "kind", "zany", "frilly", "amazing", "fuzzy", "quiet", "furry", "magical", "proud"]

for i in range(20):
  print createTitle(nouns=cute_things,adjectives=cute_adjectives)
```
generates:
```
Playful Apple
The Book And The Toy
Color About One Fun Garden And The Funny Sky
A Color During The Adorable Sun
A Loving Ballet Class On The Teacher
The Tea And The Fuzzy Ballet Class
The Funny Ballet Class About A Book
Some Kitten
Powder Puff To Some Celebration Of Silly Color
Kitten Over No Family Into Playful Cutie
The Apple Into The Doll
Cute Home
No Amazing Adventure
One Forest Without Home
The Kind Party Out The Proud Kitten
Some Fuzzy Dress
Dress
Cute Toy
Cutie
One Rabbit Towards The Fuzzy Kitten Under The Playful Sun
```


