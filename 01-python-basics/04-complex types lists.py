#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#
#################################################################################
# lists
courses = ['history', 'math', 'physics', 'compsci']
print(courses)                  # ['history', 'math', 'physics', 'compsci']
print(len(courses))             # 4
print(courses[3])               # compsci
print(courses[-1])              # compsci
print(courses[0:2])             # ['history', 'math']
print(courses[2:])              # ['physics', 'compsci']
############################################################################
#
# list methods
#
############################################################################
#
# inplace editing methods
#
courses.append('art')
print(courses)                  # ['history', 'math', 'physics', 'compsci', 'art']

courses.insert(0, 'cheffing')
print(courses)                  # ['cheffing', 'history', 'math', 'physics', 'compsci', 'art']

courses2 = ['art', 'education']
courses.insert(0, courses2)
print(courses)                  # [['art', 'education'], 'cheffing', 'history', 'math', 'physics', 'compsci', 'art']

courses = ['history', 'math', 'physics', 'compsci']
courses.extend(courses2)
print(courses)                  # ['history', 'math', 'physics', 'compsci', 'art', 'education']

art = courses.pop()
print(courses, art)             # ['history', 'math', 'physics', 'compsci', 'art'] education

courses.reverse()
print(courses)                  # ['art', 'compsci', 'physics', 'math', 'history']
original_courses = courses.copy()
courses.sort()
print(courses)                  # ['art', 'compsci', 'history', 'math', 'physics']
#
# non in place
#
courses = original_courses
sorted_courses = sorted(courses)
print(sorted_courses, courses)  # ['art', 'compsci', 'history', 'math', 'physics']
                                # ['art', 'compsci', 'physics', 'math', 'history']

nums = [1, 5, 2, 4, 3]
print(min(nums))                # 1
print(max(nums))                # 5
print(sum(nums))                # 15

print('compsci' in courses)     # True
print(courses.index('compsci')) # 1

for course in courses:
    print(course)               # art
                                # compsci
                                # physics
                                # math
                                # history

for index, course in enumerate(courses):
    print(index, course)        # 0 art
                                # 1 compsci
                                # 2 physics
                                # 3 math
                                # 4 history

#
# conversion to string (join)
#
course_string = ', '.join(courses)
print(course_string)            # art, compsci, physics, math, history
#
# conversion from strinf (split)
#
new_list = course_string.split(', ')
print(new_list)                 # ['art', 'compsci', 'physics', 'math', 'history']
