"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"mood": "chill", "energy": 0.38, "valence": 0.62, "likes_acoustic": True}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  🎵 Top 5 Recommendations")
    print("=" * 50)
    print(f"  Profile: mood={user_prefs['mood']}, energy={user_prefs['energy']}, "
          f"valence={user_prefs['valence']}, likes_acoustic={user_prefs['likes_acoustic']}")
    print("=" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Score: {score:.3f}")
        print("    Reasons:")
        for reason in explanation.split(" | "):
            print(f"      - {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
