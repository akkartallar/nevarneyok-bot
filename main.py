import random, subprocess
from gtts import gTTS
from PIL import Image, ImageDraw

videolar = [
    ("Ayasofya'nın Altında Ne Var? | Ne Var Ne Yok", "Ayasofya'nın altında kilometrelerce tünel olduğu söyleniyor. Peki o tünellerin sonunda ne var? Ahit Sandığı gerçekten orada mı?"),
    ("3. Gözünü Açtırma Yoksa... | Ne Var Ne Yok", "Epifiz bezi, yani üçüncü göz hakkında anlatılanlar doğru mu? Gece rüyanızda gördükleriniz aslında tesadüf mü?"),
    ("Rüyanda Ölmüş Birini Görüyorsan... | Ne Var Ne Yok", "Rüyanda ölmüş birini görmek ne anlama geliyor? Bu bir mesaj mı yoksa bilinçaltının oyunu mu?"),
]

baslik, hikaye = random.choice(videolar)
tts = gTTS(text=hikaye, lang='tr')
tts.save("ses.mp3")
img = Image.new('RGB', (1280, 720), color=(0, 0, 0))
d = ImageDraw.Draw(img)
d.text((60, 200), "NE VAR NE YOK", fill=(255, 200, 0))
d.text((60, 300), baslik, fill=(255, 255, 255))
img.save("kapak.jpg")
subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", "kapak.jpg", "-i", "ses.mp3", "-shortest", "video.mp4"])
print("Hazir")
