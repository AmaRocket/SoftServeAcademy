from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
"https://www.coogfans.com/uploads/db5902/original/3X/8/1/81173237ffa580ef710b0862fdddaac163274db1.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/c/b/cb1825f34d101467512d688ee119803760a603b7.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/6/c/6c1f5cbc5fcb7d27b31fe5d36110fdeabe3f9954.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/1/c/1cf606876578c7b5cbe5ff1d38589baf59e6f6f9.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/9/9/992eba235badb0b14f55faa905d9a4d53f4fea15.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/6/d/6df1ed4b1760b00604ae956e500a5ee8d11ae443.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/3/a/3ab6b5117fe238f2f8ddcffa1f2c252b0cd18241.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/b/a/bad9914e4e88474d446104314bba29e74d695bf7.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/e/a/ea3dc3b0da5c7ef58c23968527530b40c07770eb.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/5/c/5cde185c590b3a097c2573da196e09face9e1ba6.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/e/d/ed824a2bf77e8a16fe276580960f1e63b0336082.jpeg",
"https://www.coogfans.com/uploads/db5902/original/3X/2/7/274ca28f67052400b38949d5690e65aa8d536ab0.jpeg"
]
@app.route('/')
def index():
	url = random.choice(images)
	return render_template('index.html', url=url)
if __name__ == "__main__":
	app.run(host="0.0.0.0")
