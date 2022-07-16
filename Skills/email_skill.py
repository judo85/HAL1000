
# --- imports

import smtplib



# --- globals

from Skills.skills_settings import *



# --- functions

def parse_address(address):

    ### TODO

    return address, None


def send_email(address, body, subject = None):
    # Check if address in contacts
    if address in CONTACTS.keys():
        address = CONTACTS[address]
    
    # Parse email address
    try:
        address, provider = parse_address(address)
    except:
        return None

    domain = EMAIL_API[provider]['domain']
    port   = EMAIL_API[provider]['port']
    mysmt  = smtplib.SMTP(domain, port)
    mysmt.ehlo()
    mysmt.starttls()
    my_email = MY_EMAIL["email"]
    my_psw   = MY_EMAIL["psw"]

    # Use your own login info; you may need an app password
    mysmt.login(my_email, my_psw)

    # Send the email
    mysmt.sendmail(my_email, address, 
                   f'Subject: {subject}.\n {body}.')
    mysmt.quit()

    return EMAIL_SUCCESS


# --- tests

if __name__ == '__main__':
    pass



### --- NOTES
#
#   Use classes
#
#
#
