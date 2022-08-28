import re

def main():
    print('Hello!')
    line = input('Paste the rate line:')
    print(line)
    m = re.findall('(\d.\d\d)', line)
    print(m)
    print('Term,Posted Rate,Our Rate \\n6 months,%s%%,%s%% \\n1 year,%s%%,%s%% \\n2 years,%s%%,%s%% \\n3 years,%s%%,%s%% \\n4 Years,%s%%,%s%% \\n5 years,%s%%,%s%% \\n7 years,%s%%,%s%% \\n10 years,%s%%,%s%% \\nBridge Loan,n/a \\n HELOC,Prime + %s \\nVariable rate,(P-%s)%% \\nPrime rate,%s%% (TD:%s%%) \\n' % (m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10],m[11],m[12],m[13],m[14],m[15],m[16],m[17],m[18],m[19]))
    
    

if __name__ == '__main__':
  main()
