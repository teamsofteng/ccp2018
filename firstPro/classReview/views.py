from django.views.generic import TemplateView
from django.shortcuts import render
from scheduleGen.models import Courses, CourseLinks, Majors

class home(TemplateView):
	template_name =  'classReview/index.html'
