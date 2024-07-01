text = "X-DSPAM-Confidence:    0.8475"

index = text.find(".")
num = float(text[index-1:])
print(num)
