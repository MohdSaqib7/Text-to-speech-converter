from gtts import gTTS
text = "Welcome to converter text to voice Now start Reading News Tech giant Google has spent $1 billion (roughly Rs. 7,410 crore) to buy a central London building where it is currently a tenant, showing its confidence in the future of the office as a place to work, the company said on Friday."
language = 'en'
obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")
print("finish")