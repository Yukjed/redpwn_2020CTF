Solution/Flag: flag{l00ks_l1ke_a_l0t_of_64s}


The challenge's tittle often provide some aid or direction to solve the problem. Here, the tittle repites the number 64 three times, which can be a hint to
decode a Base64 string three (or a couple of) times.


The problem also gives two files: generate.js and cipher.txt.
generate.js is a ASCII text file, with the Javascript extension.
cipher.txt is a ASCII text, with very long lines, with no line terminators file.


Let's take a look of the file and see what it does. Finding the purpose of the program will be the key to find the decryption process.
First, there's a constant btoa that will initialize a buffer so the string that the program will read later on is treated as a base64 string (or number). This is
a function that will take a string and encode it with as base64.

Moreover, we can see some file realted intrstuictions. In a nutshell, the program reads the string from the text file (flag.txt) into a constant.

The interesting part is within the loop. We can easily see that it will repeat some sort of instruction 25 times. From i=0 to i=25 (it does not execute the
i=25 loop). Each instruction will call the function btoa, it will take the string (which was initially read from the file) and encode it as a base64.

Finally the last instruction will write the string (base 64 number encode 25 times) to the cipher.txt file that was given to us.
P.S.: Each string we can see uses the UTF-8 binary classification, which we know it will follow the ASCII byte representation.

base
So, at this point I knew all I had to do is to decode the string in cipher.txt 25 times. I searched in the web for base64 decoder and ended up in 
http://www.utilities-online.info/base64/#.XvN-9aYpCXh . Here I decoded the text 25 times and got the flag: flag{l00ks_l1ke_a_l0t_of_64s}.

However, I felt this did not fulfill my curiosity on this challange, my objective know was to autmate the process of decoding the code 25 times.
For that purpose I start coding in Python3 and got this code to work:


So, basically the program opens the cipher.txt file, reads the string and starts decoding it in the loop. After 25 loops the string is displayed to the terminal.
