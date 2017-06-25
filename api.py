#!flask/bin/python
from flask import Flask, jsonify, abort
from flask import request
from flask.ext.cors import CORS
import re
import base64
import face_match
import os


# docker run -p 5000:5000 -e PORT=5000  -v "$PWD":/root/face_recognition image/python python3 api.py

#docker run -p 5000:5000 image/python

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/api/onboard/v1', methods=['POST'])
def create_task():
    if not request.json or not 'selfie' in request.json or not 'dni' in request.json:
        print ("Faltan imagenes")
        abort(400, 'faltan imagenes')
    
    print ("Image ...")
    #print (request.json['selfie'])
    dni_img = request.json['dni']
    selfie_img = request.json['selfie']

    print ("selfie")
    dni_img

    print ("dni")
    selfie_img

    
    #dni_img_data = re.sub('^data:image/.+;base64,', '', dni_img)
    #selfie_img_data = re.sub('^data:image/.+;base64,', '', selfie_img)
    

    #dni_img_data  = base64.b64decode(dni_img_data)


    #try:
    #    with open("dni3.png", "wb") as fh:
    #        fh.write(dni_img_data)
    ##        fh.close()
    #except IOError:
    #    print ("Could not read file:") 
    print ("CHECKING PHOTOS .......")

    save_base64_to_image(dni_img, 'tmp_dni123.png')
    save_base64_to_image(selfie_img, 'tmp_selfie123.png')

    check = face_match.test_dni_selfie('tmp_dni123.png', 'tmp_selfie123.png')
    print("CHECK {}".format(check))
    #fh = open("selfie.png", "wb")
    #fh.write(selfie_img_data.decode('base64'))
    #fh.close()

    task = {
        'id': 1,        
        'check': str(check)
        
    }
    
    return jsonify(task), 200


def save_base64_to_image(base64_string, file_name):
    img_data = re.sub('^data:image/.+;base64,', '', base64_string)
    img_data_pure  = base64.b64decode(img_data)
    try:
        with open(file_name, "wb") as fh:
            fh.write(img_data_pure)
            fh.close()
    except IOError:
        print ("Could not write  file "+file_name)




if __name__ == '__main__':



    print ("STARTING API")
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=True,host="0.0.0.0",port=port)



# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book", "image": "data:image/jpeg;base64,R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw=="}' http://localhost:5000/api/onboard/v1


#data:image/jpeg;base64,R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw==
