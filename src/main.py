"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys
from pathlib import Path

# Add the current directory to sys.path to allow imports
sys.path.insert(0, str(Path(__file__).parent))

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Define user preference profiles
    profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9}
        },
        {
            "name": "Chill Lofi",
            "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.2}
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.8}
        },
        # Adversarial/Edge case profiles
        {
            "name": "Conflicting High Energy Sad",
            "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9}  # High energy but sad mood - conflicting preferences
        },
        {
            "name": "Extreme Classical Neutral",
            "prefs": {"genre": "classical", "mood": "neutral", "energy": 1.0}  # Extreme energy with neutral mood
        },
        {
            "name": "Low Energy Intense",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.1}  # Low energy but intense mood - potential edge case
        }
    ]

    for profile in profiles:
        print(f"\n--- Profile: {profile['name']} ---")
        user_prefs = profile['prefs']
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            for reason in explanation.split("; "):
                print(f"  - {reason}")
            print()


if __name__ == "__main__":
    main()
