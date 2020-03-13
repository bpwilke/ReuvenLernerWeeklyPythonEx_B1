Hi, and welcome to the first installment of Weekly Python Exercise B1!

This week, we'll explore the built-in data types, seeing how we can store information in them, and then extract information from them, without having to create a new class.

I want you to create two different functions, collect_places and display_places.  Neither function takes an argument; instead, they will both work with a global variable, "visits".  (I'm purposely keeping quiet about my preferred type for "visits", so that you can think about it a bit.)

The idea is that we want to organize a list of places to which someone has traveled. That is: We'll ask the user to enter, one at a time, a city and country to which they have traveled. The city and country should be separated by a comma. If there is no comma, then the user is given an error message, and given another chance. If the user enters a city-country combination, then this information is recorded, and then they're asked again.  Indeed, the user is asked again and again for a city-country combination, until they provide an empty response. When that happens, the questioning phase ends, and the reporting phase begins.

In the report, we'll want to see a list of all of the places visited, organized by country. That is, we'll get a list of the visited countries, presented in alphabetical order, and for each country, we'll see a list of visited cities, also in alphabetical order.  If the city was visited more than once, then we'll see a number next to its name.

For example, this is how the interaction could look:
    Tell me where you went: New York, USA
    Tell me where you went: London, England
    Tell me where you went: Shanghai, China
    Tell me where you went: Chicago, USA
    Tell me where you went: Beijing, China
    Tell me where you went: Chicago, USA
    Tell me where you went: Beijing, China
    Tell me where you went: lalala
    That's not a legal city, country combination
    Tell me where you went: Boston, USA
    Tell me where you went: <user presses "enter" here>

    You visited:
    China
        Beijing (2)
        Shanghai
    England
        London
    USA
        Boston
        Chicago (2)
        New York
    
Questions or comments?  Just visit the forum.  (If you have problems logging in, let me know.)

I'll be back on Monday with a solution.

Until then,

Reuven

# Tests are below here
import solution
from io import StringIO
import sys

empty_place_inputs = StringIO('\n')
one_place_input = StringIO('London, England\n\n')
many_place_inputs = StringIO('''Shanghai, China
Beijing, China
Tel Aviv, Israel
Haifa, Israel
Madrid, Spain
Barcelona, Spain

''')


def test_no_places(monkeypatch):
    monkeypatch.setattr('sys.stdin', empty_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 0

def test_one_place(monkeypatch):
    monkeypatch.setattr('sys.stdin', one_place_input)
    solution.collect_places()
    assert len(solution.visits) == 1

def test_many_places(monkeypatch):
    monkeypatch.setattr('sys.stdin', many_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 3
   
def test_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('abcd\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip().startswith("Tell me where you went: That's not a legal city, country combination")
    assert captured_out.strip().endswith("Tell me where you went:")

def test_sorting_cities(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    beijing_index = captured_out.index('Beijing')
    shanghai_index = captured_out.index('Shanghai')
    assert beijing_index < shanghai_index

def test_sorting_countries(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Haifa, Israel\nLondon, England\nNew York, USA\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    israel_index = captured_out.index('Israel')
    england_index = captured_out.index('England')
    usa_index = captured_out.index('USA')
    assert england_index < israel_index
    assert israel_index < usa_index
                        

def test_counting(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert len(solution.visits['China']) == 2

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    assert 'Beijing (2)' in captured_out
    assert 'Shanghai' in captured_out