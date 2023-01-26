'''
NAME: ANKIT KUMAR
ID: 2020ucs0118

COMPUTER PROJECT

EFP001MU1M
Computer and Programming Lab
Lab Project - 1 (Week 6)
TOPIC: To implement the facilities available in MS-WORD or LIBRA word.
'''

#Firstly asking the user to input the paragraph


lines=""
list_lines=[] #list is for further uses

print("Enter the song/poem/paragraph/lines :")

while True:
    line1=input()
    if line1:
        lines=lines+line1+'\n'
        list_lines.append(line1)
    else:
        break
print("Entered text is :")
print(lines) # line is printed but the list is stored for further uses

# considering small alphabets (a) and capital alphabets (A) to be different

for i in range (0,26):
    print("\n The functions you can perform are :")
    print("(1)To count the total number of words in the text")
    print("(2)To count total number of a particular alphabet in complete text")
    print("(3)To find whether a word is present or not")
    print("(4)To convert the complete text in the uppercase format")
    print("(5)To convert the complete text in the lowercase format")
    print("(6)To replace a alphabet from complete text")
    print("(7)To insert line number before each line")
    print("(8)To insert the alphabet before each line ")
    print("(9)To insert a special character before each line ")
    print("(10)To add more lines at the end of text")
    print("(11)To remove a specific line from the text ")
    print("(12)To add a word at a particular position in a particular line")
    print("(13)To count number of vowels in a text")
    print("(14)To count total number of lines in text ")
    print("(15)To find number of consonants ")
    print("(16)To add a gap/space in the starting of line(indent) ")
    print("(17)To find the line number of particular line ")
    print("(18)To add space or gap between each line of the text ")
    print("(19)To add a title to your text ")
    print("(20)To compare the length of two lines")
    print("(21)To count the number of words in a specific line ")
    print("(22)To  backprint or reverse the complete paragraph ")
    print("(23)To arrange/sort the lines in ascending order ")
    print("(24)To arrange/sort the lines in descending order ")
    print("(25)To swap two lines of the text")
    print("(26)To END the program(Enter any number greater than 25)")


    #asking user to input the facility number he want to perform
    user_inp=int(input("\nEnter the number ,whose function you want to perform "))


    if (user_inp == 1):

        #To count the total number of words in the text

        print("\nTo count the total number of words in the text")
        line_copy1=lines
        d=line_copy1.split()
        countw=len(d)#number of words in text
        print("The total number of words in complete text entered by user is :",countw) 


    elif (user_inp == 2):

        #To count total number of a particular alphabet in complete text

        line_copy2=lines
        print("\nTo count total number of a particular alphabet in complete text")
        counta=0
        alpha=input("Enter the alphabet whose occurence you want to count : ")
        for i in line_copy2:
            if i == alpha:
                counta= counta+1
        print("The number of times the alphabet ", alpha ," ouccured in text input are :",counta)


    elif (user_inp==3):

        #To find whether a word is present or not

        line_copy3=lines
        print("\nTo find whether a word is present or not")
        word=input("Enter the word you want to find whether it is present or not : ")
        if word in line_copy3:
            print("The word is present in the text")
        else:
            print("The word is not present in the text")


    elif (user_inp==4):

        #To convert the complete text in the uppercase format

        line_copy4=lines
        print("\nTo convert the complete text in the uppercase format")
        st=""
        for i in line_copy4:
            if (ord(i)>96) and (ord(i)<123):
                k=chr(ord(i)-32)
                st=st+k
            else:
                st=st+i
        print("The converted text in uppercase is")
        print(st)


    elif (user_inp==5):

        #To convert the complete text in the lowercase format

        line_copy5=lines
        print("\nTo convert the complete text in the lowercase format")
        st=""
        for i in line_copy5:
            if (ord(i)>64) and (ord(i)<91):
                k=chr(ord(i)+32)
                st=st+k
            else:
                st=st+i
        print("The converted text in lowercase is")
        print(st)


    elif (user_inp==6):

        #To replace a alphabet from complete text

        line_copy6=lines
        print("\n To replace a alphabet from complete text")
        alpha1=input("Enter the alphabet you want to replace : ")
        alpha2=input("Enter the alphabet you want to add in place of previous  alphabet : ")
        string=""
        for i in line_copy6:
            if i == alpha1:
                string=string+alpha2
            else:
                string=string+i
        print("The text after replacement is ")
        print(string)
        

    elif (user_inp==7):

        #To insert line number before each line

        list1=list_lines.copy()
        print("\nTo insert the line number before each line ")
        st=''
        for i in range (0,len(list1)):
            st=st+'('+str((i+1))+')'
            for j in range (0,len(list1[i])):
                st=st+list1[i][j]
            st=st+'\n'
        print("The text after numbering is :")
        print(st)


    elif (user_inp==8):

        #To insert the alphabet before each line

        list2=list_lines.copy()
        st=''
        a=65
        b=65
        c=65
        d=65
        print("\nTo inser alphabets(A,B,C...) before each line ")
        for i in range (0,len(list2)):
            if i<26:
                st=st+'('+chr(a)+')'
                a=a+1
            elif i>25 and i<52:
                st=st+'('+chr(b)*2+')'
                b=b+1
            elif i>51 and i<78:
                st=st+'('+chr(c)*3+')'
                c=c+1
            else:
                st=st+'('+chr(d)*4+')'
                d=d+1
            for j in range (0,len(list2[i])):
                st=st+list2[i][j]
            st=st+'\n'
        print("The text after adding alphabets is")
        print(st)


    elif (user_inp==9):

        #To insert a special character before each line

        list3=list_lines.copy()
        st=''
        print("\nTo insert any symbol (@,#,$,%,&,<,>) before each line ")
        k=input("Enter the symbol you want to add : ")
        for i in range (0,len(list3)):
            st=st+'('+k+')'
            for j in range (0,len(list3[i])):
                st=st+list3[i][j]
            st=st+'\n'
        print("The text after adding symbol is")
        print(st)


    elif (user_inp==10):

        #To add more lines at the end of text

        list4=list_lines.copy()
        line=''
        print("To add more lines at the end of text")
        print("Enter the song/poem/paragraph/lines you want to add at the end of text:")

        while True:
            line1=input()
            if line1:
                line=line+line1+'\n'
                list4.append(line1)
            else:
                break
        m=''
        for i in list4:
            m=m+str(i)+'\n'
        print("New text after addition is:")
        print(m)


    elif (user_inp==11):

        #To remove a specific line from the text

        list5=list_lines.copy()
        print("To remove a specific line from the text")
        print("\nEnter the line number you want to remove")
        k=int(input())
        list5.remove(list5[k-1])
        st=''
        for i in list5:
            st=st+i+'\n'
        print("Text after removing line is:")
        print(st)


    elif (user_inp==12):

        #To add a word at a particular position in a particular line

        list6=list_lines.copy()
        print("To add a word at a particular position in a particular line")
        k=int(input("Enter the position of the line where you want to add a words : "))
        m=int(input("Enter the position of the word after which you want to add a new words : "))
        w=input("Enter the new words you want to add : ")
        b=list6[k-1].split(' ')
        b.insert(m,w)
        st=''

        for i in b:
            st=st+str(i)+' '

        list6[k-1]=st
        st1=''
        for j in list6:
            st1=st1+str(j)+'\n'
        print("Text after the function is performed is:")
        print(st1)


    elif (user_inp==13):

        #To count number of vowels in a text

        lines_copy7=lines
        print("To count number of vowels in a text")
        countv=0
        for i in lines_copy7:
            if i=='a' or i=='e' or i=='i' or i=='o' or i =='u' or i=='A' or i=='E' or i=='I' or i=='O' or i =='U':
                countv=countv+1
        print ("Total number of vowels in the text is ")
        print(countv)


    elif (user_inp==14):

        #To count total number of lines in text
        print("To count total number of lines in text")

        c=len(list_lines)
        print("Total number of lines in text is ",c)
        
        

    elif (user_inp==15):

        #To find number of consonants

        lines_copy8=lines
        print("To find number of consonants")
        countc=0
        for i in lines_copy8:
            if (i>='a' and i<='z') or (i>='A' and i<='Z'):
                if i!='a' and i!='e' and i!='i' and i!='o' and i !='u' and i!='A' and i!='E' and i!='I' and i!='O' and i !='U' :
                    countc=countc+1
        print ("Total number of consonants in the text is ")
        print(countc)


    elif (user_inp==16):

        #To add a gap/space in the starting of line(indent)

        list7=list_lines.copy()
        print("To add a gap/space in the starting of line(indent)")
        st3=''
        print("Function to add space or indent")
        print("Hint : (' '*n) n here is number of space(indent)")
        k=int(input("Enter the value for n "))
        for i in range(0,len(list7)):
            st3=st3+' '*k+list7[i]+'\n'
        print("Text after adding indent  is : ")
        print(st3)


    elif (user_inp==17):

        #To find the line number of particular line

        list8=list_lines.copy()
        print("To find the line number of particular line")

        find_line=input("Enter / paste the line whose line number you want to know : ")
        for i in range(0,len(list8)):
            if list8[i]==find_line:
                k=i+1
        print("The line number of line you entered is ")
        print(k)


    elif (user_inp==18):


        #To add space or gap between each line of the text
        print("To add space or gap between each line of the text")

        list9=list_lines.copy()
        st=''
        print("Function to add spacing between each line")
        for i in range(0,len(list9)):
            st=st+'\n'+' '+'\n'+list9[i]+'\n'
        print("Text after spacing  is : ")
        print(st)


    elif (user_inp==19):

        #To add a title to your text
        print("To add a title to your text")

        list10=list_lines.copy()
        title=input("Enter the title you want to add : ")
        string='\nTITLE : '+title

        for i in list10:
            string=string+'\n'+i
        print("Text after adding title is :")
        print(string)


    elif (user_inp==20):

        #To compare the length of two lines
        print("To compare the length of two lines")

        list11=list_lines.copy()
        k=int(input("Enter the first line number to compare : "))
        m=int(input("Enter the second line number to compare with : "))
        if (len(list11[k-1])>len(list11[m-1])):
            print("The line number ",k," is greater than line number ",m)
        else:
            print("The line number ",m," is greater than line number ",k)


    elif (user_inp==21):

        #To count the number of words in a specific line
        
        print("To count the number of words in a specific line")

        list12=list_lines.copy()
        m=int(input("Enter the line number number in which you want to count the total words"))
        b=list12[m-1].split()
        c=len(b)
        print ("Total number of words in line number ",m,"is : ", c)


    elif (user_inp==22):

        #To backprint the text i.e., to reverse each word and line
        print("To backprint the text i.e., to reverse each word and line")

        lines_copy9=lines
        print("To backprint the text")
        st=''
        for i in range (len(lines_copy9)-1,-1,-1):
            st=st+lines_copy9[i]
        print(st)


    elif (user_inp==23):

        #To arrange/sort the lines in ascending order
        print("To arrange/sort the lines in ascending order")

        list13=list_lines.copy()
        print("To sort the line in ascending order")
        
        for i in range (0,len(list13)):
            max=''
            flag=0
            for j in range(0,len(list13)-1):
                if list13[j]>list13[j+1]:
                    max=list13[j+1]
                    list13[j+1]=list13[j]
                    list13[j]=max
                    flag=1
            if flag==0:
                break

        st=''
        for i in range (0,len(list13)):
            st=st+list13[i]+'\n'

        print("The text in ascending order")
        print(st)


    elif (user_inp==24):

        #To arrange/sort the lines in descending order
        print("To arrange/sort the lines in descending order")

        list14=list_lines.copy()
        print("To sort the text in descending order ")
        for i in range (0,len(list14)):
            max=''
            for j in range(i,len(list14)):
                if list14[j]>max:
                    max=list14[j]
                    t=j
            list14[t]=list14[i]
            list14[i]=max

        st=''
        for i in range (0,len(list14)):
            st=st+list14[i]+'\n'

        print("The text in descending order")
        print(st)

    elif (user_inp==25):

        #To swap two lines of the text
        print("To swap two lines of the text")


        list15=list_lines.copy()
        k=int(input("Enter the line number of the first line you want to swap : "))
        m=int(input("Enter the line number of second line with which you want to swap the first line : "))
        t=[]
        t=list15[k-1]
        list15[k-1]=list15[m-1]
        list15[m-1]=t
        st2=''
        for i in list15:
            st2=st2+i+'\n'
        print("Text after swapping is : ")
        print(st2)


        

    else:
        print("The Program is ended ")
        break
    

