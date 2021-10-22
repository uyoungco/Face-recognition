import face_recognition
from flask import Flask, request, redirect

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/create_face_model', methods=['POST', 'GET'])
def create_face_model():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return redirect(request.url)

        if 'code' not in request.form:
            return redirect(request.url)

        file = request.files['photo']
        code = request.form['code']
        print("code", code)

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            img = face_recognition.load_image_file(file)
            # Get face encodings for any faces in the uploaded image
            unknown_face_encodings = face_recognition.face_encodings(img)
            if len(unknown_face_encodings) == 0:
                return "无法识别出人脸"
            if len(unknown_face_encodings) >= 2:
                return "照片中存在多张人脸"

            # resulst = str(unknown_face_encodings[0])
            arrlist = [str(n) for n in unknown_face_encodings[0]]
            resutl = ",".join(arrlist)
            # return str(resulst)
            return resutl
    return '''
        <!doctype html>
        <title>Is this a picture of Obama?</title>
        <h1>上传照片返回识别编码</h1>
        <form method="POST" enctype="multipart/form-data">
          <input type="file" name="photo">
          <input type="hidden" name="code" value="imooc">
          <input type="submit" value="Upload">
        </form>
        '''


@app.route('/checkin', methods=['POST', 'GET'])
def checkin():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return redirect(request.url)

        if 'targetModel' not in request.form:
            return redirect(request.url)

        file = request.files['photo']
        targetModel = request.form['targetModel']

        target = targetModel.split(",")
        target2 = [float(n) for n in target]

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            img = face_recognition.load_image_file(file)
            # Get face encodings for any faces in the uploaded image
            unknown_face_encodings = face_recognition.face_encodings(img)
            if len(unknown_face_encodings) == 0:
                return "无法识别出人脸"
            if len(unknown_face_encodings) >= 2:
                return "照片中存在多张人脸"

            match_results = face_recognition.compare_faces([target2], unknown_face_encodings[0])
            if match_results[0]:
                return "True"

            return "False"
    return '''
        <!doctype html>
        <title>Is this a picture of Obama?</title>
        <h1>上传照片和提交编码 识别是否为真</h1>
        <form method="POST" enctype="multipart/form-data">
          <input type="file" name="photo">
          <input type="text" name="targetModel" value="">
          <input type="submit" value="Upload">
        </form>
        '''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
