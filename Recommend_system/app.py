from flask import Flask, render_template, request
import pickle
import numpy as np
import difflib

app = Flask(__name__)

# Load data and similarity matrix
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_score.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=[round(x, 2) for x in popular_df['avg_rating'].values])


@app.route('/recommend', methods=['GET', 'POST'])
def recommend_ui():
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # Fuzzy matching using difflib
        matches = difflib.get_close_matches(user_input, pt.index, n=1, cutoff=0.5)

        if not matches:
            return render_template('recommend.html', data=[], not_found=True)

        matched_book = matches[0]
        index = np.where(pt.index == matched_book)[0][0]

        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item = {
                'title': temp_df['Book-Title'].values[0],
                'author': temp_df['Book-Author'].values[0],
                'image': temp_df['Image-URL-M'].values[0]
            }
            data.append(item)

        return render_template('recommend.html', data=data, not_found=False)

    return render_template('recommend.html', data=[], not_found=False)


if __name__ == '__main__':
    app.run(debug=True)
