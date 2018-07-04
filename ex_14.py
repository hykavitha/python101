import sys

print('Arguments:', len(sys.argv))
print('List:', str(sys.argv))

if sys.argv < 2:
    print('To few arguments, please specify a filename')

filename = sys.argv[1]
print('Filename:', filename)
