str1 = '/*Jon is @developer & musician!!'

str1 = str1.replace('@', '#')
str1 = str1.replace('&', '#')
str1 = str1.replace('/', '#')
str1 = str1.replace('*', '#')

print(str1)

#Output: #Jon is #developer # musician!!