class DataProcessor:
    def filter_data(self, data):
        # Example filter: only include breeds with a male weight minimum greater than 20 kg
        return [breed for breed in data['data'] if breed['attributes']['male_weight']['min'] > 20]

    def transform_data(self, data):
        # Example transformation: extract only the breed name and male weight
        return [{'Breed': breed['attributes']['name'], 'Male Weight': f"{breed['attributes']['male_weight']['min']} - {breed['attributes']['male_weight']['max']} kg"} for breed in data]