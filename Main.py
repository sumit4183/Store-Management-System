import Login as l
import Menu as m
i=l.check()
if i==1:
    print("\nLogged in successfully!")
    input("Press enter key to continue\n>")
    m.menu()
else:
    print("\nERROR!\nUser id or password is invalid")


