from googleapiclient.discovery import build
import pprint


def search_for_tag(tag):
    my_api_key = 'AIzaSyBUQQ4MeC8N6wDwxmHS8-FEqVGWUtfl754'
    my_cse_id = "018007238419152413196:g_1r4bqw2i0"

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']

    results = google_search(
        'programming what is {0} site:en.wikipedia.org'.format(tag), my_api_key, my_cse_id, num=1)
    return results[0]
