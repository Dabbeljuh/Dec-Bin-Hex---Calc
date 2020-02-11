# integer number to binary number
def integer_to_bin(dec):
  return bin(int(dec))
# inteintegerger number to hexainteger number
def integer_to_hexdec(dec):
  return hex(int(dec))
# binary number to integer number
def bin_to_integer(binary):
  return int(str(binary), 2)
# binary to hexainteger
def bin_to_hexdec(binary):
  return hex(int(str(binary), 2))
# hexainteger to binary
def hex_to_bin(hex):
  return bin(int(hex, 16))
# hexacimal to integer
def hex_to_integer(hex):
  return int(hex, 16)
# binary with decimal point to decimal 
def bin_decimal_to_decimal(dec):
  s = str(dec)
  s1, s2 = s.split(".")
  s1 = int(s1, 2)
  s2 = int(s2, 2)/(2**len(s2))
  return s1 + s2   

def type_recognizer():
  again = 'y'
  while again == 'y' or again == 'Y':
    print("Please enter number: ")
    print("For binary start with '0b' ")
    number = input("for hexainteger start with '0x': \n ")
    
    if number[0:2] == '0b':
      if '.' in str(number):
        print("decimal: ", bin_decimal_to_decimal(number))
      else:
        print('integer:', bin_to_integer(number))
        print('hex:', bin_to_hexdec(number))
    elif number[0:2] == '0x':
      print('integer:', hex_to_integer(number))
      print('binary:', hex_to_bin(number))
    
    else:
      try:
        float(number)
        print("binary:", integer_to_bin(number)) 
        print("hex: ", integer_to_hexdec(number))
      except ValueError:
        print("no valid number")
    again = input('again? y/n: \n' )
  

  
type_recognizer()

''' 
test_dec = 'aaa1.5'
test_hex = '1A6B.B'
test_bin = 100000111101.001 '''

