
def detect(filename):
    from imageai.Detection.Custom import CustomObjectDetection
    import os
    items = []
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("detection_model-ex-004--loss-0018.229.h5")
    detector.setJsonPath("detection_config.json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=filename, minimum_percentage_probability=60, output_image_path="detected.jpg")
    for detection in detections:
        items.append(detection["name"])
    os.remove("detected.jpg")
    return items
