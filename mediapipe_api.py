from mediapipe.tasks import python
from mediapipe.tasks.python import text



class MediaPipeAPI:

    def __init__(self):
        self.base_options = python.BaseOptions(model_asset_path="classifier.tflite")
        self.options = text.TextClassifierOptions(base_options=self.base_options)
        self.classifier = text.TextClassifier.create_from_options(self.options)


    def getScore(self,text):
        classification_result = self.classifier.classify(text)
        top_category = classification_result.classifications[0].categories[0]
        return {'category':top_category.category_name,'score':round(top_category.score,2)}
    
