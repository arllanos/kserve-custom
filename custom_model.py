import kserve
from typing import Dict
from ray import serve

@serve.deployment(name="custom-model", num_replicas=2)
class AlexNetModel(kserve.KFModel):
    def __init__(self):
       self.name = "custom-model"
       super().__init__(self.name)
       self.load()

    def load(self):
        pass

    def predict(self, request: Dict) -> Dict:
        pass

if __name__ == "__main__":
    kserve.KFServer().start({"custom-model": AlexNetModel})