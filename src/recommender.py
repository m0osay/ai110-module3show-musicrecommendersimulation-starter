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
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    int_fields   = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                key: int(val) if key in int_fields
                     else float(val) if key in float_fields
                     else val
                for key, val in row.items()
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns a tuple of (score, reasons) where score is 0.0-1.0
    and reasons is a list of strings explaining the score.
    """
    score = 0.0
    reasons = []

    # Mood match (weight: 0.35) — most important factor
    if song["mood"] == user_prefs.get("mood"):
        score += 0.35
        reasons.append(f"mood match: {song['mood']} (+0.35)")

    # Energy proximity (weight: 0.25) — continuous scoring
    target_energy = user_prefs.get("energy", 0.5)
    energy_score = 1 - abs(song["energy"] - target_energy)
    score += 0.25 * energy_score
    reasons.append(f"energy proximity: {song['energy']} vs target {target_energy} (+{0.25 * energy_score:.2f})")

    # Valence proximity (weight: 0.25) — continuous scoring
    target_valence = user_prefs.get("valence", 0.5)
    valence_score = 1 - abs(song["valence"] - target_valence)
    score += 0.25 * valence_score
    reasons.append(f"valence proximity: {song['valence']} vs target {target_valence} (+{0.25 * valence_score:.2f})")

    # Acousticness (weight: 0.15) — rewards based on user preference
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    acoustic_score = song["acousticness"] if likes_acoustic else 1 - song["acousticness"]
    score += 0.15 * acoustic_score
    reasons.append(f"acousticness: {song['acousticness']} (+{0.15 * acoustic_score:.2f})")

    return round(score, 4), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, " | ".join(reasons)))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
