from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from opportunities.models import Opportunity, Account

# Create your views here.


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def opp_list(request):
    opps = Opportunity.objects.all()
    return render(request, "opp_list.html", {"opps": opps})


@login_required
def acc_list(request):
    accs = Account.objects.all()
    return render(request, "acc_list.html", {"accs": accs})
