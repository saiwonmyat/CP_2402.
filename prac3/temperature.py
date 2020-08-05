def celsius_to_fahrenheit(ct):
  Fahrenheit=ct*1.8+32.0
  print (Fahrenheit)

def main():
  f = float(input("Enter the celsicus: "))
  fahrenheit = celsius_to_fahrenheit(f)
  return fahrenheit
main()