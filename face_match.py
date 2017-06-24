#docker run  -v "$PWD":/root/face_recognition image/python python3 test.py

#docker run  -v "$PWD":/root/face_recognition image/python python3 test.py

import face_recognition




def test_dni_selfie(know_file, unk_file):
	know = face_recognition.load_image_file(know_file)
	unk = face_recognition.load_image_file(unk_file)


	know_encoding = face_recognition.face_encodings(know)[0]
	unk_encoding = face_recognition.face_encodings(unk)[0]


	results = face_recognition.compare_faces([know_encoding], unk_encoding)
	print("Is the unknown face  ? {}".format(results[0]))
	return results[0]




def test():
	dni = face_recognition.load_image_file("images/chily1.jpg")
	test1 = face_recognition.load_image_file("images/chily0.jpg")
	test2 = face_recognition.load_image_file("images/chily2.jpg")
	test3 = face_recognition.load_image_file("images/obama.jpg")
	 



	# Get the face encodings for each face in each image file
	# Since there could be more than one face in each image, it returns a list of encordings.
	# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
	dni_encoding = face_recognition.face_encodings(dni)[0]
	test1_encoding = face_recognition.face_encodings(test1)[0]


	# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
	results = face_recognition.compare_faces([dni_encoding], test1_encoding)
	print("Is the unknown face  ? {}".format(results[0]))

	results = face_recognition.compare_faces([dni_encoding], face_recognition.face_encodings(test2)[0])
	print("Is the unknown face  ? {}".format(results[0]))

	results = face_recognition.compare_faces([dni_encoding], face_recognition.face_encodings(test3)[0])
	print("Is the unknown face  ? {}".format(results[0]))

	print ("hola !!!")


if __name__ == '__main__':
	test()