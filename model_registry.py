import json
import os
class ModelRegistry:
    def __init__(self, file_name="models.json"):
        self.file_name = file_name

    def load_models(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    def save_models(self, models):
        with open(self.file_name, "w") as file:
            json.dump(models, file, indent=4)

    def generate_model_id(self, models):
        return f"MODEL-{len(models) + 1}"

    def validate_model(self, name, sponsor):
        if not name:
            return "Model name is required"
        if not sponsor:
            return "Sponsor is required"
        return None

    def register_model(self, name, version, sponsor, business_line, model_type, risk, status):
        models = self.load_models()
        error = self.validate_model(name, sponsor)
        if error:
            return {"error": error}
        model_id = self.generate_model_id(models)
        model = {
            "model_id": model_id,
            "name": name,
            "version": version,
            "sponsor": sponsor,
            "business_line": business_line,
            "model_type": model_type,
            "risk": risk,
            "status": status,
            "created_at": str(datetime.datetime.now())
        }

        models.append(model)
        self.save_models(models)
        return model

    def get_all_models(self):
        return self.load_models()
