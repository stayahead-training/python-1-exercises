# the open builtin function is used to read and write files
# the object returned by open is iterable
VAT_RATE = 1.2
file_in = open('prices.dat')
file_out = open('prices_with_vat.dat', 'w')

for line in file_in:
    # code a function that will test ALL chars in the string for valid number chars
    if line and line[0] in '0123456789.-':
        price = float(line)
        price_with_vat = price * VAT_RATE
        file_out.write(str(price_with_vat) + '\n')
               
file_in.close()
file_out.close()