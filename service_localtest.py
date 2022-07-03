import requests
import base64
import firebase
import env

def postImg(): 
    
    imageFile = open("testing.png", "rb")

    imageBytes = base64.b64encode(imageFile.read())

    response = requests.post(
		"http://127.0.1.1:6969/detect",
		data=imageBytes
	)
    print("Response received!")
    response_data = response.json()
    print(response_data)
    

    db = firebase.Firebase()
    db.authenticate()
    db.push(response_data)
            
def main():
    postImg()

if __name__ == '__main__':
    main()