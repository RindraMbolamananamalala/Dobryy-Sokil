from PRESENTATION.VIEW.rindra_view import Rindra_View, ViewWidgetsId

from BUSINESS.MODEL.DOMAIN_OBJECTS.rindra import Rindra

from BUSINESS.SERVICES.APPLICATION_SERVICES.rindra_SA import RindraSA


class RindraController:

    def set_rindra_view(self, rindra_view):
        self.rindra_view = rindra_view

    def get_rindra_view(self):
        return self.rindra_view

    def set_rindra_sa(self, rindra_sa):
        self.rindra_sa = rindra_sa

    def get_rindra_sa(self):
        return self.rindra_sa

    def __init__(self, rindra_view):
        # Preparing the View Part
        self.set_rindra_view(rindra_view)
        self.get_rindra_view().manage_event(ViewWidgetsId.BUTTON_ADD_NEW_RINDRA, self.event_button_add_clicked)
        self.get_rindra_view().manage_event(ViewWidgetsId.BUTTON_LIST, self.event_button_list_clicked)

        # Preparing the Application Service part
        self.rindra_sa = RindraSA()

    def event_button_add_clicked(self):
        rindra_to_save_text = self.get_rindra_view().get_user_input_text()
        rindra_to_save = Rindra(rindra_to_save_text)
        self.get_rindra_sa().add_new_rindra(rindra_to_save)

        # refreshing the text area showed to the user
        self.get_rindra_view().update_text_to_show_to_user('')

    def event_button_list_clicked(self):
        rindras = self.get_rindra_sa().get_all_rindras()
        rindras_text = "\n" \
            .join([str(line.get_data()) for line in rindras])
        self.get_rindra_view().update_text_to_show_to_user(rindras_text)