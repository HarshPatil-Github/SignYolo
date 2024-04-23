from ultralytics import YOLO

model = YOLO("runs/detect/train9/weights/best.pt")



# Train the model
result = model.train(data="config.yaml", epochs=1)
