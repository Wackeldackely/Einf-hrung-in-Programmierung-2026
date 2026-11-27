# Aufgabe 08-05
#  TODO: Ihre Lösung hier


class Post:  # Basisklasse
    def __init__(self, autor, inhalt):
        self.autor = autor
        self.inhalt = inhalt

    def anzeigen(self):
        print(f"--- POST von @{self.autor} ---\n{self.inhalt}\n{'-' * 30}")


class BildPost(Post):  # 1.Kindklasse
    def __init__(self, autor, inhalt, bild_datei):
        super().__init__(autor, inhalt)
        self.bild_datei = bild_datei

    def anzeigen(self):
        print(
            f"--- BILD-POST von @{self.autor} ---\n{self.inhalt}\n[Bild: {self.bild_datei}]\n{'-' * 30}"
        )


class VideoPost(Post):  # 2. Kindklasse
    def __init__(self, autor, inhalt, video_datei, dauer):
        super().__init__(autor, inhalt)
        self.video_datei = video_datei
        self.dauer = dauer

    def anzeigen(self):
        print(
            f"--- VIDEO-POST von @{self.autor} ---\n{self.inhalt}\n[Video: {self.video_datei} ({self.dauer})\n{'-' * 30}"
        )


text_post = Post("user123", "Das ist ein einfacher Test-Post")
bild_post = BildPost("insta_star", "Urlaubsfoto! #sommer", "sonnenuntergang.jpg")
video_post = VideoPost(
    "youtuber", "Mein neues Tutorial ist online!", "anleitung.mp4", 65
)

text_post.anzeigen()
bild_post.anzeigen()
video_post.anzeigen()
