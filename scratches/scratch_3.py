from collections import namedtuple
d = {"name": "joe", "age": 20}
d_named = namedtuple("Employee", d.keys())(**d)
print(d)
print(d_named)
