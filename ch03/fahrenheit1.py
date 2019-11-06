

def fahrenheit_to_celsius(fahrenheit):
    print('화씨온도 :', fahrenheit)
    cel = fahrenheit
    for i in range(len(fahrenheit)):
        cel[i] = (fahrenheit[i]-32)*5/9
    print('썹씨온도 :', cel)

sample_temperature_list = [40,15,32,64, -4, 11]

fahrenheit_to_celsius(sample_temperature_list)
