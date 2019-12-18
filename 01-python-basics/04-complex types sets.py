#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
#################################################################################
# sets
"""
"""
cs_courses = {'history', 'math', 'physics', 'compsci'}
art_courses = {'history', 'math', 'art', 'design'}
print(f'cs_courses = {cs_courses})')
print(f'art_courses = {art_courses})')
# duplicate elimination
cs_courses = {'history', 'math', 'physics', 'compsci', 'math'}
print('adding another math to cs_courses...')
print(f'cs_courses = {cs_courses})')
#
print(f"is math in cs_courses: {'yes' if 'math' in cs_courses else 'no'}")
# intersection
print('intersection:', cs_courses.intersection(art_courses))
# difference
print('difference:', cs_courses.difference(art_courses))
# union
print('union:', cs_courses.union(art_courses))
