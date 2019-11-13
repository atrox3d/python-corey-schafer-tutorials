#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
#################################################################################
# lists
courses = ['history', 'math', 'physics', 'compsci']
print(courses)
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[2:])
#
# list methods
#
courses.append('art')
print(courses)
courses.insert(0, 'cheffing')
print(courses)
courses2 = ['art', 'education']
courses.insert(0, courses2)
print(courses)
courses = ['history', 'math', 'physics', 'compsci']
courses.extend(courses2)
print(courses)
art = courses.pop()
print(courses, art)
courses.reverse()
print(courses)
original_courses = courses.copy()
courses.sort()
print(courses)
courses = original_courses

sorted_courses = sorted(courses)
print(sorted_courses, courses)

nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))

print('compsci' in courses)
print(courses.index('compsci'))

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

course_string = ', '.join(courses)
print(course_string)

new_list = course_string.split(', ')
print(new_list)


