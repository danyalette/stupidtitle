
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
Weird Between Skin  
Some Adult  
A Extension Out No Drawer  
No Issue  
Benefit As Some Treat Against Some Extent  
Engine Among The Editor  
No Rent  
Some Bicycle During A Disk  
Risk At Senior  
No Seat By Fact With No Crazy  
Database Of Bank  
A National Like Classic Into The Sand  
A Passage  
Female Without No Island  
The Hall  
Nasty Against A Count  
One Mortgage About Brick  
One Wheel To Street  
Car  
The Age Into A Stage  
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
You  may supply your own nouns, articles or prepositions. For instance:
```
from stupidtitle import createTitle

cute_things = ["cutie", "hug", "fun", "beauty", "radiance", "love", "bunny", "cat", "kitten", "rainbow", "magical forest", "going skating", "silliness", "pink", "color", "frilly dress", "ballet class", "teacher", "apple", "little duck", "running", "jumping", "mouse", "home sweet home", "book", "crumpet", "tea", "powder puff", "party", "joy", "gift", "doll", "treat", "playtime", "candy", "celebration", "mutual respect", "sunny garden", "yard", "jumping rope", "sky", "sun"]

for i in range(20):
  print createTitle(nouns=cute_things)
```
generates:
```
Adoration Towards Hug  
Cutie To The Apple Without One Cutie  
One Ballet Class Among Bunny  
A Ballet Class Through No Teacher  
Cat Around A Teacher  
Love Through A Adoration  
No Love Without A Beauty  
Cat Among The Cutie  
Adoration  
The Silliness Towards Going Skating  
Teacher About Color  
One Fun With A Fun  
A Bunny  
Love  
Apple  
One Silliness  
One Silliness Out A Radiance  
Love  
One Pink  
No Cutie Before Ballet Class  
```


