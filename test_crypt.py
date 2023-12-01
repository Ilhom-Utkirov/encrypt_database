class Crypto:
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                               'UPHTIVJCEGWRNMYBXLZDAFKQOSuphtivjcegwrnmybxlzdafkqos9512374860')

    # Function to translate plain text
    def rot13(self, text):
        return text.translate(self.rot13trans)



