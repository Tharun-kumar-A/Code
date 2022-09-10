import csv
#from passlib.hash import pbkdf2_sha256

path = "/storage/emulated/0/MEDIA/document/AcodeProjects/Python/LogIn/logInData.csv"

def main():
	a=1
	while(a!=3):
		print('''\n
----------------MENU--------------
  1. Log in
  2. Sign up
  3. Exit
----------------------------------
\n''')
		a= int(input("\nEnter your choice (1/2/3) : "))
		if(a==1):
			set_up(1) #log in
		elif(a==2):
			set_up(2) #sign up
		elif(a==3):
			print('''
####   #    #  ######
#  #    #  #   #
######   ##    ######
#    #   ##    #
######   ##    ######  # # #
				''')
		else:
			print("\nERR34_INVALID_OPTION")

def set_up(a):
	with open(path,'r') as l:
	# import the UIDs
	    read=csv.reader(l,delimiter=',')
	    myUid=[]
	    myName=[]
	    myPass=[]
	    myData=[]
	    lines=[]
	    
	    for row in read:
	    	if(row!=[]):
	    		myUid.append(int(row[0]))
	    		myName.append(row[1])
	    		myPass.append(row[2])
	    		myData.append(row[3])
	    		lines.append(row)
	    #print(myUid)
	    if(a==1):
	    	log_in(myUid,myName,myPass,myData,lines)
	    elif(a==2):
	    	sign_up(lines)
	# csv file 'l' scope ends here
def log_in(mU,mN,mP,mD,lst):
	uid= int(input("\nEnter your UID : "))
	index=binary_search_recur(mU,0,len(mU)-1,uid)
	if(index==-1):
		print("\nERR31_INVALID_UID")
		return None
	pasw=str(input("\nEnter the password : "))
	if(pasw!=mP[index]):
		print("\nERR42_INVALID_PASSWORD")
		return None
	logged_in(uid,index,mN[index],mP[index],mD[index],lst)
def sign_up(lst):
	modi=lst[0]
	ind=int(modi[0])
	uid=12344+ind
	name=str(input("\nEnter Your Username : "))
	pas=str(input("\nEnter the password : "))
	repas=str(input("\nReconfirm the password : "))
	if(pas!=repas):
		print("\nERR72_PASSWORD_MISMATCH")
		return None
	newrow=[uid,name,pas,""]
	print("\nNote:\n\t Your UID : ",uid)
	sto=input("\nPress Enter to continue...\n")
	ind+=1
	modi[0]=ind
	lst[0]=modi
	with open(path,'w') as li:
		writer=csv.writer(li)
		writer.writerows(lst)
	with open(path,'a') as lis:
		write=csv.writer(lis)
		write.writerow(newrow)
	return None
def logged_in(uid,ind,name,pas,dat,lst1):
	a=1
	while(a!=6 and a!=5):
		print("\nHi, ",name)
		print('''\n
----------------MENU--------------
  Your Uid : %u
  Data : %s
	1. Change the User Data
	2. Change UserName
	3. Change Password
	4. Save 
	5. Save and Log off
	6. Delete Account
----------------------------------
		\n'''%(uid,dat))
		a=int(input("\nEnter your option : "))
		if(a==1):
			dat=input("\nEnter the new data : ")
		elif(a==2):
			name=input("\nEnter the new UserName : ")
		elif(a==3):
			newpass=input("\nEnter the Old password : ")
			if(newpass==pas):
				cpas=input("\nEnter the new password : ")
				conp=input("\nReconfirm the password : ")
				if(cpas==conp):
					pas=cpas
				else:
					print("\nERR72_PASSWORD_MISMATCH")
			else:
				print("\nERR73_WRONG_PASSWORD")
		elif(a==4):
			print("\nSaved...")
			lst1[ind]=[uid,name,pas,dat]
		elif(a==5):
			print("\nLogged off...")
			lst1[ind]=[uid,name,pas,dat]
		elif(a==6):
			yon=input("\nDo you want to continue ? (Y/N) : ")
			if(yon=='Y' or yon=='y'):
				lst1[ind]=[]
				print("\nYour account is deleted...")
			elif(yon=='N' or yon=='n'):
				print("\nOperation Cancelled...")
				a=1
			else:
				print("\nERR34_INVALID_OPTION")
		else:
			print("\nERR34_INVALID_OPTION")
	with open(path,'w') as lin:
		wrt=csv.writer(lin)
		wrt.writerows(lst1)
def binary_search(array, query): 
    lo,hi=0,len(array)-1 
    while lo<=hi: 
        mid=(hi+lo)//2 
        val=array[mid] 
        if val==query: 
            return mid 
        elif val < query: 
            lo=mid+1 
        else: 
            hi=mid-1 
    return None
 
def binary_search_recur(array, low,  high, val): 
	if low > high:
		return -1
	mid = (low + high) // 2
	if val < array[mid]:
		return binary_search_recur(array, low, mid - 1, val)
	elif val > array[mid]:
		return binary_search_recur(array, mid + 1, high, val)
	else: 
		return mid
main()