# tasks.py
from celery_co import  shared_task
import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import insightface
from matplotlib import pyplot as plt
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1, extract_face


@shared_task
def process_juvenile_records(train_dir):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20, thresholds=[0.8, 0.9, 0.9], factor=0.709, post_process=True, device=device)
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

    model = insightface.app.FaceAnalysis()
    ctx_id = 0  # to use GPU
    model.prepare(ctx_id=ctx_id)
    
    train_dir = 'D:/FINAL/snoop/media/juveniles/'

    face_db = {}

    X_train = []
    y_train = []

    for person in os.listdir(train_dir):
        person_dir = os.path.join(train_dir, person)
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face = mtcnn(image)
            emb = resnet(face.unsqueeze(0).to(device)).detach().cpu().numpy()
            X_train.append(emb)
            y_train.append(person)

    X_train = np.concatenate(X_train)
    X_train = X_train.reshape(len(X_train), -1)
    y_train = np.array(y_train)

    le = LabelEncoder()
    y_train_enc = le.fit_transform(y_train)

    clf = SVC(probability=True)
    clf.fit(X_train, y_train_enc)

    for person in os.listdir(train_dir):
        person_dir = os.path.join(train_dir, person)
        emb_list = []

        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path)

            faces = model.get(img)

            if faces:
                face = faces[0]
                emb = face.normed_embedding
                emb_list.append(emb)

        if emb_list:
            face_db[person] = np.mean(emb_list, axis=0)

    return 'Processing completed'
