n1 = float(input('Digite a metragem: '))
cm = n1 * 100
mm = n1 * 1000
dam = n1 / 10
km = n1 / 1000
dm = n1 * 10
hm = n1 / 100
print(f'{n1} m tem {cm :.2f} cm {mm:.2f} mm {dam:.2f} dam {km:.2f} km {dm:.2f} dm {hm:.2f} hm ')
print(f'O valor em milimitro é {mm:.0f} mm')
print(f'O valor em Decímetro é {dm:.0f} dm')
print(f'O valor em Kilomentro é {km:.0f} km')
print(f'O valor em Decâmetro é {dam:.0f} hm')
print(f'O valor em Hectômetro é {hm:.0f} dm')
print(f'O valor em Centímetro é {cm:.0f} cm')

