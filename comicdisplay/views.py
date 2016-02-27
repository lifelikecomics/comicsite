from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random

from .models import Comic

# Create your views here.
def comicview(request, comic_id):
	if comic_id == "":
		curr_comic = Comic.objects.latest('pub_date')
	else:
		#get the index of the comic we want, then get the next and previous comics
		curr_comic = get_object_or_404(Comic, pk=comic_id)

	comic_list = sorted(Comic.objects.all(), key=lambda Comic: Comic.pub_date)
	curr_comic_inx = comic_list.index(curr_comic)

	#get previous comic id
	prev_comic = ""
	if (curr_comic_inx != 0):
		prev_comic = comic_list[curr_comic_inx - 1]

	#get random comic id
	rand_comic = random.choice(comic_list)

	#get next comic id
	next_comic = ""
	if (curr_comic_inx + 1 < len(comic_list)):
		next_comic = comic_list[curr_comic_inx + 1]


	context = {'curr_comic': curr_comic, 'prev_comic': prev_comic, 'rand_comic':rand_comic, 'next_comic':next_comic}
	return render(request, 'comics/index.html', context)


	