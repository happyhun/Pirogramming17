from multiprocessing import context
from platform import release
from django.shortcuts import render
from .models import Review
from django.shortcuts import redirect

# Create your views here.
def review(request):
    reviews = Review.objects.all()
    context={
        "reviews": reviews,
    }
    return render(request, template_name="reviews/review.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        rating = request.POST["rating"]
        time = request.POST["time"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        Review.objects.create(title = title, release = release, genre = genre, rating = rating,
        time = time, review = review, director = director, actor = actor)

        return redirect("/")
    review = Review
    context={
        'review': review
    }
    return render(request, template_name="reviews/create.html", context=context)

def detail(request, id):
    review = Review.objects.get(id=id)
    time = review.time
    hour = time // 60
    minute = time % 60
    if hour == 0:
        time = str(minute)+"분"
    else:
        time = str(hour)+"시간"+" "+str(minute)+"분"
    
    context = {
        "review":review,
        "time":time,
    }
    return render(request, template_name="reviews/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        rating = request.POST["rating"]
        time = request.POST["time"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        Review.objects.filter(id=id).update(title = title, release = release, genre = genre, rating = rating,
        time = time, review = review, director = director, actor = actor)
        return redirect(f"/review/{id}")

    review = Review.objects.get(id=id)
    genres = Review.GENRE_CHOICES
    context = {
        "review":review,
        "genres":genres,
    }
    return render(request, template_name="reviews/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Review.objects.filter(id=id).delete()
        return redirect("/")