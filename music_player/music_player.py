import pygame

class MusicPlayer:
    def __init__(self):
        self.current_track: str = ""
        self.is_playing: bool = False
        self.is_paused: bool = False
        pygame.mixer.init()

    def load_track(self, track_path: str):
        """Loads and initializes the specified music track for playback."""
        self.current_track = track_path
        pygame.mixer.music.load(self.current_track)
        self.is_playing = False
        self.is_paused = False

    def play(self, loop: bool = False):
        """Plays the current track, optionally looping if loop is set to True."""
        if not self.current_track:
            print("No track loaded.")
            return

        loop_times = -1 if loop else 0
        pygame.mixer.music.play(loops=loop_times)
        self.is_playing = True
        self.is_paused = False

    def pause(self):
        """Pauses music if it is currently playing."""
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.is_playing = False

    def stop(self):
        """Stops music playback and resets the track."""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def resume(self):
        """Resumes music if it was paused."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.is_paused = False
```
