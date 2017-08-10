import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
                str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # Get the title,comments, if one is available. By checking for this will fix informational
    # errors.
    title = response_dict['title']
    if not title:
        title = "No title provided."

    comments = response_dict.get('descendants', 0)
    if not comments:
        comments = "No commments provided."

    submission_dict = {
        'title': title,
                'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
                'comments': comments
        }
    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])

