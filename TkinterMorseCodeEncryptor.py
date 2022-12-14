def button_clicked():
    message = entry.get()
    message = message.upper()
    if ValidMessage(message) == True:
        cipher = Encryption(message)
        messageent.delete("1.0", tk.END)
        messageent.insert("1.0", cipher)
    else:
        messageent.delete("1.0", tk.END)
        messageent.insert("1.0", "Invalid character")
    
def reset():
    messageent.delete("1.0",tk.END)
    entry.delete(0,tk.END)
    
def Encryption(message):
    Cipher = []
    for i in message:
        if i != " ":
            Cipher.append(MorseCode[i])
        elif i == " ":
            Cipher.append(" ")
    Cipher = " ".join(Cipher)
    return Cipher

def ValidMessage(message):
    try:
        for i in message:
            MorseCode[i]
    except KeyError:
        return False
    else:
        return True

def main():
    global MorseCode, messageent, entry
    MorseCode = { "A":".-", "B":"-...",
              "C":"-.-.", "D":"-..", "E":".",
              "F":"..-.", "G":"--.", "H":"....",
              "I":"..", "J":".---", "K":"-.-",
              "L":".-..", "M":"--", "N":"-.",
              "O":"---", "P":".--.", "Q":"--.-",
              "R":".-.", "S":"...", "T":"-",
              "U":"..-", "V":"...-", "W":".--",
              "X":"-..-", "Y":"-.--", "Z":"--..",
              "1":".----", "2":"..---", "3":"...--",
              "4":"....-", "5":".....", "6":"-....",
              "7":"--...", "8":"---..", "9":"----.",
              "0":"-----", ",":"--..--", ".":".-.-.-",
              "?":"..--..", "/":"-..-.", "-":"-....-",
              "(":"-.--.", ")":"-.--.-", " ":" "}
    window = tk.Tk()
    window.geometry("450x300")
    window.config(bg="#45f7e0")
    frame = tk.Label(bg="#45f7e0")
    frame2 = tk.Label(bg="#45f7e0")
    frame3 = tk.Label(bg="#45f7e0")
    label = tk.Label(text = "Please enter your message to encrypt:", bg = "#40edd8")
    entry = tk.Entry()
    button = tk.Button(text = "Done.", command = button_clicked, bg = "#40edd8")
    button2 = tk.Button(text = "Reset.", command = reset, bg = "#40edd8")
    messageent = tk.Text(width = 40, height = 6)
    label.pack()
    entry.pack()
    frame.pack()
    button.pack()
    frame2.pack()
    button2.pack()
    frame3.pack()
    messageent.pack()

import tkinter as tk
main()
