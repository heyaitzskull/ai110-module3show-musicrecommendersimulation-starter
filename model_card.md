# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

TuneMatcher 1.0  

---

## 2. Goal / Task  

This recommender suggests songs that match what you like in music. It looks at your favorite genre, mood, and energy level to find good matches.  

---

## 3. Data Used  

The dataset has 30 songs. Each song has details like genre, mood, energy, tempo, and more. It covers pop, lofi, rock, and some others. But it might not have all music types out there.

---

## 4. Algorithm Summary  

It scores songs by how well they match your preferences. Genre and mood are the biggest factors. Then it checks tempo, how acoustic it is, and energy level. Songs that match closer get higher scores.  

---

## 5. Observed Behavior / Biases  

The system sometimes picks songs that match genre well but not energy. For example, it might suggest a high-energy rock song to someone who wants chill pop. This could miss people who care a lot about energy.  

---

## 6. Evaluation Process  

I tested it with different user types like high-energy pop fans and chill lofi lovers. I looked at the top 5 songs for each and checked if they matched the genre and energy. Some surprises, like how one intense song kept showing up for happy preferences.  

---

## 7. Intended Use and Non-Intended Use  

This is for fun music discovery in a classroom or personal project. It's not for real music apps or professional recommendations.

---

## 8. Ideas for Improvement  

Add more songs to the list. Make energy matching stronger. Let users give feedback to improve algorithm recipe. 

## 9. Personal Reflection  

I was surprised how tweaking the weights could totally flip the recommendations, like making energy way more important than genre. Building this made me think about just how much more complicated the algorithms for real music apps are as well as the biases that come with it. I will definetly keep this project in mind the next time I get irritated when spotify recommends me a song that does not fit my taste at all. Even with all the smarts, human judgment still rules for catching those weird mismatches or understanding why a song just clicks for someone.

  
