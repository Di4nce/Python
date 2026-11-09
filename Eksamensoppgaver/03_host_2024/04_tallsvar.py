# Tallsvar
# a) Hva er verdien til det binære tallet 10101 med vanlige tall?
#Svar: 21

# b) La oss si du har et passord med 10 tegn, hvor hvert tegn kan være en stor bokstav i det
# engelske alfabetet (26 tegn), en liten bokstav i det engelske alfabetet, et tall, eller et av
# spesialtegnene punktum, komma, anførselstegn, utropstegn, vanlig startparentes og vanlig
# sluttparentes. La oss si at en angriper har en datamaskin som kan prøve 2 000 000 passord i
# sekundet. Hvor mange år vil det ta å teste alle mulighetene her? Du kan anta et år er 365 dager.
# Rund av til nærmeste heltall antall år:
# Svar:
# kombinasjoner (26+26+10+6)**10 = 2.11392282x10**18
# Utregninger pr år: 2 000 000 * 3600 * 24 * 365
# 33516 år


# c) Gitt følgende Python-sctipt. Hva skrives ut?
# tall = 0
# for i in range(1, 6): 1: 1, 2: 3, 3: 6, 4: 10, 5: 15
#     tall += i
# print(tall)
# Svar 1, 3, 6, 10, 15. 15 er svaret.

# d) Gitt følgende Python-sctipt. Hva skrives ut?
# tall = 100
# i = 20
# while tall > 0:
#     tall = tall - i
#     if i>5:
#         i = i-2
# print(tall)

# Svar: -4
# tanke
# 80 (18)
# 62 (16)
# 46 (14)
# 32 (12)
# 20 (10)
# 10 (8)
# 2 (6)