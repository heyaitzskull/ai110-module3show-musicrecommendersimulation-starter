import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences."""
    def normalize_distance(value: float, target: float, max_diff: float) -> float:
        if max_diff <= 0:
            return 0.0
        return max(0.0, 1.0 - abs(value - target) / max_diff)

    preferred_genre = (user_prefs.get("genre") or user_prefs.get("favorite_genre") or "").strip().lower()
    preferred_mood = (user_prefs.get("mood") or user_prefs.get("favorite_mood") or "").strip().lower()
    tempo_target = user_prefs.get("tempo_bpm") or user_prefs.get("preferred_tempo")
    acoustic_target = user_prefs.get("preferred_acousticness")
    valence_target = user_prefs.get("preferred_valence")
    energy_target = user_prefs.get("energy") or user_prefs.get("target_energy")
    intensity_target = user_prefs.get("preferred_intensity")
    likes_acoustic = user_prefs.get("likes_acoustic")

    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    song_tempo = float(song.get("tempo_bpm", 0.0))
    song_acousticness = float(song.get("acousticness", 0.0))
    song_valence = float(song.get("valence", 0.5))
    song_energy = float(song.get("energy", 0.5))
    song_intensity = float(song.get("energy", 0.5))

    genre_families = {
        "pop": {"indie pop", "electropop", "synthwave", "synthpop", "dance pop", "pop rock"},
        "lofi": {"ambient", "chillhop", "study beats"},
        "rock": {"punk", "metal", "grunge", "hard rock"},
        "electronic": {"synthwave", "disco", "house", "dance"},
        "hip hop": {"rap", "trap"},
        "jazz": {"blues", "soul", "r&b"},
        "country": {"folk", "americana"},
        "classical": {"opera", "soundtrack", "new age"},
    }

    mood_groups = [
        {"happy", "optimistic", "playful", "carefree", "vivacious", "hopeful"},
        {"chill", "relaxed", "serene", "calm", "dreamy", "focused"},
        {"intense", "aggressive", "energetic", "rebellious", "exuberant"},
        {"moody", "melancholic", "mysterious", "nostalgic", "romantic", "soulful", "trusting", "cinematic", "transcendent", "liberated"},
    ]

    reasons: List[str] = []

    if preferred_genre and song_genre:
        if song_genre == preferred_genre:
            genre_score = 1.0
            reasons.append("genre exact match (+0.28)")
        else:
            related = False
            if song_genre in genre_families.get(preferred_genre, set()):
                related = True
            elif preferred_genre in genre_families.get(song_genre, set()):
                related = True
            if related:
                genre_score = 0.6
                reasons.append("genre related match (+0.17)")
            else:
                genre_score = 0.0
                reasons.append("genre mismatch (+0.00)")
    else:
        genre_score = 0.5
        reasons.append("genre preference unavailable (+0.14)")

    if preferred_mood and song_mood:
        if song_mood == preferred_mood:
            mood_score = 1.0
            reasons.append("mood exact match (+0.24)")
        else:
            mood_score = 0.0
            for group in mood_groups:
                if preferred_mood in group and song_mood in group:
                    mood_score = 0.5
                    reasons.append("mood similar (+0.12)")
                    break
            if mood_score == 0.0:
                reasons.append("mood mismatch (+0.00)")
    else:
        mood_score = 0.5
        reasons.append("mood preference unavailable (+0.12)")

    if tempo_target is not None:
        tempo_score = normalize_distance(song_tempo, float(tempo_target), 80.0)
        reasons.append(f"tempo similarity ({tempo_score:.2f} * 0.14)")
    else:
        tempo_score = 0.5
        reasons.append("tempo preference unavailable (+0.07)")

    if acoustic_target is not None:
        acoustic_score = normalize_distance(song_acousticness, float(acoustic_target), 1.0)
        reasons.append(f"acousticness similarity ({acoustic_score:.2f} * 0.12)")
    elif likes_acoustic is not None:
        acoustic_target = 1.0 if likes_acoustic else 0.0
        acoustic_score = normalize_distance(song_acousticness, acoustic_target, 1.0)
        reasons.append(f"acousticness preference ({acoustic_score:.2f} * 0.12)")
    else:
        acoustic_score = 0.5
        reasons.append("acousticness preference unavailable (+0.06)")

    if valence_target is not None:
        valence_score = normalize_distance(song_valence, float(valence_target), 1.0)
        reasons.append(f"valence similarity ({valence_score:.2f} * 0.12)")
    else:
        valence_score = 0.5
        reasons.append("valence preference unavailable (+0.06)")

    if energy_target is not None:
        energy_score = normalize_distance(song_energy, float(energy_target), 1.0)
        reasons.append(f"energy similarity ({energy_score:.2f} * 0.06)")
    else:
        energy_score = 0.5
        reasons.append("energy preference unavailable (+0.03)")

    if intensity_target is not None:
        intensity_score = normalize_distance(song_intensity, float(intensity_target), 1.0)
        reasons.append(f"intensity similarity ({intensity_score:.2f} * 0.04)")
    elif energy_target is not None:
        intensity_score = normalize_distance(song_intensity, float(energy_target), 1.0)
        reasons.append("intensity proxy from energy (+0.04)")
    else:
        intensity_score = 0.5
        reasons.append("intensity preference unavailable (+0.02)")

    score = (
        0.28 * genre_score
        + 0.24 * mood_score
        + 0.14 * tempo_score
        + 0.12 * acoustic_score
        + 0.12 * valence_score
        + 0.06 * energy_score
        + 0.04 * intensity_score
    )

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommend top k songs based on user preferences."""
    # Compute scores for all songs
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    # Sort by score descending and take top k
    top_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
    
    return top_songs
