Back when the Web was young, the assumption was that people would browse through Web sites.  HTTP was seen as a way to transfer information from servers to browsers, which (obviously) existed in order for people to read things.

Today, Web servers largely provide information not to humans, but rather to other programs. They provide this data in a variety of formats.  One of these formats is JSON ("JavaScript Object Notation").  Note that JSON is a format for text files.  It doesn't describe a data structure.  In order to actually use JSON data, you need to translate it from the JSON string into data structures in the language you're using -- such as Python.  Similarly, you can take data structures and turn them into JSON strings, in order for them to be manipulated in your language.

JSON is cross-platform; it's a rare language nowadays that cannot translate its data structures to JSON, and vice versa.  In Python, the "json" module provides us with this functionality.  

How can you get JSON from a remote site onto yours?  There are packages that come with Python, but I'd generally recommend using "requests", a fantastic library on PyPI.

Once you've retrieved data in JSON format, what can you do with it?  Just about anything you want; you can analyze it, rewrite it, or even output it into a different format.  For example, you can create a CSV file from a subset of the data that you downloaded.  The "csv" module in Python's standard library handles this very well.

For this week's exercise, you are to download information in JSON format about the 1,000 largest cities. I've put it on GitHub as:

    https://gist.github.com/reuven/77edbb0292901f35019f17edb9794358

but you should download the "raw" version, which is here:

    https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json

(Please don't even try to write down this URL.)

After you retrieve the data and decode the JSON into Python data structures, I want you to create a CSV file. That file, which should have tabs as delimiters (rather than commas), should include the following data from the JSON file:
City name
State name
City population
City size rank
More specifically: You should write a function that takes a URL and a filename. It'll download the JSON information from the URL, and then write it to the file specified.

Questions or comments?  Discuss them in the forum!

I'll be back on Monday with a solution.

Reuven