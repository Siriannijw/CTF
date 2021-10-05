# spelling-quiz
Category: Cryptography\
Points: 100

## Description
I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.\
[public.zip](https://artifacts.picoctf.net/picoMini+by+redpwn/Cryptography/spelling-quiz/public.zip)

## Solution

### Brute Force
This problem isn't able to be brute forced easily. There are 148,362,637,348,470,135,821,287,825 permutations with 26 unique members.

### Frequency Analysis

One approach is to use frequency analysis. Some letters are used more than others in words, and that can be used to get a general idea of which letters can be paired with others. Below is a table with the frequency of the encrypted letters of the study guide in comparison with the frequency of letters used in a [dictionary](https://en.wikipedia.org/wiki/Letter_frequency). You can see some general correlations which can significantly reduce the number of likely permutations.

| Letter | Dictionary | Study Guide |
| ------ | ---------- | ----------- |
| a      | 7.88       | 7.10        |
| b      | 1.94       | 3.32        |
| c      | 3.98       | 7.07        |
| d      | 3.88       | 2.29        |
| e      | 11.45      | 0.51        |
| f      | 1.37       | 2.63        |
| g      | 3.08       | 0.59        |
| h      | 2.36       | 0.11        |
| i      | 8.61       | 7.39        |
| j      | 0.23       | 0.16        |
| k      | 1.02       | 0.41        |
| l      | 5.23       | 5.59        |
| m      | 2.74       | 3.12        |
| n      | 7.18       | 4.52        |
| o      | 5.98       | 3.69        |
| p      | 2.80       | 0.94        |
| q      | 0.19       | 1.99        |
| r      | 7.15       | 10.72       |
| s      | 8.71       | 2.99        |
| t      | 6.67       | 7.47        |
| u      | 3.34       | 1.70        |
| v      | 1.03       | 6.82        |
| w      | 0.93       | 9.29        |
| x      | 0.27       | 8.23        |
| y      | 1.53       | 1.05        |
| z      | 0.43       | 0.29        |

### Large Words

Unfortunately, all words in the study guide are likely not in a standard dictionary. There were some words in the study guide that were abnormally long. There are not many words in the English dictionary that have similar lengths, making it easy to compare and find a similar letter pattern. Below are two I was able to identify.

| Num | Encrypted                       | Pattern Match                   |
| --- | ------------------------------- | ------------------------------- |
| 31  | mwnflicimwbfrtqlvcwnflicirvfxtr | dichlorodiphenyltrichloroethane |
| 28  | xtvwmwaravxulwafsrtvxcwxtwas    | antidisestablishmentarianism    |

Between these two matches, there are 20 unique letters. The gives 6 remaining letters, totaling 265 permutations.

Pairing the 20 decrypted letters with all 265 permutations, and selecting the one with the highest word matches in the dictionary allowed me to get the full decryption cipher. 

### Flag
```
```