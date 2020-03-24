from django.shortcuts import render
from django.http import HttpResponse
from glob import glob
from os import path
import yaml
from allauth.account.views import SignupView, LoginView
from labs.forms import *
from labs.models import *

def index(request):
    # Get list of directories in the templates folder. Each directory represents a course.
    courses = [x.split("/")[-2] for x in glob("./labs/templates/courses/*/")]
    courses_with_labs_count = {}
    for course in courses:
        # Count the labs for each course. Each subdirectory of the course directory is considered a lab if it has an index.yaml file.
         courses_with_labs_count[course] = len([x for x in glob("./labs/templates/courses/" + course + "/*/") if path.exists(x+"/index.yaml")])
    return render(request, 'index.html', {'courses': courses_with_labs_count})


def course(request, course_id):
    # Get the paths of labs for this course from its directory. Labs should have an index.yaml file.
    labs_paths = sorted([x for x in glob("./labs/templates/courses/" + course_id + "/*/") if path.exists(x+"/index.yaml")]) # x.split("/")[-2]
    labs = {}
    for lab in labs_paths:
        with open(lab+'/index.yaml') as f:
            dataMap = yaml.safe_load(f)
            # Set the key equal to lab directory name and the value equal to the content of the index file of the lab
            labs[lab.split("/")[-2]] = dataMap
    return render(request, 'course.html', {'course': course_id, 'labs': labs})

def lab(request, course_id, lab_id):
# Parse the index file and store it in a dictionary object
    with open("./labs/templates/courses/" + course_id + "/" + lab_id+'/index.yaml') as f:
        dataMap = yaml.safe_load(f)

    tasks = []
# Get the filenames for the intro, steps and finish
    intro = dataMap['details']['intro']['text'][0:-2]+'html'
    for item in dataMap['details']['steps']:
        tasks.append(item['text'][0:-2] + "html")
    finish = dataMap['details']['finish']['text'][0:-2]+'html'
# Convert the filenames from md extension to html. Our html files have the same names as the md files.
    return render(request, 'lab.html', {'course': course_id, 'lab': lab_id, 'tasks': tasks, 'intro': intro, 'finish': finish, 'data': dataMap})


class MySignupView(SignupView):
    template_name = 'signup.html'
    form_class = RegistrationForm
class MyLoginView(LoginView):
    template_name = 'login.html'