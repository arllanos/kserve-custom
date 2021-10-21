import kserve
from typing import Dict
from ray import serve

@serve.deployment(name="custom-model")
class AlexNetModel(kserve.KFModel):
    def __init__(self):
       self.name = "custom-model"
       super().__init__(self.name)
       self.load()

    def load(self):
        pass

    async def predict(self, request: Dict) -> Dict:
        result = [1, 1]
        return {"predictions": result}

if __name__ == "__main__":
    kserve.KFServer().start({"custom-model": AlexNetModel})