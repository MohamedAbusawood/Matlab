from flask import Flask, render_template, request
import yake

app = Flask(__name__)

custom_kw_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, dedupFunc='seqm', windowsSize=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('Services.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/extractpg')
def extractpg():
    return render_template('extract.html')

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text.strip():
            try:
                keywords = custom_kw_extractor.extract_keywords(text)
                # Now including scores in the selection
                selected_keywords = [{'keyword': kw[0], 'score': round(kw[1], 2)} for kw in keywords]
                highlighted_text = highlight_keywords(text, [kw['keyword'] for kw in selected_keywords])
                top_20_keywords = selected_keywords[:20]  # This now includes scores
                return render_template('highlight.html', text=highlighted_text, keywords=top_20_keywords)
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render_template('highlight.html', error=error_message)
        else:
            error_message = "Please enter some text."
            return render_template('extract.html', error=error_message)
    return render_template('extract.html')



def highlight_keywords(text, keywords):
    highlight_color = '<span style="color:red">'  
    reset_color = '</span>'  
    for keyword in keywords:
        highlighted_keyword = f"{highlight_color}{keyword}{reset_color}"
        text = text.replace(keyword, highlighted_keyword)
    return text

if __name__ == '__main__':
    app.run(debug=True)
