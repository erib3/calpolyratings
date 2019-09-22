import os
import sys

sys.path.append('/home/ethan/cpratings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpratings.settings')

import django
django.setup()
from department_courses.models import Department

# Cal Poly Departments
departments = [
	("Aerospace Engineering", "AERO"),
	("Agribusiness", "AGB"),
	("Agricultural and Environmental Plant Sciences", "AEPS"),
	("Agricultural Communication", "AGC"),
	("Agricultural Education", "AGED"),
	("Agriculture", "AG"),
	("Animal Science", "ASCI"),
	("Anthropology",  "ANT"),
	("Architectural Engineering", "ARCE"),
	("Architecture", "ARCH"),
	("Art", "ART"),
	("Astronomy and Astrophysics", "ASTR"),
	("Biology",  "BIO"),
	("Biomedical Engineering", " BMED"),
	("BioResource and Agricultural Engineering", "BRAE"),
	("Botany", "BOT"),
	("Business", "BUS"),
	("Chemistry", "CHEM"),
	("Child Development", "CD"),
	("Chinese","CHIN"),
	("City and Regional Planning", "CRP"),
	("Civil Engineering", "CE"),
	("Communication Studies", "COMS"),
	("Computer Engineering", "CPE"),
	("Computer Science", "CSC"),
	("Construction Management","CM"),
	("Dairy Science", "DSCI"),
	("Dance", "DANC"),
	("Data Science", "DATA"),
	("Early Start English", "ESE"),
	("Early Start Math", "ESM"),
	("Earth Science",  "ERSC"),
	("Economics",  "ECON"),
	("Education",  "EDUC"),
	("Electrical Engineering",  "EE"),
	("Engineering",  "ENGR"),
	("English",  "ENGL"),
	("Environmental Design",  "EDES"),
	("Environmental Engineering",  "ENVE"),
	("Ethnic Studies",  "ES"),
	("Fire Protection Engineering", "FPE"),
	("Food Science and Nutrition",  "FSN"),
	("French", "FR"),
	("Geography", "GEOG"),
	("Geology", "GEOL"),
	("German",  "GER"),
	("Graduate Studies", "GS"),
	("Graduate Studies-Accounting", "GSA"),
	("Graduate Studies-Business",  "GSB"),
	("Graduate Studies-Economics", "GSE"),
	("Graduate Studies-Packaging", "GSP"),
	("Graphic Communication",  "GRC"),
	("Health",  "HLTH"),
	("History", "HIST"),
	("Honors Contract",  "HNRC"),
	("Honors", "HNRS"),
	("Industrial and Manufacturing Engineering",  "IME"),
	("Industrial Technology and Packaging", "ITP"),
	("Interdisciplinary Studies in Liberal Arts", "ISLA"),
	("Italian", "ITAL"),
	("Japanese", "JPNS"),
	("Journalism", "JOUR"),
	("Kinesiology", "KINE"),
	("Landscape Architecture", "LA"),
	("Liberal Arts and Engineering Studies", "LAES"),
	("Liberal Studies", "LS"),
	("Marine Science", "MSCI"),
	("Materials Engineering", "MATE"),
	("Mathematics", "MATH"),
	("Mechanical Engineering", "ME"),
	("Microbiology", "MCRO"),
	("Military Science Leadership", "MSL"),
	("Music", "MU"),
	("Natural Resources", "NR"),
	("Philosophy", "PHIL"),
	("Physical Education: Men", "PEM"),
	("Physical Education: Women", "PEW"),
	("Physical Science", "PSC"),
	("Physics", "PHYS"),
	("Political Science", "POLS"),
	("Psychology", "PSY"),
	("Recreation, Parks and Tourism Administration", "RPTA"),
	("Religious Studies", "RELS"),
	("Science and Mathematics", "SCM"),
	("Social Sciences", "SOCS"),
	("Sociology", "SOC"),
	("Soil Science", "SS"),
	("Spanish", "SPAN"),
	("Statistics", "STAT"),
	("Systems Integration Engineering", "SIE"),
	("Theatre", "TH"),
	("University Studies", "UNIV"),
	("Wine and Viticulture", "WVIT"),
	("Women's and Gender Studies", "WGS"),
	("World Languages and Cultures", "WLC"),
	]

def populate():
	for field in departments:
		dp = Department(name=field[0], abbreviation=field[1])
		dp.save()


# Start execution here!
if __name__ == '__main__':
  print("Starting department population script...")
  populate()
