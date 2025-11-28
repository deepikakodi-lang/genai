from django.shortcuts import render


def home(request):
    apps = [
        {"name": "Supplier Contract Review", "url": "/supplier/", "icon": "fa-file-contract"},
        {"name": "Logistic App", "url": "/logistic/", "icon": "fa-truck"},
        {"name": "Underwriter App", "url": "/underwriter/", "icon": "fa-shield-halved"},
        {"name": "Medical Claims", "url": "/medical_claims/", "icon": "fa-shield-halved"},
    ]
    return render(request, "dashboard/home.html", {"apps": apps})
