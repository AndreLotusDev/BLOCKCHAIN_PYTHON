from flask import Flask, jsonify
from controller import BusinessController 

app = Flask(__name__)
business_controller = BusinessController()
        
@app.route('/mine', methods = ['GET']) 
def mine():
    
    response = business_controller.make_block_interaction()
    
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    
    chain = business_controller.get_chain()
    response = {'chain': chain,
                'length': len(chain)}

    print(response['chain'])
    return jsonify(response), 200
        
app.run(host= '0.0.0.0', port = 5000)