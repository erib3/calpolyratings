from django import template

register = template.Library()


@register.filter
def toLetterGrade(value):
	grade_table = {-1:'', 0:'A+', 1:'A', 2:'A-', 3:'B+', 4:'B', 5:'B-', 6:'C+', 7:'C', 8:'C-', 9:'D', 10:'F'}
	return grade_table[int(value)]

@register.filter
def formatDifficultyGrade(value):
    if(value == -1):
        return ''
    return "Difficulty " + str(int(value)) + "/10"
