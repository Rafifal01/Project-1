# Tokopedia Review Sentiment Analysis

Buying the same kind of product from an official brand store or from a reseller
is a choice Indonesian shoppers make constantly, usually on price alone. This
project asks whether that choice actually shows up in customer satisfaction, by
scraping and analysing the reviews of two Tokopedia clothing stores: Faith
Industries, an official brand store, and Jul Clothing, a non-official one.

Coursework project from 2024, built with [@aldidaim21](https://github.com/aldidaim21).
It is archived — kept for reference rather than maintained.

## What's in it

`scraping_tokopedia.py` walks a store's review pages with Selenium and pulls the
product name, reviewer, timestamp, review text and star rating into a CSV. That
produced 385 reviews for Faith and 415 for Jul, both included here as
`Data Mentah *.csv`.

The two `Unprocessed Data - Labelling` notebooks handle the Indonesian side of
the cleaning. Star ratings get stripped of the word "bintang", text is
lowercased, emoji are removed, then a hand-written slang dictionary expands the
usual shortenings (`yg` → `yang`, `bgt` → `banget`, `cs` → `customer service`)
before Sastrawi does stopword removal and stemming. The result is machine
translated to English, and TextBlob assigns each review a polarity score that
becomes its Positive/Neutral/Negative label.

The two `visualization` notebooks take it from there: sentiment distribution,
polarity and word-count histograms, most frequent positive and negative terms,
and word clouds per sentiment class.

## What came out of it

The interesting part isn't the sentiment split, it's what the negative reviews
are actually about. Searching the negative set for `small`, `thin` and `wrong`
surfaces the recurring complaints, and they cluster on two things: garments
running smaller than expected, and fabric being thinner than the product photos
suggested. Neither is about delivery or seller responsiveness, which is where
you might expect an official-versus-reseller gap to show up.

## Running it

```bash
pip install -r requirements.txt
```

The notebooks were written in Google Colab and still carry
`/content/drive/MyDrive/...` paths, so they will not run as-is — point them at
local files first. The intermediate CSVs they pass between each other
(`translateFaith.csv`, `translateJul.csv`, `faithfinal.csv`) are not in the repo,
so only the raw scrape is reproducible from here. The scraper itself targets
Tokopedia's obfuscated CSS class names as they were in early 2024; those have
long since changed, so treat it as a record of the approach rather than a working
tool.

## Known limitations

Worth being upfront about, since a few of these would be done differently now.

Sentiment labels come from running TextBlob over machine-translated Indonesian.
TextBlob's polarity lexicon is built for English, and translation of review slang
is lossy, so the labels are noisier than the neat pie charts suggest. The star
rating was sitting right there in the scraped data as a much stronger ground
truth — there is even a `Labelling()` function in the notebooks that maps
rating > 3 to Positive, written and then never called.

The notebooks import SVC, RandomForest, LogisticRegression, GridSearchCV, SMOTE
and TF-IDF. None of them are used. No model is trained anywhere in this project;
it is exploratory analysis, and the imports are leftovers from a plan that didn't
happen.

The polarity breakdown quoted in the notebook markdown (40% / 30% / 30%) is
identical in both notebooks, so it is boilerplate rather than a measured result
for either store.

Sample sizes are small — 385 and 415 reviews from one store each — and both
stores sell clothing, so nothing here generalises to official versus non-official
sellers as a category.

Review text and reviewer display names are reproduced as scraped from public
Tokopedia listings.
