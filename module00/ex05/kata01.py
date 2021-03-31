#!/usr/bin/env python3

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

def main():
    for lang in languages:
        print(f'{lang} was created by {languages[lang]}')

if __name__ == "__main__":
    main()