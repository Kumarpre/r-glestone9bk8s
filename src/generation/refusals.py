class RefusalHandler:
    @staticmethod
    def get_refusal(category: str) -> str:
        base_footer = "\n\nSource: https://groww.in/p/mutual-funds\nLast updated from sources: System Policy"
        
        if category == "ADVICE":
            message = "I am a factual assistant and cannot provide investment advice, predictions, or opinions on whether a fund is 'good' or 'bad'."
            return message + base_footer
            
        elif category == "COMPARISON":
            message = "I cannot compare multiple funds or suggest which one is better. I can only provide objective facts about a single fund at a time."
            return message + base_footer
            
        else:
            message = "I can only answer factual questions related to the specified HDFC mutual funds."
            return message + base_footer
