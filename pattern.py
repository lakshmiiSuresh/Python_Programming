# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         print("*",end ="")
#     print()

#---------------------------------------------------------------------------------------

# *
# * *
# * * *
# * * * * 
# * * * * *

# rows = 5
# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print()

#----------------------------------------------------------------------------------------
# * * * * *
# * * * * 
# * * * 
# * * 
# * 

# rows = 5
# for i in range(rows):
#     for j in range(i):
#         print('',end="")
#     for j in range(rows-i):
#         print('* ',end="")
#     print()


#-------------------------------------------------------------------------------------------------
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# rows = 5
# for i in range(rows):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(rows-i):
#         print("*",end=" ")
#     print()

#-----------------------------------------------------------------------------------
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# rows = 5
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#-----------------------------------------------------------------------------------
#     *
#    * *
#   * * * 
#  * * * *
# * * * * *

# rows = 5
# k = 0
# for i in range(1, rows):
#     for j in range(1,rows-i):
#         print(" ",end=" ")
    
#     while k != 2*i-1:
#         print('*',end=" ")
#         k+=1
#     k = 0
#     print()

#----------------------------------------------------------------------------------
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# #OR

# rows = 5
# for i in range(rows):
#     p = 1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()


#-------------------------------------------------------------------------------------------
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# rows = 4
# k = 1
# for i in range(rows):
#     for j in range(i+1):
#         print(k,end=" ")
#         k+=1
#     print()

#----------------------------------------------------------------------------------------------
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4

# rows = 4
# k = 1
# for i in range(rows):
#     for j in range(i+1):
#         print(k,end=" ")
#     k+=1
#     print()

#---------------------------------------------------------------------------------------------
# 1
# 2 2 
# 1 1 1 
# 2 2 2 2 
# 1 1 1 1 1 

# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if i%2 != 0:
#             print("1",end=" ")
#         else:
#             print("2",end =" ")
#     print()

#-----------------------------------------------------------------------------------------------
#     +
#     +
# + + + + +
#     +
#     +

# rows = 5
# for i in range(1,rows+1):
#     for j in range(i+2):
#         if i%3 == 0:
#             print("+",end=" ")
#     for j in range(1,i+2):
#         print(" ",end=" ")
    
#         if j == i%3:
#             print("+",end=" ")
#     print()


# rows = 5
# for i in range(1,6):
#     if i%3 !=0:
#         for j in range(1,6):
#             if j%3 == 0:
#                 print('+',end=" ")
#             else:
#                 print(' ',end=" ")
#         print()
#     else:
#         for k in range(5):
#             print('+',end=' ')
#         print()
                




    # for j in range(1,i+2):
    #     print(" ",end=" ")
    
    #     if j == i%3:
    #         print("+",end=" ")
    # print()

    # or

n = 5
for i in range(n):
    for j in range(n):
        if (j==2) or (i==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#-----------------------------------------------------------------------------------------------------
# *     *
#  *   *
#    *
#  *   *
# *      *
        
        
n = 5
for i in range(n):
    for j in range(n):
        if (i==j) or (i+j==n-1):
            print("*", end = " ")
        else:
            print(" ",end=" ")
    print()


