from urllib2 import urlopen
from json import loads

def get_new_submissions(subreddit, limit=25):
	"""
	Get new submissions from a subreddit page. The limit keyword defines the 
	number of submissions to get in 1 request (min = 25, max = 100) 
	"""
	url = "http://www.reddit.com/r/{0}/new.json?limit={1}".format(subreddit,limit)
	txt_data = urlopen(url).read()
	
	# the data that we get is text type thus it needs to be converted into json using loads
	json_data = loads(txt_data)
	
	# we get a dictionary containing 'kind' and 'data' keys in json_data.
	# we need to get the list of posts from the 'data'. 
	posts = json_data['data']['children']
	return posts


def clean(posts, params = []):
	"""
	Clean the data and extract the list of keys defined in the *args
	You can set the param_list as 
	['domain', 'media_cached','selftext']
	Other params that you can set are:
	
	['domain', 'banned_by', 'media_embed', 'subreddit', 'selftext_html', 'selftext', 'likes', 'secure_media', 'link_flair_text', 'id',\ 'gilded', 'secure_media_embed', 'clicked', 'stickied', 'author', 'media', 'score', 'approved_by', 'over_18','hidden', 'thumbnail',\ 'subreddit_id', 'edited', 'link_flair_css_class', 'author_flair_css_class', 'downs', 'saved', 'is_self', 'permalink', 'name', 'created',\ 'url', 'author_flair_text', 'title', 'created_utc','distinguished','num_comments', 'visited', 'num_reports', 'ups'] 
	"""	
	temp_posts = []

	for post_info in posts:
		post_data = post_info['data']
		post = [post_data[param]for param in params]
		temp_posts.append(post)
	
	return temp_posts

	
def write_to_file(posts_data, subreddit):
	"""
	Write the cleaned data to a file.
	"""	
	filename = str(subreddit)
	f = open(filename, 'w+')
	for data in posts_data:
		txt = ','.join(data)
		f.write(txt)
		f.write('\n')
 	f.close()


def main():
	#set initial variables
	subreddit = 'machinelearning'
	limit = 100

	# get posts
	posts = get_new_submissions(subreddit, limit)

	# set the params needed from the reddit post data
	params = ['name','title']
	data = clean(posts, params)

	#write the data to file
	write_to_file(data, subreddit)



if __name__ == '__main__':
	main()
