from manage_main import ManageMain

if __name__ == "__main__":

    checkpoint = 1

    manage_main = ManageMain()
    
    manage_main.display_welcome_screen()

    while(checkpoint == 1):
        manage_main.start_calibration_screen()
        checkpoint = 2

        while(checkpoint == 2):
            manage_main.data_entry_screen()
            checkpoint = 3

            while(checkpoint == 3):
                manage_main.data_acquisition_screen()
                checkpoint = 4

                while(checkpoint == 4):
                    if manage_main.repeat_or_close_screen() == 'Q':
                        checkpoint = 0
                    else:
                        checkpoint = 1
