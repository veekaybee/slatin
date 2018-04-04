# Slatin

lavic + Latin.  A simple transliterator from the Roman alphabet to Cyrillic. 

![russian](https://raw.githubusercontent.com/veekaybee/slatin/master/russian.png)

Why? Cyrillic is so hot right now. If we're going to troll, let's make sure we're trolling correctly. 

Inspired by [these tweets.](https://twitter.com/vboykis/status/981212453999665152) 

![russian](https://raw.githubusercontent.com/veekaybee/slatin/master/fb.png)

Background on [Russian transliteration.](https://en.wiktionary.org/wiki/Wiktionary:Russian_transliteration) 

## Under the Hood: 

[Python's Transliterate Package.](https://pypi.python.org/pypi/transliterate) 

## Example:

``` python
from transliterate import translit, get_available_language_codes
text = "Facebook"
print(translit(text,'ru'))
Фацебоок
```

It's not 100% accurate, but it's much, much better than randomness. 

 
## Getting started

Use the web app. To build the web app locally: 

## Instructions here






