
# Recipe Chatbot

This chatbot suggests recipes based on the ingredients you provide using **TheMealDB API**.

## How to Run

### Requirements
- Python 3.x
- Install dependencies:

```bash
pip install gradio requests
```

### Run Locally

1. Clone the repository or download the files.
2. Install the dependencies:

```bash
pip install gradio requests
```

3. Run the app:

```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:7860`.

### How to Use

1. Enter ingredients (in English, separated by commas).
2. Get a recipe suggestion with instructions and a link to the full recipe.

### Example Input:

`chicken, rice, tomato`

### Example Output:

```
🍽 Recipe suggested: Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber

👨‍🍳 Instructions: Add'l ingredients: mayonnaise, sriracha...

1. Place rice in a fine-mesh sieve and rinse until water runs clear. Add to a small pot with 1 cup water (2 cups for 4 servings) and a pinch of salt. Bring to a boil, then cover and reduce heat to low. Cook until rice is tender, 15 minutes. Keep covered off heat for at least 10 minutes or until ready to serve.

2. Meanwhile, wash and dry all produce. Peel and finely chop garlic. Zest and quarter lime (for 4 servings, zest 1 lime and quarter both). ...

🔗 [View full recipe](link)
```

