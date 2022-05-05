import datetime
import hashlib
import json


class Blockchain:

    def __init__(self):

        self.INDEX = 'index'
        self.TIMESTAMP = 'timestamp'
        self.PROOF = 'proof'
        self.PREVIOUS_HASH = 'previous_hash'

        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):

        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}

        self.chain.append(block)
        return block

    def get_previous_block(self):

        return self.chain[-1]

    def proof_of_work(self, previous_proof):

        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = self.do_hash_operation(new_proof, previous_proof)
            if self.validate_hash_operation(hash_operation):
                check_proof = True
            else:
                new_proof += 1

            return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):

        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            if self.is_not_valid_block(block, previous_block):
                return False

            previous_proof = previous_block[self.PROOF]
            proof = block[self.PROOF]
            hash_operation = self.do_hash_operation(proof, previous_proof)

            if self.validate_hash_operation(hash_operation):
                return False

            previous_block = block
            block_index += 1

        return True

    def is_not_valid_block(self, block, previous_block):

        if block[self.PREVIOUS_HASH] != self.hash(previous_block):
            return True

        return False

    def do_hash_operation(self, new_proof, previous_proof):

        return hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

    def validate_hash_operation(self, hash_operation):

        return hash_operation[:4] == '0000'

    def mine(self):

        previous_block = self.get_previous_block()
        previous_proof = previous_block[self.PROOF]
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)

        block = self.create_block(proof, previous_hash)

        return block
