import random

choices = ['حجر', 'ورقة', 'مقص']

arabic_to_index = {
    'حجر': 0,
    'ورقة': 1,
    'مقص': 2
}

index_to_arabic = choices

def play_round():
    user_choice = input('اختر (حجر/ورقة/مقص): ').strip()
    if user_choice not in arabic_to_index:
        print('اختيار غير صالح. حاول مرة أخرى.')
        return
    comp_choice = random.choice(choices)
    print(f'اختار الحاسوب: {comp_choice}')
    user_idx = arabic_to_index[user_choice]
    comp_idx = arabic_to_index[comp_choice]
    if user_idx == comp_idx:
        print('تعادل!')
    elif (user_idx - comp_idx) % 3 == 1:
        print('فزت!')
    else:
        print('خسرت!')


def main():
    print('مرحبا بك في لعبة حجر ورقة مقص!')
    while True:
        play_round()
        again = input('هل تريد اللعب مرة أخرى؟ (نعم/لا): ').strip().lower()
        if again != 'نعم':
            print('شكرا للعب!')
            break


if __name__ == '__main__':
    main()
