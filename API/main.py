from main_manager import MainManager

if __name__ == "__main__":

    checkpoint = 1

    main_manager = ManageMain()
    
    main_manager.display_welcome_screen()

    while(checkpoint == 1):
        main_manager.start_calibration_screen()
        checkpoint = 2

        while(checkpoint == 2):
            main_manager.data_entry_screen()
            checkpoint = 3

            while(checkpoint == 3):
                main_manager.data_acquisition_screen()
                checkpoint = 4

                while(checkpoint == 4):
                    if main_manager.repeat_or_close_screen() == 'Q':
                        checkpoint = 0
                    else:
                        checkpoint = 1
