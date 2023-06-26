from tkinter import *


morse_code_dict = {
    'A':'.-',
    'B':'-...',
    'C':'- .-.',
    'D':'-. .',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    ' ':' ',
    '\n':'',
}

def traslate_to_morse(sentence):
    result = ''
    for letter in sentence:
        result+=' '+morse_code_dict[letter.upper()]

    l.config(text=result)


if __name__ == '__main__':
    main = Tk()


    text = Text(height=5, width=52)
    text.grid(row=1, column=1)
    b = Button(text='To Morse', command=lambda:traslate_to_morse(text.get("1.0",END)))
    b.grid(row=2,column=1)
    l = Label(text='')
    l.grid(row=3,column=1)
    main.mainloop()



