def decimal_to_bin(dec):
  return bin(int(dec))

def decimal_to_hexdec(dec):
  return hex(int(dec))

def bin_to_decimal(binary):
  return int(str(binary), 2)

def bin_to_hexdec(binary):
  return hex(int(str(binary), 2))

def hex_to_bin(hex):
  return bin(int(hex, 16))

def hex_to_decimal(hex):
  return int(hex, 16)

def bin_float_to_float(dec):
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
    number = input("for hexadecimal start with '0x': \n ")
    
    if number[0:2] == '0b':
      if '.' in str(number):
        print("float: ", bin_float_to_float(number))
      else:
        print('decimal:', bin_to_decimal(number))
        print('hex:', bin_to_hexdec(number))
    elif number[0:2] == '0x':
      print('decimal:', hex_to_decimal(number))
      print('binary:', hex_to_bin(number))
    
    else:
      try:
        float(number)
        print("binary:", decimal_to_bin(number)) 
        print("hex: ", decimal_to_hexdec(number))
      except ValueError:
        print("no valid number")
    again = input('again? y/n: \n' )
  

  
type_recognizer()

''' 
test_dec = 'aaa1.5'
test_hex = '1A6B.B'
test_bin = 100000111101.001 '''

