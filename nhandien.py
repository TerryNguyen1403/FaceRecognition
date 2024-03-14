import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import subprocess

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng nhận diện khuôn mặt")


        self.image_path = None
        self.image_label = tk.Label(root,bg="#FFFFFF")
        self.image_label.pack(padx=200, pady=100)

        browse_button = tk.Button(root, text="Chọn hình ảnh", command=self.browse_image,bg="#4CAF50", fg="white")
        browse_button.pack(pady=10)

        recognize_button = tk.Button(root, text="Nhận diện hình ảnh", command=self.recognize_face,bg="#3498db", fg="white")
        recognize_button.pack(pady=10)

        run_script_button = tk.Button(root, text="Nhận diện bằng webcam", command=self.run_another_file,bg="#e74c3c", fg="white")
        run_script_button.pack(pady=10)

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Select Image",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, path):
        image = Image.open(path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def recognize_face(self):
        if self.image_path:
            image = cv2.imread(self.image_path)
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=3)

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Nhận diện hình ảnh", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            tk.messagebox.showerror("Lỗi", "Vui lòng chọn hình ảnh trước")

    def run_another_file(self):
        try:
            subprocess.run(["python", "C:/Users/datvi/Downloads/FaceRecognition-master/FaceRecognition-master/FaceRecognition.py"])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error running script: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
