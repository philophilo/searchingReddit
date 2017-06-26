from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from indexerNew import Searcher
from lang_proc import query_terms
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
Bootstrap(app)
# TODO: configurable
searcher = Searcher("indexesNew")

#
#NOTE: Flask looks for templates in "templates" folder
#

class SearchForm(Form):
	user_query = StringField('user_query', validators=[DataRequired()])
	search_button = SubmitField("Search!")

@app.route("/", methods=["GET", "POST"]) #Decorator --  oi
def index():
	search_form = SearchForm(csrf_enabled=False)
	print search_form.user_query.data
	if search_form.validate_on_submit():
		return redirect(url_for("search_results", query=search_form.user_query.data))
	return render_template("index.html", form=search_form)

@app.route("/search_results/<query>")
def search_results(query):
    query_words = query_terms(query)
    app.logger.info("Requested [{}]".format(" ".join(query_words)))
    print ">>>>>", query_words
    docids = searcher.find_documents_AND(query_words)
    urls = [searcher.get_url(docid) for docid in docids]
    texts = [searcher.generate_snippet(query_words, docid) for docid in docids]

    return render_template("search_results.html", query=query, urls_and_texts=zip(urls,texts))

if __name__ == '__main__':
	app.run(debug = True)
