"""
 Contains the class and methods to provide a ticket granting service
 @author Sajal Saha & Kirk Vander Ploeg
"""
import random
import shared_secret_key


class TGS:
    """
    Initialize the TGT and TOKEN lists
    """

    def __init__(self):
        self.TGT = [12121, 123312, 87542, 5689898, 124546]  # VALID TGTs
        self.TOKEN = [14586, 41258, 14589, 54852, 54863]  # VALID TOKENS
        self.ShareKey = shared_secret_key.SHARED_KEY_BTN_TGS_FS

    """
    This method checks the authenticity of the TGT. See inline comments
    for steps. 
    @param tgt TGT for the verification
    @return encrypted after verification of the successful TGT
    """

    def authenticateTGT(self, tgt):
        """
        Implementation Here. Replace None with correct statements on each 
        line.        
        """
        if tgt in self.TGT:  # Update if statement to check weather tgt in TGT list or not.
            index = random.randrange(0, 4)  # create a random index
            token = self.TOKEN[index]  # use index to retrieve a TOKEN
            print("tocken", token)
            encryptedToken = self.encryptTokenToByte(token)  # Call proper method method to encrypt the token.
            print("Enc token", encryptedToken)
            return encryptedToken  # return the encrypted token.
        else:
            return None  # TGT not valid, return None

    """
    This method encrypts a token into bytes. The encryption is done by adding
    the key shared with the fileserver to the token and then converting to 
    bytes. encryptedToken = (token + shared key).to_bytes
    *Hint: see to_bytes() here: https://docs.python.org/3/library/stdtypes.html
    @param token token from TGS
    @return byte array of the encrypted token
    """

    def encryptTokenToByte(self, token):
        changedToken = token + self.ShareKey
        encryptedToken = changedToken.to_bytes((changedToken.bit_length() + 7) // 8, 'big')  # encrypt the token here
        return encryptedToken


k = TGS().authenticateTGT(12121)
