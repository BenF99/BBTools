from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "week1": {
            "set1": "ORM",
            "set2": "ORM",
            "set3": "ORM",
        },
        "week2": {
            "set1": "ORM",
            "set2": "ORM",
            "set3": "ORM",
        },
        "week3": {
            "set1": "ORM",
            "set2": "ORM",
            "set3": "ORM",
        },
        "week4": {
            "set1": "ORM",
            "set2": "ORM",
            "set3": "ORM",
        }
    }
    if (request.GET.get('mybtn')):
        onerm = float(request.GET.get('submit_form'))
        context["week1"]["set1"] = "{:.2f}".format(onerm * 0.65)
        context["week1"]["set2"] = "{:.2f}".format(onerm * 0.75)
        context["week1"]["set3"] = "{:.2f}".format(onerm * 0.85)
        context["week2"]["set1"] = "{:.2f}".format(onerm * 0.70)
        context["week2"]["set2"] = "{:.2f}".format(onerm * 0.80)
        context["week2"]["set3"] = "{:.2f}".format(onerm * 0.90)
        context["week3"]["set1"] = "{:.2f}".format(onerm * 0.75)
        context["week3"]["set2"] = "{:.2f}".format(onerm * 0.85)
        context["week3"]["set3"] = "{:.2f}".format(onerm * 0.95)
        context["week4"]["set1"] = "{:.2f}".format(onerm * 0.4)
        context["week4"]["set2"] = "{:.2f}".format(onerm * 0.5)
        context["week4"]["set3"] = "{:.2f}".format(onerm * 0.6)

    return render(request, '531/main.html', context)
