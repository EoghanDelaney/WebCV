from django.shortcuts import render

# Create your views here.
def cv_an(request):
    context = {'job1': 'Data Analyse', 'job2': 'Mechanical Estimator'}
    return render(request, 'analytics_cv.html', context=context)

def cv_mech(request):
    context = {'job1': 'Mechanical Estimator', 'job2': 'BIM'}
    return render(request, 'mech_cv.html', context=context)