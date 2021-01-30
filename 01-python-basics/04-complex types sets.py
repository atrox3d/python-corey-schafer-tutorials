#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
#   Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#
#################################################################################
#
# sets
#
cs_courses = {'history', 'math', 'physics', 'compsci'}
art_courses = {'history', 'math', 'art', 'design'}
print(f'cs_courses = {cs_courses})')                # cs_courses = {'math', 'physics', 'compsci', 'history'})
print(f'art_courses = {art_courses})')              # art_courses = {'math', 'art', 'history', 'design'})
#
# duplicate elimination
#
cs_courses = {'history', 'math', 'physics', 'compsci', 'math'}
print('adding another math to cs_courses...')
print(f'cs_courses = {cs_courses})')                # cs_courses = {'math', 'physics', 'compsci', 'history'})
#
#   existence
#
print(f"is math in cs_courses: {'yes' if 'math' in cs_courses else 'no'}")
    # is math in cs_courses: yes
#
# intersection
#
print('intersection:', cs_courses.intersection(art_courses))
    # intersection: {'math', 'history'}
#
# difference
#
print('difference:', cs_courses.difference(art_courses))
    #difference: {'physics', 'compsci'}
#
# union
#
print('union:', cs_courses.union(art_courses))
    # union: {'physics', 'art', 'compsci', 'design', 'math', 'history'}
