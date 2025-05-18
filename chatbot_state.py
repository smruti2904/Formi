from template_utils import render_prompt
from property_info import get_property_info  # Adjust import if filename differs

class ChatbotStateMachine:
    def __init__(self):
        self.state = "ask_location"
        self.context = {}

    def handle_input(self, user_input):
        if self.state == "ask_location":
            # Call KB API to validate location
            prop = get_property_info(user_input)
            if prop:
                self.context["property"] = prop
                self.state = "confirm_location"
                # Render confirmation prompt with property details
                return render_prompt("state_confirm_location.j2", property=prop)
            else:
                return "Sorry, we don't have any outlet in that location. Could you please provide a different city or outlet?"

        elif self.state == "confirm_location":
            # Accept positive confirmations
            if user_input.lower() in ["yes", "y", "correct"]:
                self.state = "next_state"  # Next flow, e.g., booking
                return "Great! How can I assist you with your booking today?"
            # Explicitly handle negative confirmation
            elif user_input.lower() in ["no", "n"]:
                self.state = "ask_location"
                return "Okay, please tell me the city or outlet you are interested in."
            else:
                # Ask user to respond clearly
                return "Please reply with 'yes' or 'no'. Is the location correct?"

        else:
            return "Sorry, I didn't get that. Could you please repeat?"