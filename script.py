import requests
import urllib.request
import config

subject = input('Get images of ? ')
number = int(input('How many images do you want ? '))
format = '.jpg'
image_quality = 'regular' # raw, full, regular, small
url_photos = 'https://api.unsplash.com/search/photos/?page='


def download_images(images_arr, count, downloaded):
    for i in range(len(images_arr)):
        if downloaded <= number:
            with open('./downloads/'+ subject + str(downloaded) + format,'wb') as file:
                file.write(requests.get(images_arr[i]).content)
            print('Downloaded: ',downloaded,' of ',number)
            downloaded += 1
        else:
            return

def number_of_images(num):
    count = 0
    downloaded = 1

    if num % 10 == 0:
        num = num // 10
    else:
        num = (num // 10) + 1

    for i in range(num):
        url =  url_photos + str(i) + '&query=' + subject + '&client_id=' + config.ACCESS_KEY
        content = requests.get(url).json()
        images = [content['results'][index]['urls'][image_quality] for index in range(len(content['results']))]

        download_images(images, count, downloaded)

        downloaded += 10
        count += 1

number_of_images(number)
print('~Download complete!~')
