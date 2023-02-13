max_place = range(1,51)
def deliver(place):
        if place in max_place:
            return  True
        else:
            print(f"Xurmatli mijoz bizda bunday raqamli otirish joyi yo'q iltimos joyizni raqamini yaxshilib tekshirib aytib yuvoring!")
            return False