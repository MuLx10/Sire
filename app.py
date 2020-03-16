from flask import Flask, render_template
import random, os

# Create the app.
app = Flask(__name__)

# Add a route.
@app.route('/')
def home():
    sample_quotes = [
        "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
        "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
        "There are no shortcuts to any place worth going. – Beverly Sills",
        "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
        "You don’t drown by falling in the water; you drown by staying there. – Ed Cole"
    ]

    # Select a random quote.
    selected_quote = random.choice(sample_quotes)

    # Pass the selected quote to the template.
    return render_template('quotes.html', quote=selected_quote)



if __name__ == "__main__":
    app.run(os.getenv('LISTEN_HOST', '0.0.0.0'), int(os.environ.get("PORT", 5000)))


