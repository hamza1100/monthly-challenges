from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': 'Learn Django for at least 20 minutes every day!'
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse('Walk for at least 20 minutes every day!')

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('monthly-challenge', args=[redirect_month])
    except:
        return HttpResponseNotFound('This month number is not supported')
    return HttpResponseRedirect(redirect_path)

# second argument maching the dynamic path variable
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # f'<h1>{challenge_text}</h1>'
    except:
        return HttpResponseNotFound("<h1> This month is not supported </h1>")
    # return HttpResponse(response_data)

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('monthly-challenge', args=[month])
        list_items += f'<li><a href=\'{month_path}\'>{capitalized_month}</a></li>'
    
    month_listing = f"<ul>{list_items}</ul>"
    return HttpResponse(month_listing)