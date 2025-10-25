import cv2 as cv
import numpy as np
import sqlite3
import time
import os
from tensorflow import keras


model = keras.models.load_model('model.h5')
conn = sqlite3.connect('presence_log.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS presence_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_time TEXT,
        exit_time TEXT,
        frame_count INTEGER
    )
''')

cap = cv.VideoCapture('Video_2025-06-13_060505.wmv')
count = 0
presence = 0
entry_time = None
frame_counter = 0
atending_count = 0

while True:
    ret, image = cap.read()
    if not ret:
        break

    img = image[300:600, 200:800]
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_resized = cv.resize(img_gray, (128, 128)) / 255.0
    img_resized = img_resized.astype('float32')
    img_resized = np.expand_dims(img_resized, axis=-1)
    img_resized = np.expand_dims(img_resized, axis=0)

    pred_1 = model.predict(img_resized)
    pred_2 = (pred_1 >= 0.5).astype(int)
    detected = int(pred_2[0])  # 0 or 1
    label = str(detected)
    if presence == 0 and detected == 1:
        presence = 1
        entry_time = time.strftime('%Y-%m-%d %H:%M:%S')
        frame_counter = 1
        atending_count += 1

    elif presence == 1 and detected == 1:
        frame_counter += 1
        atending_count += 1

    elif presence == 1 and detected == 0:
        presence = 0
        exit_time = time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
                INSERT INTO presence_log (entry_time, exit_time, frame_count)
                VALUES (?, ?, ?)
            ''', (entry_time, exit_time, frame_counter))
        conn.commit()

    cv.rectangle(image, (200, 300), (800, 600), (0, 255, 0), 4)
    text_position = (200, 290)
    text_position_2 = (500, 290)
    cv.putText(image, label, text_position, cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
    fainal_count = f"atending time is {int(atending_count/5)} secont"
    cv.putText(image, fainal_count, text_position_2, 
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

    cv.imwrite(os.path.join('pred_2', f"{count}.jpg"), image)
    count += 1

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
conn.close()
cv.destroyAllWindows()
