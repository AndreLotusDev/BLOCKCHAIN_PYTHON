from blockchain import Blockchain 

class BusinessController:
    
    def __init__(self):
        
        self.blockchain = Blockchain()
        
    def make_block_interaction(self):
        
        block = self.blockchain.mine()
        
        response = {'message': 'Parabens voce minerou um bloco!', 
                    'index': block[self.blockchain.INDEX],
                    'timestamp': block[self.blockchain.TIMESTAMP],
                    'proof': block[self.blockchain.PROOF],
                    'previous_hash': [self.blockchain.PREVIOUS_HASH] }
                    
        return response
                                       
    def get_chain(self):
        return self.blockchain.chain         
            