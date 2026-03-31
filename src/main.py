"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "Chill Lofi": {
        "mood": "chill", "energy": 0.38, "valence": 0.62, "likes_acoustic": True
    },
    "High-Energy Pop": {
        "mood": "intense", "energy": 0.92, "valence": 0.80, "likes_acoustic": False
    },
    "Deep Intense Rock": {
        "mood": "intense", "energy": 0.88, "valence": 0.42, "likes_acoustic": False
    },
    # Edge cases
    "Conflicting (high energy + chill mood)": {
        "mood": "chill", "energy": 0.90, "valence": 0.50, "likes_acoustic": False
    },
    "Extreme Acoustic Ambient": {
        "mood": "moody", "energy": 0.10, "valence": 0.30, "likes_acoustic": True
    },
    "Perfectly Balanced (all mid)": {
        "mood": "focused", "energy": 0.50, "valence": 0.50, "likes_acoustic": False
    },
}


def print_recommendations(profile_name, user_prefs, recommendations):
    print("\n" + "=" * 55)
    print(f"  Profile: {profile_name}")
    print(f"  mood={user_prefs['mood']}, energy={user_prefs['energy']}, "
          f"valence={user_prefs['valence']}, likes_acoustic={user_prefs['likes_acoustic']}")
    print("=" * 55)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Score: {score:.3f}")
        print("    Reasons:")
        for reason in explanation.split(" | "):
            print(f"      - {reason}")
    print("\n" + "=" * 55)


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, user_prefs, recommendations)


if __name__ == "__main__":
    main()
