
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
The Appeal Into A Sure Conflict
Temperature
No Major Balance
Reach Over One Special Confusion
One Small Exit Like A Better Weird
A Professor At Some Small Hotel
Paint With No Feed
Economic Topic With The Special Mix
Federal Habit From Early Battle
The Certain Block Against Public Sing
The Red Like The Pleasure
Right Paint On The Early Objective After Assistance
The Instruction Over A Social Blue
Long Farmer
Better Routine
No Code To The Right Menu As The Sure Assumption
A Contribution Against Analysis In A Sure Secretary
Recent Buddy Between A Internet
Low Shoe
Month
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

cute_things = ["cutie", "hug", "fun", "beauty", "radiance", "love", "bunny", "cat", "kitten", "rainbow", "forest", "going skating", "silliness", "color", "dress", "ballet class", "teacher", "apple", "duck", "running", "jumping", "mouse", "home sweet home", "book", "crumpet", "tea", "powder puff", "party", "joy", "gift", "doll", "treat", "playtime", "candy", "celebration", "mutual respect", "garden", "yard", "jumping rope", "sky", "sun"]
cute_adjectives = ["cute", "funny", "silly", "sleepy", "loving", "pink", "adorable", "goofy", "playful", "fun", "elegant", "exciting", "kind", "zany", "frilly", "amazing"]

for i in range(20):
  print createTitle(nouns=cute_things,adjectives=cute_adjectives)
```
generates:
```
Love Over A Sleepy Hug
Party
The Kind Duck
The Pink Running
Some Fun Party
A Kitten By The Kind Celebration
The Running With One Playful Celebration
The Celebration Towards A Mouse
The Pink Ballet Class Of Mouse
Running As The Color
Color Over Yard Around One Pink Tea
Frilly Silliness Into Sleepy Party
Pink Silliness About The Exciting Playtime Without Some Playful Forest
Some Silly Joy Without Some Ballet Class
The Elegant Mouse Among The Mutual Respect
No Adorable Forest
The Adorable Playtime Among A Adorable Playtime Like Some Book
The Kitten Over Gift
Powder Puff Over The Playful Joy
One Loving Ballet Class From Goofy Running
```


