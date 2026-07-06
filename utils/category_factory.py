from models.category import Category

class CategoryFactory:
    @staticmethod
    def create_category(name: str):
        return Category(name.strip().title())
