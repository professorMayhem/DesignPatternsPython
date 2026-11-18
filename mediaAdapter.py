
from abc import ABC, abstractmethod


# -----------------------------------------
# MediaPlayer interface
# -----------------------------------------

class MediaPlayer(ABC):

    @abstractmethod
    def play(self, audio_type, file_name):
        pass


# -----------------------------------------
# AdvancedMediaPlayer interface
# -----------------------------------------

class AdvancedMediaPlayer(ABC):

    @abstractmethod
    def play_vlc(self, file_name):
        pass

    @abstractmethod
    def play_mp4(self, file_name):
        pass


# -----------------------------------------
# Create advanced media players
# -----------------------------------------

class VlcPlayer(AdvancedMediaPlayer):

    def play_vlc(self, file_name):
        print(f"Playing vlc file. Name: {file_name}")

    def play_mp4(self, file_name):
        pass


class Mp4Player(AdvancedMediaPlayer):

    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        print(f"Playing mp4 file. Name: {file_name}")


# -----------------------------------------
# Create the MediaAdapter
# -----------------------------------------

class MediaAdapter(MediaPlayer):

    def __init__(self, audio_type):

        if audio_type.lower() == "vlc":
            self.advanced_player = VlcPlayer()

        elif audio_type.lower() == "mp4":
            self.advanced_player = Mp4Player()

        else:
            raise ValueError(
                f"Unsupported format: {audio_type}"
            )

    def play(self, audio_type, file_name):

        if audio_type.lower() == "vlc":
            self.advanced_player.play_vlc(file_name)

        elif audio_type.lower() == "mp4":
            self.advanced_player.play_mp4(file_name)


# -----------------------------------------
# Create the AudioPlayer
# -----------------------------------------

class AudioPlayer(MediaPlayer):

    def play(self, audio_type, file_name):

        audio_type = audio_type.lower()

        # AudioPlayer natively supports MP3
        if audio_type == "mp3":
            print(f"Playing mp3 file. Name: {file_name}")

        # Use the adapter for other supported formats
        elif audio_type in ("vlc", "mp4"):
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)

        else:
            print(
                f"Invalid media. {audio_type} format not supported"
            )


# -----------------------------------------
# Demonstrate the Adapter Pattern
# -----------------------------------------

def main():

    audio_player = AudioPlayer()

    audio_player.play("mp3", "beyond the horizon.mp3")

    audio_player.play("mp4", "alone.mp4")

    audio_player.play("vlc", "far far away.vlc")

    audio_player.play("avi", "mind me.avi")


if __name__ == "__main__":
    main()
