Solution/Flag: flag{l00ks_l1ke_a_l0t_of_64s}


The challenge's title often provides some aid or direction to solve the problem. Here, the title repeats the number 64 three times, which can be a hint to decode a Base64 string three (or a couple of) times.

The problem also gives two files: generate.js and cipher.txt.
Generate.js is an ASCII text file, with the Javascript extension.
Cipher.txt is an ASCII text, with very long lines, with no line terminators file.

Let's take a look of the file and see what it does. Finding the purpose of the program will be the key to finding the decryption process.

![generate.js](https://github.com/Yukjed/redpwn_2020CTF/blob/master/crypto/base646464/jsBase64Encoding.png)

First, there's a constant, but that will initialize a buffer so the string that the program will read later on is treated as a base64 string (or number). This is a function that will take a string and encode it with as base64.

Moreover, we can see some file related instructions. In a nutshell, the program reads the string from the text file (flag.txt) into a constant.
The interesting part is within the loop. We can easily see that it will repeat some sort of instruction 25 times. From i=0 to i=25 (it does not execute the i=25 loop). Each instruction will call the function byte, it will take the string (which was initially read from the file) and encode it as a base64.

Finally the last instruction will write the string (base 64 number encodes 25 times) to the cipher.txt file that was given to us.
P.S.: Each string we can see uses the UTF-8 binary classification, which we know it will follow the ASCII byte representation.

So, at this point I knew all I had to do is to decode the string in cipher.txt 25 times. I searched in the web for base64 decoder and ended up at 
http://www.utilities-online.info/base64/#.XvN-9aYpCXh . Here I decoded the text 25 times and got the flag: flag{l00ks_l1ke_a_l0t_of_64s}.

However, I felt this did not fulfill my curiosity on this challenge, my objective now was to automate the process of decoding the code 25 times.
For that purpose I start coding in Python3 and got this code to work:

![python Base 64 Decoding (25 times)](https://github.com/Yukjed/redpwn_2020CTF/blob/master/crypto/base646464/pythonBase64Decoding.png)

So, basically the program opens the cipher.txt file, reads the string and starts decoding it in the loop. After 25 loops the string is displayed to the terminal.

![Code Testing](https://github.com/Yukjed/redpwn_2020CTF/blob/master/crypto/base646464/pythonBase64.png)





Já podem parar de fingir que estão a ler o relatório: MangCTF{Na0_ign0rem_0s_v0ss0s_4m1gos}
