# 🎵 Music Recommender Simulation

![alt text](image.png)
![alt text](image-1.png)

# proposed user profile:
favorite_genre
favorite_mood
preffered_tempo
preferred_acousticness
preferred_valence
target_energy = audio energy level
preferred_intensity = subjective “edge” or aggression of the track

Example point scheme
genre_score: 0–1
mood_score: 0–1
tempo_score: 0–1
acousticness_score: 0–1
valence_score: 0–1
energy_score: 0–1
intensity_score: 0–1

score =

0.28 * genre_score
+ 0.24 * mood_score
+ 0.14 * tempo_score
+ 0.12 * acousticness_score
+ 0.12 * valence_score
+ 0.06 * energy_score
+ 0.04 * intensity_score

How to compute similarity
Genre: exact match = 1.0, related genre family = 0.6, otherwise 0.0
Mood: exact or very close emotion = 1.0, similar mood = 0.5
Tempo/attributes: use distance from preferred value, normalized to 0..1
e.g. tempo_score = 1 - (abs(song_tempo - preferred_tempo) / max_tempo_diff)

biases:

Genre bias
Heavily weighting favorite_genre favors familiar labels and can repeatedly recommend the same genre.
It may underserve niche or cross-genre tracks that match mood/energy but not genre.

Personalization vs. novelty bias
Strong genre/mood weights can reduce exposure to new or surprising tracks.
The algorithm may overfit to an assumed profile and fail to recommend useful variety.

Cold-start bias
New songs with incomplete metadata or missing feature values get penalized even if they would be good matches.
New users with sparse preferences may get poor recommendations if the algorithm depends too much on exact matches.

Mood label bias
Mood is often subjective and inconsistently tagged.
If mood categories are coarse or culturally biased, recommendations may reflect those labeling assumptions rather than actual user feeling.

Audio feature matching bias
Features like tempo, acousticness, valence, energy, and intensity assume the user wants exact audio similarity.
This can overly favor tracks that sound “the same” and reduce diversity.

## Project Summary


In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

