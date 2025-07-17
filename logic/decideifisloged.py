if (user != None):
    if(login == true):
        redirect(home_screen)
else:
    redirect(sign_up_screen)