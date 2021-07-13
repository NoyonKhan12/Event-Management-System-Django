from django.shortcuts import render
from. models import Events

# Create your views here.
def index(request):
    

    event1 = Events()
    event1.name = "Setara Convention Hall, Dhaka"
    event1.desc = "Capacity - 200, Size - 2500 sqft, Floor - Second Floor"
    event1.img = "setara.png"
    event1.price = "10000 TK"

    event2 = Events()
    event2.name = "Celebration Hall, Dhaka"
    event2.desc = "Capacity - 300, Size - 3500 sqft, Floor - First Floor"
    event2.img = "celebration.png"
    event2.price = "20000 TK"

    event3 = Events()
    event3.name = "Khulna Convention Hall, Khulna"
    event3.desc = "Capacity - 150, Size - 2000 sqft, Floor - Third Floor"
    event3.img = "kcc.png"
    event3.price = "15000 TK"

    events = [ event1, event2, event3]

    return render(request,"index.html",{'events': events})