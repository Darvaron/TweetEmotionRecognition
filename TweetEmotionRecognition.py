from logic.model import model

def main():
    Emodel = model()
    test_list = ['i started thinking about which spaces made me feel most creative and what characteristics they had',
                 'im sorry i feel so uncertain about it',
                 'i am feeling better though i dont sound it',
                 'i was wondering if you will focus on the problems because any way you are not care for themselves when complaining or feeling needy',
                 'i feel your frustration but it s time to calm the hell down',
                 'i feel all funny sometimes',
                 'i left the theater feeling sad and alone the sudden realization of my own fleeting mortality weighing down each and every step',
                 'i feel terrible when i hurt peoples feelings worse afterwards and i always hope never to do it again',
                 'i imagined being in form fitting clothing that was beautiful looking in the mirror and feeling proud being lighter and more energetic',
                 'i plan to do so by obtaining an mba and from that mba program i feel that the most valuable outcomes i would like']

    for t in test_list:
        print('Tweet: {} \nPredicted Emotion: {}\n'.format(t, Emodel.predict(t)))

if __name__ == "__main__":
    main()