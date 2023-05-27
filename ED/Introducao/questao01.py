diai, horarioi = input().split()
fim, horariof = input().split()

horarioi = horarioi.split(":")
horariof = horariof.split(":")
diai = int(diai)
fim = int(fim)
minutosi = int(horarioi[1])
segundosi = int(horarioi[2])
horarioi = int(horarioi[0])
minutosf = int(horariof[1])
segundosf = int(horariof[2])
horariof = int(horariof[0])

tempo_inicial = segundosi + (minutosi*60) + (horarioi*60*60) + (diai*86400)
tempo_final = segundosf + (minutosf*60) + (horariof*60*60) + (fim*86400)
tempo = tempo_final-tempo_inicial

if(tempo <= 0):
    print("Data inválida!")
else:
    dias = tempo//86400
    print(f"{dias} dia(s)")
    tempo -= dias*86400
    horas = tempo//3600
    print(f"{horas} hora(s)")
    tempo -= horas*3600
    minutos = tempo//60
    print(f"{minutos} minuto(s)")
    tempo -= minutos*60
    print(f"{tempo} segundo(s)")