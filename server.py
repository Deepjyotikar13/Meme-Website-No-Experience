
from flask import Flask,render_template
import json,requests
app=Flask(__name__)
@app.route("/")
def meme_page():
	api_url="https://meme-api.com/gimme"#this is api to get memes from reddit
	data=json.loads(requests.get(api_url).text)#api response as a json data 
	#selecting all the necessarythings i need to display on the website
	meme_image=image=data["preview"][-1]# this is the meme image
	subreddit_name=data["subreddit"]#subreddit name 
	meme_title=data["title"]#this is the title
	up_votes=data["ups"]#totalup votes
	post_link=data["postLink"] #post link and if you click on the subreddit name you can visit the actuall post on reddit
	
	meme_data_list=[meme_image,subreddit_name,meme_title,up_votes,post_link]# i converted everything into a list so i can acess it easily in the html code
	return render_template("meme_page.html",meme_data=meme_data_list)
if __name__=="__main__":
	app.run(debug=True,port=8000)