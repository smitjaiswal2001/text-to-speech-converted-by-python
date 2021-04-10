from gtts import gTTS
import os
myText = "હેલો મારું નામ સ્મીત જયસ્વાલ છે"
output = gTTS(text=myText, lang='gu', slow=True, )
output.save("output.mp3")
os.system("start output.mp3")