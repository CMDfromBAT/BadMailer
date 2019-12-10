#CODED BY CMD
import smtplib
import time

#Func for sending email PLEASE DONT CHANGE THE EMAIL PASSWORD! I`LL BECANE UR IP AND DDoS U!
def sendgoogle(message, target):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('safetyserviceofgogle@gmail.com','dontchangeplease')
    print("Login succesfull");time.sleep(3)
    smtpObj.sendmail('safetyserviceofgogle@gmail.com',target,message)
    print("Email sent!")
    smtpObj.quit()

#FUNC FOR THE EMAIL CONTENT
def mechanism():
    print(" ______      ___     ______                           ")
    print("|      \   /     \  | _____\                          ")
    print("| By    | |       | |       |    _  _    _    _  _    ____   ___ ")
    print("|       | | v.1.0 | |       |   | \/ |  / \   |  |   |___ | | __|         ")
    print("|      /  |  ___  | |       |   |    | /___\  |  |   |      |\                " )
    print("|      \  | |   | | |       |   |    |/     \ |  |__||____| | \                       ")
    print("| CMD   | | |   | | | _____ |                                                       ")
    print("|_______| |_|   |_| |______/                                                          ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<                        ")    
    target = input("Victim E-Mail: ")
    message = input("Your message, for new line write ENTER: ")
    while True:
        if message.__contains__("ENTER"):
            message += ("\n")
            message = message.replace("ENTER", "")
            print (message)
            message += input("Next line of the message: ")
        else:
            print(message)
            sure = input("Is this the message you want to send? y/n: ")
            if sure == "y":
                sendgoogle(message, target)
            else:
                print("False input! Please start the program one time more")



print(" ______      ___     ______                           ")
print("|      \   /     \  | _____\                          ")
print("| By    | |       | |       |    _  _    _    _  _    ____   ___ ")
print("|       | | v.1.0 | |       |   | \/ |  / \   |  |   |___ | | __|         ")
print("|      /  |  ___  | |       |   |    | /___\  |  |   |      |\                " )
print("|      \  | |   | | |       |   |    |/     \ |  |__||____| | \                       ")
print("| CMD   | | |   | | | _____ |                                                       ")
print("|_______| |_|   |_| |______/                                                          ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<                        ")

print("This is BADMAIL by CMD. With this tool you can sendphishing E-Mails\nfrom safetyserviceofgogle@gmail.com")
print("WARNING! USE FOR EDUCATIONAL PURPOSE ONLY!DEVELOPER IS NOT RESPONSIBLE!")
print("RUN AT YOUR OWN RISK!")
safe = input("Are you informed about all risks? [y]/[n]: ")
if safe == "y":
    mechanism()
else:
    print(safe)


