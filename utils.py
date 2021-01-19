def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Gunting', 'Kertas']
    print(name + ' memilih: ' + hands[hand])

def judge(player, friend):
    if player == friend:
        return 'Seri 😉'
    elif player == 0 and friend == 2:
        return 'Kalah 🙁'
    elif player == 1 and friend == 0:
        return 'Kalah 🙁'
    elif player == 2 and friend == 1:
        return 'Kalah 🙁'
    else:
        return 'Menang 🤩'
