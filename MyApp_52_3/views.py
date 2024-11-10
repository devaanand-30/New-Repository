from django.shortcuts import render

def home(request):
    context = {
    
        'name': 'Devaanand Kumar Profile',
        'email': 'devaanandkumar5114@gmail.com',
        'education': ['KL University', 'MPC', 'SSC'],
        'skills': ['Python', 'Django', 'C', 'Data_Analysis', 'Java'],
        'Fresher': 'Looking for entry-level opportunities to start my career in tech.',
        'hobbies': ['Reading', 'Coding', 'Chess'],
        'github_url': 'https://github.com/yourusername',
    }
    return render(request, 'home.html', context)  # Use 'home.html' if not in a subfolder

