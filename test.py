from virecognize.client import ViRecognitionAPI


def run():
    access_key = ''
    secret_key = ''
    api = ViRecognitionAPI(access_key, secret_key)

    image_url = 'http://sg-live-02.slatic.net/p/cchappiness-v-neck-short-sleeve-t-shirt-army-green-export-6879-861477-1-zoom.jpg'
    tag_group = 'fashion_attributes'

    response = api.image_recognize(image_url, tag_group)

    print response


if __name__ == '__main__':
    run()
