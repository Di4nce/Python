def skriv_timer_minutter(antall_timer=12, antall_minutter=60):  # = default verdier
    for time in range(1, antall_timer+1):
        print(time)
        for minutt in range(1, antall_minutter+1):
            print(f"{time}:{minutt}")


skriv_timer_minutter(7 ,4)
skriv_timer_minutter()
skriv_timer_minutter(4)                     # endrer første parameter
skriv_timer_minutter(antall_minutter=4)     # for å kun endre siste parameter
