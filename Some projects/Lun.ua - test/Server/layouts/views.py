from django.shortcuts import render
from django.http import HttpResponseRedirect


from .models import image_result
from .models import proceed_result
from .forms import UploadFileForm
from .models import image_detail


from PIL import Image

import classifier


import urllib
import os


# Create your views here.
def result_for_page(request):
    count_images = 20
    page_number = int(request.path.split("/")[1])

    next_page = str(page_number + 1)
    prev_page = str(page_number - 1)

    results = []
    map = proceed_result.objects.in_bulk([x for x in range(page_number * count_images, page_number * count_images + count_images)])
    for key, obj in map.iteritems():
        results.append(image_result(obj.url, obj.proceed_default, obj.proceed_bfs))

    return render(request, 'result.html', {'results' : results, 'next_page' : next_page, 'prev_page' : prev_page})


def result_for_upload(request):
    results = []
    file_path = "media\\tmp.jpg"

    res = classifier.proceed_file(file_path)

    results.append(image_result("media/tmp.jpg", res['default'], res['bfs']))

    return render(request, 'result.html', {'results' : results, 'next_page' : -1, 'prev_page' : -1})



def upload_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print "FORM: ", form
        print request.POST, request.FILES
        print form.is_valid()
        if form.is_valid():
            new_img = Image.open(request.FILES['image_file'])
            new_img.save("media\\tmp.jpg")

            return HttpResponseRedirect('upload_result')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def detail(request):
    id = request.path.split("_")[-1]
    arr = classifier.proceed_detail(id)

    bfs_results = []
    straight_results = []
    for element in arr[0:1]:
        straight_results.append(image_detail(element[0], element[1]))

    for element in arr[1:]:
        bfs_results.append(image_detail(element[0], element[1]))

    return render(request, 'detail.html', {'straight_results': straight_results, 'bfs_results': bfs_results})



def result_by_keys(request, key_default, key_bfs):
    count_images = 20

    # page_number = int(request.path.split("/")[1].split("_")[1])
    page_path, page_numb = request.path.split("/")[1].split("_")
    page_number = int(page_numb)

    next_page = "%s_%d" % (page_path, (page_number + 1))
    prev_page = "%s_%d" % (page_path, (page_number - 1))

    results = []
    # objects_filter = list(proceed_result.objects.filter(proceed_default="apartment_layout", proceed_bfs="apartment_layout"))
    objects_filter = list(proceed_result.objects.filter(proceed_default=key_default, proceed_bfs=key_bfs))

    try:
        arr = [objects_filter[x] for x in range(page_number * count_images, page_number * count_images + count_images)]
        for obj in arr:
            results.append(image_result(obj.url, obj.proceed_default, obj.proceed_bfs))
    except:
        print "Invalid number of page..."

    return render(request, 'result.html', {'results' : results, 'next_page' : next_page, 'prev_page' : prev_page})


def result_both(request):
    return result_by_keys(request, "apartment_layout", "apartment_layout")


def result_bfs(request):
    return result_by_keys(request, "other", "apartment_layout")


def result_default(request):
    return result_by_keys(request, "apartment_layout", "other")
