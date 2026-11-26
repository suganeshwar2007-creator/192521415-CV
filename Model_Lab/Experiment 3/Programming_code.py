import cv2
cap = cv2.VideoCapture('traffic.mp4')
if not cap.isOpened():
    print("traffic.mp4 not found!")
    exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
if fps == 0:
    fps = 30

out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
back = cv2.createBackgroundSubtractorMOG2()

print("Video started - press q to stop")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Video finished - saved as output.mp4")
        break

    mask = back.apply(frame)
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 800:
            x, y, w2, h2 = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w2, y+h2), (0, 255, 0), 2)
            cv2.putText(frame, 'Vehicle', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow('Vehicle Detection', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
