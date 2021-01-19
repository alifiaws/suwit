import utils

import random # import module random

print('✨ Memulai Permainan Batu Gunting Kertas ✨')
player_name = input('Halo! Siapa Namamu? : ')

print('Ayo pilih mana? (0: Batu 👊, 1: Gunting ✌️, 2: Kertas 🖐️)')
player_hand = int(input('Masukkan Nomor Pilihanmu (0-2): '))

if utils.validate(player_hand):
    friend_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(friend_hand, 'Temanmu')

    result = utils.judge(player_hand, friend_hand)
    print('Hasil: ' + result)
else:
    print('Mohon Masukkan Nomor Yang Benar Ya 😊')
