class FinalScreen:
    is_first_time = True

    def set_final_screen(self):
        if FinalScreen.is_first_time:
            self._create_final_screen_widget()
            FinalScreen.is_first_time = not FinalScreen.is_first_time
            
        self._set_buttons_layout()