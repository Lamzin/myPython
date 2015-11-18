import time
from layouts.models import proceed_result


def data_fill_all():
    data = open("layouts//fill_database//data.txt", "r")
    storage_url = "http://storage.googleapis.com/lun_ua/"

    objects = []
    for line in data:
        try:
            arr = line.split()
            result_new = proceed_result()
            result_new.name = arr[0]
            result_new.url = storage_url + arr[0]
            result_new.proceed_default = arr[1]
            result_new.proceed_bfs = arr[2]
            objects.append(result_new)
        except:
            print "something going wrong... %s" % line

    time_begin = time.clock()

    try:
        print "Inserting..."
        proceed_result.objects.bulk_create(objects)
    except:
        print "Error!"

    print "Total time = %f" % (time.clock() - time_begin)